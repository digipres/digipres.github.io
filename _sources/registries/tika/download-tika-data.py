from __future__ import with_statement
from __future__ import print_function
import urllib

# Download Tika XML sigs:
#url = "https://github.com/apache/tika/raw/trunk/tika-core/src/main/resources/org/apache/tika/mime/tika-mimetypes.xml"
url = "https://svn.apache.org/repos/asf/tika/trunk/tika-core/src/main/resources/org/apache/tika/mime/tika-mimetypes.xml"
urllib.urlretrieve(url,"tika-mimetypes.xml")


