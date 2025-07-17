from urllib.request import urlretrieve
import zipfile
import io
import re

#
# This basic parser grabs the sets of file extenions but does not properly parse the magic test tree, so misses a lot.
#

# Download file source package:
url = "https://github.com/file/file/archive/refs/heads/master.zip"
file = "file.zip"
urlretrieve(url,file)

# Regexes
empty = re.compile("^\s*$")
ext = re.compile("^!:ext\s+(.*)$")
mime = re.compile("^!:mime\s+(.*)$")

# Status: have we started a signature record:
in_sig = False

# Loop through the zip, find the Magic files...
with zipfile.ZipFile(file, "r") as f:
    for name in f.namelist():
        if name.startswith("file-master/magic/Magdir"):
            #print(name)
            fmt = None
            with f.open(name) as entry:
                for line in io.TextIOWrapper(entry):
                    # empty:
                    if empty.match(line):
                        pass
                    # hash-line
                    elif line.startswith("#"):
                        pass
                        #comment = fmt.get('comment', "")
                        #comment += line
                        #fmt['comment'] = comment
                    # metadata-line
                    elif line.startswith("!"):
                        # Extract extensions:
                        em = ext.match(line)
                        if em:
                            exts = fmt.get('extensions', [])
                            exts = list(set(exts + list(filter(None, em.groups()[0].split('/')))))
                            fmt['extensions'] = exts
                        # Extract content-types:
                        mm = mime.match(line)
                        if mm:
                            mimes = fmt.get('types', [])
                            mimes = list(set(mimes + [ mm.groups()[0] ] ))
                            fmt['types'] = mimes
                    # signature line:
                    else:
                        # These lines are whitespace separated:
                        sm = re.split(r'(?<!\\)\s+', line.strip(), maxsplit=3)
                        #UGH need to split on un-escaped whitespace. ie. don't split on "\ "
                        # Binary signatures start with an un-nested number for a match position:
                        if not line.startswith('>'):
                            # output and reset
                            if fmt and 'name' in fmt:
                                print(fmt)
                            fmt = { 'source': name }

                        # We should take the name from the first line that has a name in the right spot
                        if len(sm) == 4:
                            last = sm[3]
                            if last and not 'name' in fmt:
                                fmt['name'] = last
            # EOF so print last entry:
            if fmt:
                print(fmt)


