#!/bin/bash -

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

ffd()
{
	type fd > /dev/null 2>&1 && {
		fd $@ | PathMarker.py set
		return
	}
	find $@ | PathMarker.py set
}

ffind()
{
	find $@ | PathMarker.py set
}

fcd()
{
	cd `PathMarker.py fix $@`
}
