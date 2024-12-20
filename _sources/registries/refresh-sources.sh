#!/bin/sh
set -e

cd fdd
python download-fdd-data.py
cd -

cd pronom
python download-pronom-data.py
cd -

cd nara
python download-nara-data.py
cd -

cd tika
python download-tika-data.py
cd -

cd trid
python download-trid-data.py
cd -

cd githublinguist
python download-githublinguist-data.py
cd -

cd wikidata
python download-wikidata-formats.py
python download-wikidata-software.py
cd -

cd ../../..
python digipres.github.io/_sources/registries/mediawikis/scan-wikis.py
cd -

git commit -m "Refreshed the known format data sources." .
