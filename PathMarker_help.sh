#!/bin/bash -
#===============================================================================
#
#          FILE: PathMarker_help.sh
#
#         USAGE: ./PathMarker_help.sh
#
#   DESCRIPTION: 
#
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 2018年05月01日 16时15分46秒
#      REVISION:  ---
#===============================================================================

v()
{
	PathMarker.py get vim $@
}

t()
{
	git -c color.ui=always $@ | PathMarker.py set | less -r -X -F
}

mgit()
{
	git -c color.ui=always $@ | PathMarker.py set | less -r -X -F
}

gitmark()
{
	git -c color.ui=always $@ | PathMarker.py set | less -r -X -F
}
