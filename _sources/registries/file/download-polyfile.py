import json
#import pathlib
from polyfile.magic import MagicMatcher, MagicTest

#
# This code needs polyfile to be added as a runtime dependency, but can parse the file magic test tree
# This works for v0.5.5 of polyfile, dated March 2025, but the embedded version of the file magic definitions appears to be at least two years older than that.
#
# However, polyfile does not support regex/31/s and perhaps other recent syntax, so can't be used to track changes to the current file magic.
# 

#files = [f for f in pathlib.Path().glob("./file-master/magic/Magdir/*")]

magic_matcher: MagicMatcher = MagicMatcher.DEFAULT_INSTANCE #.parse(*files)

def name_of(mt):
    mt_str = str(mt.message)
    mt_str = mt_str.replace("\t", " ")
    mt_str = mt_str.replace("\x08", " ")
    return mt_str.strip()

def get_full_name(mt: MagicTest):
    name = name_of(mt)
    for amt in mt.ancestors():
        name = name_of(amt) + name
    return name

def to_fmt(mt: MagicTest):
    # Record the full name:
    fmt = {
        'name': get_full_name(mt)
    }

    # Add source, if any:
    si = mt.source_info
    if si:
        fmt['source'] = f"{si.path.name}#L{si.line}"
    
    # Add content types, if any:
    content_types = list(mt.mimetypes())
    if len(content_types) > 0:
        fmt['types'] = content_types

    # Add extensions, if any:
    extensions = list(mt.extensions)
    if len(extensions) > 0:
        fmt['extensions'] = extensions

    return fmt

def scan_magic(magic_tests):
    for mt in magic_matcher:
        yield to_fmt(mt)
        for smt in mt.descendants():
            yield to_fmt(smt)


# Output all the possible test results, skipping those with identical outcomes
last_mt = None
for mt in scan_magic(magic_matcher):
    if last_mt != mt:
        print(json.dumps(mt))
    last_mt = mt
