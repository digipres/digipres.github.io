from __future__ import with_statement
from __future__ import print_function
import urllib

# Download Github Linguist language sigs:
url = "https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml"
urllib.urlretrieve(url,"languages.yml")
