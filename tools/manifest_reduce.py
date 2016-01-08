#!/bin/env python3
#The goal of this script is to automatically reduce the default Android manifest to only include things we build based on previous build output

import sys
import re
import xml.etree.ElementTree as ET

if len (sys.argv) != 3:
    print ("Usage: manifest_reduce.py manifest.xml make_output")
    sys.exit(-1)

manifest = ET.parse(sys.argv[1])
manifest_root = manifest.getroot()
make_output = open(sys.argv[2])

makefiles=[]
for line in make_output.readlines():
    m = re.match("including ([^\s]*) ...", line)
    if (m):
        #convert ./device/asus to device/asus
        makefiles.append(m.group(1).strip("./"))


def contains_makefile(path):
    for m in makefiles:
        if m.startswith(path):
            return True
    return False

for p in manifest.getroot().findall("project"):
    path = p.attrib["path"]
    if "chromium" in path:
        continue

    if not contains_makefile(path):
        manifest_root.remove(p)

manifest.write("default_reduced.xml")