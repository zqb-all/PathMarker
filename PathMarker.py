#!/usr/bin/env python

import sys
import os
import re
import linecache
from  PathPicker.src import parse
from  PathPicker.src.formattedText import FormattedText

PathMarker_buffer_file = os.path.expanduser('~/.PathMarker')
open(PathMarker_buffer_file, 'a').close()
theline = ""

if __name__ == "__main__":
    if sys.argv[1] == "set":
        count = 0
        f = open(PathMarker_buffer_file,"w")
        for name in sys.stdin.readlines():
            formattedLine = FormattedText(name)
            result=parse.matchLine(str(formattedLine))
            if result:
                path = parse.prependDir(result[0], withFileInspection=True)
                count += 1
                sys.stdout.write("%d\t%s" % (count, name))
                f.write("%s\n" % path)
            else:
                sys.stdout.write("\t%s" % (name))
        f.close

    if sys.argv[1] == "get":
        for i in range(2, len(sys.argv)):
            if sys.argv[i].isdigit():
                theline += ' '
                theline += linecache.getline(PathMarker_buffer_file, int(sys.argv[i])).strip()
            else:
                theline += ' '
                theline += sys.argv[i]
        sys.stdout.write("%s\n" % theline)
        os.system("%s" % theline)

    if sys.argv[1] == "fix":
        for i in range(2, len(sys.argv)):
            if sys.argv[i].isdigit():
                theline += ' '
                theline += linecache.getline(PathMarker_buffer_file, int(sys.argv[i])).strip()
            else:
                theline += ' '
                theline += sys.argv[i]
        sys.stdout.write("%s" % theline)
        os.system("echo %s" % theline)


