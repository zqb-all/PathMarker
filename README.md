
# PathMarker

PathMarker is a simple command line tool that solves the perpetual
problem of selecting files out of bash output.

PathMarker is inspire by [guake terminal](https://github.com/Guake/guake),
base on [Facebook PathPicker](https://github.com/facebook/PathPicker.git).

It is easiest to understand by watching simple demos:

![image](https://github.com/zqb-all/PathMarker/blob/master/demo/demo1.gif)

## Examples
After installing PathMarker, using it is as easy as piping into `PathMarker set`.
It takes a wide variety of input -- try it with all the options below:

* `git status | PathMarker.py set`
* `hg status | PathMarker.py set`
* `git grep "FooBar" | PathMarker.py set`
* `grep -r "FooBar" . | PathMarker.py set`
* `git diff HEAD~1 --stat | PathMarker.py set`
* `find . -iname "*.js" | PathMarker.py set`
* `arc inlines | PathMarker.py set`

and anything else you can dream up!

Files in the output will marked by number.

After use `PathMarker.py set` to mark files. You can use files with `PathMarker.py get`.

Numbers follow `PathMarker.py get` will replace by files name marked by `PathMarker.py set`.

Try:
* `PathMarker.py get vim 1`
* `PathMarker.py get md5sum 1 2 3`

## Installing PathMarker

### Manual Installation

* `cd /usr/local/ # or wherever you install apps`
* `git clone https://github.com/zqb-all/PathMarker.git`
* `cd PathMarker/`
* `git submodule init`
* `git submodule update`

Here we make a symbolic link from the bash script in the repo
to `/usr/local/bin/` which is assumed to be in the current
`$PATH`

* `ln -s "$(pwd)/PathMarker.py" /usr/local/bin/PathMarker.py`
now PathMarker.py should work
* `git show | PathMarker.py set`
* `PathMarker.py get vim 1`

For easily to use PathMarker.py with git/vim, try source PathMarker_help.sh in .bashrc

* `echo "source $(pwd)/PathMarker_help.sh" >> ~/.bashrc`
* `source ~/.bashrc`

Now you can use `t` as `git`, `v` as `vim`, `fcd` as `cd`, `ffd` as `fd`, `ffind` as `find`
* `t show`
* `v 1`
* `ffd src`
* `ffind . -name src`
* `fcd 1`

Note:
If you don't have fd, ffd just same as ffind
If you don't like these command, just modify PathMarker_help.sh

## License
PathMarker is BSD-licensed.

