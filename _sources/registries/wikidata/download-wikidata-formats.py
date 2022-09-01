# 
import json
import requests
import re

url = 'https://query.wikidata.org/sparql'
query = '''
# Return all file format records from Wikidata.
#
select distinct ?uri ?uriLabel ?puid ?extension ?mimetype ?encodingLabel ?referenceLabel ?date ?relativityLabel ?offset ?sig
where
{
  ?uri wdt:P31/wdt:P279* wd:Q235557.               # Return records of type File Format.
  optional { ?uri wdt:P2748 ?puid.      }          # PUID is used to map to PRONOM signatures proper.
  optional { ?uri wdt:P1195 ?extension. }
  optional { ?uri wdt:P1163 ?mimetype.  }
  optional { ?uri p:P4152 ?object;                 # Format identification pattern statement.
    optional { ?object pq:P3294 ?encoding.   }     # We don't always have an encoding.
    optional { ?object ps:P4152 ?sig.        }     # We always have a signature.
    optional { ?object pq:P2210 ?relativity. }     # Relativity to beginning or end of file.
    optional { ?object pq:P4153 ?offset.     }     # Offset relatve to the relativity.
    optional { ?object prov:wasDerivedFrom ?provenance;
       optional { ?provenance pr:P248 ?reference;
                              pr:P813 ?date.
                }
    }
  }
  service wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE], en". }
}
order by ?uri
'''

r = requests.get(url, params = {'format': 'json', 'query': query})
data = r.json()

format_data = []

for r in data['results']['bindings']:
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
        for x in ['puid','extension','mimetype', 'offset', 'sig']:
            if x in r:
                item[x] = r[x]['value']
            else:
                item[x] = None
    
        #print(item)
        format_data.append(item);

with open('wikidata.json','w') as f:
    f.write(json.dumps(format_data, indent=2))

