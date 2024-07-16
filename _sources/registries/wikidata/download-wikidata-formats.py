# 
import json
import requests
import re

# Set up the query:
url = 'https://query.wikidata.org/sparql'
# Note that the original version of this query came from the Siegfried Wiki:
# https://github.com/richardlehane/siegfried/wiki/Wikidata-identifier#harvesting
# The original query was developed by Ross Spencer (https://exponentialdecay.co.uk/blog/about/).
query = '''
# Return all file format and family records from Wikidata.
#
SELECT DISTINCT ?uri ?uriLabel ?puid ?extension ?mimetype ?ffw ?lcfdd ?narafpid ?encodingLabel ?referenceLabel ?date ?relativityLabel ?offset ?sig
WHERE
{
  # Return records of type File Format or File Format Family (via instance or subclass chain):
  { ?uri wdt:P31/wdt:P279* wd:Q235557 } UNION 
    { ?uri wdt:P31/wdt:P279* wd:Q26085352 }.
      
  # Only return records that have at least one useful format identifier
  FILTER EXISTS { ?uri wdt:P2748|wdt:P1195|wdt:P1163|wdt:P3381|wdt:P3266|wdt:P11167 [] }.       
  
  OPTIONAL { ?uri wdt:P2748 ?puid.      }          # PUID is used to map to PRONOM signatures
  OPTIONAL { ?uri wdt:P1195 ?extension. }          # File extension
  OPTIONAL { ?uri wdt:P1163 ?mimetype.  }          # IANA Media Type
  OPTIONAL { ?uri wdt:P3381 ?ffw. }                # Entry in the Just Solve File Formats Wiki
  OPTIONAL { ?uri wdt:P3266 ?lcfdd. }              # Library of Congress Format Descriptions ID
  OPTIONAL { ?uri wdt:P11167 ?narafpid. }          # NARA File Format Preservation Plan ID
  OPTIONAL { ?uri p:P4152 ?object;                 # Format identification pattern statement
    OPTIONAL { ?object pq:P3294 ?encoding.   }     # We don't always have an encoding
    OPTIONAL { ?object ps:P4152 ?sig.        }     # We always have a signature
    OPTIONAL { ?object pq:P2210 ?relativity. }     # Relativity to beginning or end of file
    OPTIONAL { ?object pq:P4153 ?offset.     }     # Offset relative to the relativity
    OPTIONAL { ?object prov:wasDerivedFrom ?provenance;
       OPTIONAL { ?provenance pr:P248 ?reference;
                              pr:P813 ?date.
                }
    }
  }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE], en". }
}
ORDER BY ?uri
'''

r = requests.get(url, params = {'format': 'json', 'query': query})
data = r.json()

format_data = []

for r in data['results']['bindings']:
    # Filter down to items with at least one of the identifiers we care about:
    if any(x in r for x in ['puid','extension','mimetype']):
        # Print a sample
        if len(format_data) == 0:
            print("Printing one record to show the general form:")
            print(r)
        #
        item = {
            'id': re.findall(r"Q\d+", r['uri']['value'])[0],
            'source': r['uri']['value'],
            'name': r['uriLabel']['value'],
        }
        # Note that the mutiple fields, e.g. extensions, end up output in diffferent orders each time, which means that diffs are difficult to understand:
        for x in ['puid','extension','mimetype', 'offset', 'sig']:
            if x in r:
                item[x] = r[x]['value']
            else:
                item[x] = None
    
        #print(item)
        format_data.append(item);

with open('wikidata.json','w') as f:
    f.write(json.dumps(format_data, indent=2))

