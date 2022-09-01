from __future__ import with_statement
from __future__ import print_function
from urllib.request import urlretrieve

# Download Github Linguist language sigs:
url = "https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml"
urlretrieve(url,"languages.yml")
