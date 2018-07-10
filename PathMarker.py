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
            result=parse.matchLine(name)
            if result:
                path = parse.prependDir(result[0])
                count += 1
                sys.stdout.write("%d\t%s" % (count, name))
                f.write("%s\n" % path)
            else:
                sys.stdout.write("\t%s" % (name))
        f.close

    if sys.argv[1] == "get":
        theline=linecache.getline(PathMarker_buffer_file, int(sys.argv[3])).strip()
        sys.stdout.write("%s %s" % (sys.argv[2], theline))
        os.system("%s %s" % (sys.argv[2], theline))


