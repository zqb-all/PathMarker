# PathMarker

PathMarker is a simple command line tool that solves the perpetual
problem of selecting files out of bash output.

PathMarker is inspire by [guake terminal](https://github.com/Guake/guake)
base on [Facebook PathPicker](https://github.com/facebook/PathPicker.git)

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

After use PathMarker.py set to mark files.You can use files with `PathMarker.py get`.
numbers follow the `PathMarker.py get` will replace by files name mark by `PathMarker.py set`.
try it
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

for easily to use PathMarker.py with git/vim
try source PathMarker_help.sh in .bashrc
* `echo "source $(pwd)/PathMarker_help.sh" >> ~/.bashrc`
* `source ~/.bashrc`
now you can use `t` as `git`, `v` as `vim`
* `t show`
* `v 1`
if you don't like command `v` and `t`, just modify PathMarker_help.sh

## License
PathMarker is BSD-licensed.
