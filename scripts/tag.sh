wd=$(pwd)
find $wd -name '*.h' > cscope.files
find $wd -name "*.cpp" >> cscope.files
find $wd -name "*.c" >>cscope.files
find $wd -name "*.py" >>cscope.files
cscope -Rbq
ctags -R
etags `cat cscope.files` #(Try catgs cscope.files if this doesn't work)
cscope -d
