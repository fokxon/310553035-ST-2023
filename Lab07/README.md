# Lab07
## crash file
- file name: id:000000,sig:06,src:000000,op:flip1,pos:18
## commands
```
cd Lab07
export CC=${AFL folder}/afl-gcc
export AFL_USE_ASAN=1
export AFL_I_DONT_CARE_ABOUT_MISSING_CRASHES=1
export AFL_SKIP_CPUFREQ=1
make
mkdir in
mkdir out
cp test.bmp in
${AFL folder}/afl-fuzz -i in/ -o out/ -m none -- ./bmpgrayscale @@ a.bmp
```

## screenshot of AFL running
![](https://i.imgur.com/mAIi5F2.png)

## screenshot of crash detail
![](https://i.imgur.com/PP38zIW.png)
