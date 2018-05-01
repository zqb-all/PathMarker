#!/usr/bin/env python

import sys
import os
import re
import linecache
from  PathPicker.src import parse

PathMarker_buffer_file = os.path.expanduser('~/.PathMarker')
open(PathMarker_buffer_file, 'a').close()

if __name__ == "__main__":
    if sys.argv[1] == "set":
        count = 0
        f = open(PathMarker_buffer_file,"w")
        for name in sys.stdin.readlines():
            count += 1
            sys.stdout.write("%d\t%s" % (count, name))
            result=parse.matchLine(name)
            if result:
                f.write("%s\n" % result[0])
            else:
                f.write("\n")
        f.close
    if sys.argv[1] == "get":
        theline=linecache.getline(PathMarker_buffer_file, int(sys.argv[2])).strip()
        sys.stdout.write("vim %s" % theline)
        os.system("vim %s" % theline)


