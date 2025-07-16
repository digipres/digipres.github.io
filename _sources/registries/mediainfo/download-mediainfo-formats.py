import urllib.request
import json
import html
import re

src = "https://mediaarea.net/en/MediaInfo/Support/Formats"

# Being evil, and parsing HTML with a RegEx for now.
# I will answer only to Cthulhu
# https://stackoverflow.com/a/1732454/6689
fre = re.compile('^\s*(.*) \((.*)\)<br/>\s*$')

with open('mediainfo.jsonl','w') as f_out:
    with urllib.request.urlopen(src) as fp:
        for line in fp.readlines():
            line = line.decode('utf-8')
            line = html.unescape(line)
            m = fre.match(line)
            if m:
                format = {
                    "name": m.groups()[0],
                    "extensions": m.groups()[1].split('/')
                }
                f_out.write(json.dumps(format))
                f_out.write("\n")