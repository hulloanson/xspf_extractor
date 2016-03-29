from os import path, chdir
from shutil import copy

from xml.dom.minidom import parse
import sys

# This script assume that if <location> tag contains relative path, such path
#  is relative to the xspf file

# Argument 1 as path to xspf file
xspf_path = path.expanduser(sys.argv[1])

# Argument 2 as destination directory
dst_dir = path.expanduser(sys.argv[2])

file = open(xspf_path, encoding='utf-8')

# Change working directory to the xspf file's parent directory
wdir = path.dirname(xspf_path)
if wdir != '':
    chdir(wdir)

# Get Document object from file
doc = parse(file)

# Extract <location> tag to a list and loop over it.
for track_location in doc.getElementsByTagName('location'):
    curr_track_path = track_location.firstChild.data

    curr_track_name = curr_track_path.split('/')[-1]

    try: # Copy file to destination directory
        copy(curr_track_path,
             path.join(dst_dir, curr_track_name))
    except FileNotFoundError:
        print("File not found.")

print("Done.")
