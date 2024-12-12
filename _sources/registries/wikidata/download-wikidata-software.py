# 
import json
import requests
import re

# Set up the query:
url = 'https://query.wikidata.org/sparql'
# Queries to find software entries that read or write formats, based on advice from Kat Thornton.
query_r = '''
# Items in Wikidata and the formats they are connected to via P1072 'readable file format'
SELECT DISTINCT ?item ?itemLabel ?officialWebsite ?license ?licenseLabel ?format ?formatLabel
WHERE
{
  ?item wdt:P1072 ?format.
  OPTIONAL { ?item wdt:P856 ?officialWebsite . }
  OPTIONAL { ?item wdt:P275 ?license . }
  
  # Helps get the label in your language, if not, then default for all languages, then en language
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". }
}
'''

query_w = '''
# Items in Wikidata and the formats they are connected to via P1073 'writable file format'
SELECT DISTINCT ?item ?itemLabel ?officialWebsite ?license ?licenseLabel ?format ?formatLabel
WHERE
{
  ?item wdt:P1073 ?format.
  OPTIONAL { ?item wdt:P856 ?officialWebsite . }
  OPTIONAL { ?item wdt:P275 ?license . }
  
  # Helps get the label in your language, if not, then default for all languages, then en language
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". }
}
'''

def process_query(item_data, query):

  r = requests.get(url, params = {'format': 'json', 'query': query})
  data = r.json()

  for r in data['results']['bindings']:
        # Print a sample
        if len(item_data) == 0:
            print("Printing one record to show the general form:")
            print(r)
        #
        item = {
            'id': re.findall(r"Q\d+", r['item']['value'])[0],
            'source': r['item']['value'],
            'name': r['itemLabel']['value'],
        }
        for x in ['officialWebsite', 'license', 'licenseLabel', 'format', 'formatLabel']:
            if x in r:
                item[x] = r[x]['value']
            else:
                item[x] = None
    
        #print(item)
        item_data.append(item)

def download_entries(filename, query):
    item_data = []
    process_query(item_data, query)
    with open(filename,'w') as f:
      f.write(json.dumps(item_data, indent=2))

download_entries('wikidata-reads.json', query_r)
download_entries('wikidata-writes.json', query_w)
