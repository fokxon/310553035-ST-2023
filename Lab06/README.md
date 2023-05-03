# Lab06
## experiment environment
- os: Ubuntu 20.04.5 LTS (GNU/Linux 5.15.0-56-generic x86_64)
- gcc: 9.4.0
- valgrind: 3.15.0

## Heap out-of-bounds read/write
```cpp
#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
    int *a = new int[3];
    int *b = new int[3];
	
    // heap out-of-bound write
    a[3] = 4;
    // heap out-of-bound read
    cout << a[4] << "\n";
}
```
- ASan report
```
==800026==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x60200000001c at pc 0x55c74ed7d337 bp 0x7ffdd44b7fa0 sp 0x7ffdd44b7f90
WRITE of size 4 at 0x60200000001c thread T0
    #0 0x55c74ed7d336 in main (/mnt/es/ness/fokxon/st/Lab06/a.out+0x3336)
    #1 0x7f243d1d1082 in __libc_start_main ../csu/libc-start.c:308
    #2 0x55c74ed7d20d in _start (/mnt/es/ness/fokxon/st/Lab06/a.out+0x320d)

0x60200000001c is located 0 bytes to the right of 12-byte region [0x602000000010,0x60200000001c)
allocated by thread T0 here:
    #0 0x7f243d82c787 in operator new[](unsigned long) ../../../../src/libsanitizer/asan/asan_new_delete.cc:107
    #1 0x55c74ed7d2e5 in main (/mnt/es/ness/fokxon/st/Lab06/a.out+0x32e5)
    #2 0x7f243d1d1082 in __libc_start_main ../csu/libc-start.c:308

SUMMARY: AddressSanitizer: heap-buffer-overflow (/mnt/es/ness/fokxon/st/Lab06/a.out+0x3336) in main
Shadow bytes around the buggy address:
  0x0c047fff7fb0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7ff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c047fff8000: fa fa 00[04]fa fa 00 04 fa fa fa fa fa fa fa fa
  0x0c047fff8010: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8020: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8030: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8040: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8050: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
```
- Valgrind report
```
==784720== Invalid write of size 4
==784720==    at 0x109200: main (in /mnt/es/ness/fokxon/st/Lab06/a.out)
==784720==  Address 0x4dd9c8c is 0 bytes after a block of size 12 alloc'd
==784720==    at 0x483C583: operator new[](unsigned long) (in /usr/lib/x86_64-linux-gnu/valgrind/vgpreload_memcheck-amd64-linux.so)
==784720==    by 0x1091E5: main (in /mnt/es/ness/fokxon/st/Lab06/a.out)
==784720== 
==784720== Invalid read of size 4
==784720==    at 0x10920E: main (in /mnt/es/ness/fokxon/st/Lab06/a.out)
==784720==  Address 0x4dd9c90 is 4 bytes after a block of size 12 alloc'd
==784720==    at 0x483C583: operator new[](unsigned long) (in /usr/lib/x86_64-linux-gnu/valgrind/vgpreload_memcheck-amd64-linux.so)
==784720==    by 0x1091E5: main (in /mnt/es/ness/fokxon/st/Lab06/a.out)
==784720== 
0
==784720== 
==784720== HEAP SUMMARY:
==784720==     in use at exit: 24 bytes in 2 blocks
==784720==   total heap usage: 4 allocs, 2 frees, 73,752 bytes allocated
==784720== 
==784720== LEAK SUMMARY:
==784720==    definitely lost: 24 bytes in 2 blocks
==784720==    indirectly lost: 0 bytes in 0 blocks
==784720==      possibly lost: 0 bytes in 0 blocks
==784720==    still reachable: 0 bytes in 0 blocks
==784720==         suppressed: 0 bytes in 0 blocks
==784720== Rerun with --leak-check=full to see details of leaked memory
==784720== 
==784720== For lists of detected and suppressed errors, rerun with: -s
==784720== ERROR SUMMARY: 2 errors from 2 contexts (suppressed: 0 from 0)
```

## Stack out-fo-bounds read/write
```cpp
#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
    int a[] = {2, 3, 4};
    int b[] = {5, 6, 7};

    // stack out-of-bound write
    a[3] = 4;
    // stack out-of-bound read
    cout << a[4] << "\n";
}
```
- ASan report
```
==800104==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7fffdec4462c at pc 0x561fce7d0497 bp 0x7fffdec445e0 sp 0x7fffdec445d0
WRITE of size 4 at 0x7fffdec4462c thread T0
    #0 0x561fce7d0496 in main (/mnt/es/ness/fokxon/st/Lab06/a.out+0x3496)
    #1 0x7f97fac6e082 in __libc_start_main ../csu/libc-start.c:308
    #2 0x561fce7d022d in _start (/mnt/es/ness/fokxon/st/Lab06/a.out+0x322d)

Address 0x7fffdec4462c is located in stack of thread T0 at offset 44 in frame
    #0 0x561fce7d02f8 in main (/mnt/es/ness/fokxon/st/Lab06/a.out+0x32f8)

  This frame has 2 object(s):
    [32, 44) 'a' (line 6) <== Memory access at offset 44 overflows this variable
    [64, 76) 'b' (line 7)
HINT: this may be a false positive if your program uses some custom stack unwind mechanism, swapcontext or vfork
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-buffer-overflow (/mnt/es/ness/fokxon/st/Lab06/a.out+0x3496) in main
Shadow bytes around the buggy address:
  0x10007bd80870: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10007bd80880: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10007bd80890: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10007bd808a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10007bd808b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x10007bd808c0: f1 f1 f1 f1 00[04]f2 f2 00 04 f3 f3 00 00 00 00
  0x10007bd808d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10007bd808e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10007bd808f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10007bd80900: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10007bd80910: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
```
- Valgrind report
```
==800166== HEAP SUMMARY:
==800166==     in use at exit: 0 bytes in 0 blocks
==800166==   total heap usage: 2 allocs, 2 frees, 73,728 bytes allocated
==800166== 
==800166== All heap blocks were freed -- no leaks are possible
==800166== 
==800166== For lists of detected and suppressed errors, rerun with: -s
==800166== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
```

## Global out-of-bounds read/write
```cpp
#include <bits/stdc++.h>
using namespace std;

int a[] = {2, 3, 4};
int b[] = {5, 6, 7};
int main(int argc, char const *argv[])
{
    // global out-of-bound write
    a[3] = 4;
    // global out-of-bound read
    cout << a[4] << "\n";
}
```
- ASan report
```
==836113==ERROR: AddressSanitizer: global-buffer-overflow on address 0x557a7449b02c at pc 0x557a744972f6 bp 0x7ffda80d2250 sp 0x7ffda80d2240
WRITE of size 4 at 0x557a7449b02c thread T0
    #0 0x557a744972f5 in main (/mnt/es/ness/fokxon/st/Lab06/a.out+0x32f5)
    #1 0x7f5482bad082 in __libc_start_main ../csu/libc-start.c:308
    #2 0x557a744971ed in _start (/mnt/es/ness/fokxon/st/Lab06/a.out+0x31ed)

0x557a7449b02c is located 0 bytes to the right of global variable 'a' defined in 'global_oof.cpp:4:5' (0x557a7449b020) of size 12
0x557a7449b02c is located 52 bytes to the left of global variable 'b' defined in 'global_oof.cpp:5:5' (0x557a7449b060) of size 12
SUMMARY: AddressSanitizer: global-buffer-overflow (/mnt/es/ness/fokxon/st/Lab06/a.out+0x32f5) in main
Shadow bytes around the buggy address:
  0x0aafce88b5b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0aafce88b5c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0aafce88b5d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0aafce88b5e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0aafce88b5f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0aafce88b600: 00 00 00 00 00[04]f9 f9 f9 f9 f9 f9 00 04 f9 f9
  0x0aafce88b610: f9 f9 f9 f9 00 00 00 00 00 00 00 00 00 00 00 00
  0x0aafce88b620: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0aafce88b630: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0aafce88b640: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0aafce88b650: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
```
- Valgrind report
```
==835548== HEAP SUMMARY:
==835548==     in use at exit: 0 bytes in 0 blocks
==835548==   total heap usage: 2 allocs, 2 frees, 73,728 bytes allocated
==835548== 
==835548== All heap blocks were freed -- no leaks are possible
==835548== 
==835548== For lists of detected and suppressed errors, rerun with: -s
==835548== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
```

## Use-after-free 
```cpp
#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
    int *a = new int(3);
    delete a;
    // use-after-free
    cout << *a << "\n";
}
```
- ASan report
```
==837432==ERROR: AddressSanitizer: heap-use-after-free on address 0x602000000010 at pc 0x559a09ffb394 bp 0x7fff418b1180 sp 0x7fff418b1170
READ of size 4 at 0x602000000010 thread T0
    #0 0x559a09ffb393 in main (/mnt/es/ness/fokxon/st/Lab06/a.out+0x3393)
    #1 0x7f3eb18e6082 in __libc_start_main ../csu/libc-start.c:308
    #2 0x559a09ffb22d in _start (/mnt/es/ness/fokxon/st/Lab06/a.out+0x322d)

0x602000000010 is located 0 bytes inside of 4-byte region [0x602000000010,0x602000000014)
freed by thread T0 here:
    #0 0x7f3eb1f42c65 in operator delete(void*, unsigned long) ../../../../src/libsanitizer/asan/asan_new_delete.cc:177
    #1 0x559a09ffb35c in main (/mnt/es/ness/fokxon/st/Lab06/a.out+0x335c)
    #2 0x7f3eb18e6082 in __libc_start_main ../csu/libc-start.c:308

previously allocated by thread T0 here:
    #0 0x7f3eb1f41587 in operator new(unsigned long) ../../../../src/libsanitizer/asan/asan_new_delete.cc:104
    #1 0x559a09ffb305 in main (/mnt/es/ness/fokxon/st/Lab06/a.out+0x3305)
    #2 0x7f3eb18e6082 in __libc_start_main ../csu/libc-start.c:308

SUMMARY: AddressSanitizer: heap-use-after-free (/mnt/es/ness/fokxon/st/Lab06/a.out+0x3393) in main
Shadow bytes around the buggy address:
  0x0c047fff7fb0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7ff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c047fff8000: fa fa[fd]fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8010: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8020: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8030: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8040: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8050: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
```
- Valgrind report
```
==836636== Invalid read of size 4
==836636==    at 0x10922A: main (in /mnt/es/ness/fokxon/st/Lab06/a.out)
==836636==  Address 0x4dd9c80 is 0 bytes inside a block of size 4 free'd
==836636==    at 0x483D1CF: operator delete(void*, unsigned long) (in /usr/lib/x86_64-linux-gnu/valgrind/vgpreload_memcheck-amd64-linux.so)
==836636==    by 0x109225: main (in /mnt/es/ness/fokxon/st/Lab06/a.out)
==836636==  Block was alloc'd at
==836636==    at 0x483BE63: operator new(unsigned long) (in /usr/lib/x86_64-linux-gnu/valgrind/vgpreload_memcheck-amd64-linux.so)
==836636==    by 0x109205: main (in /mnt/es/ness/fokxon/st/Lab06/a.out)
==836636== 
3
==836636== 
==836636== HEAP SUMMARY:
==836636==     in use at exit: 0 bytes in 0 blocks
==836636==   total heap usage: 3 allocs, 3 frees, 73,732 bytes allocated
==836636== 
==836636== All heap blocks were freed -- no leaks are possible
==836636== 
==836636== For lists of detected and suppressed errors, rerun with: -s
==836636== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
```

## Use-after-return
```cpp
#include <bits/stdc++.h>
using namespace std;

int *a;
void foo()
{
    int b = 3;
    a = &b;
}
int main(int argc, char const *argv[])
{
    foo();
    // use-after-return
    cout << *a << "\n";
}
```
-  ASan report
```
3
```
(no report)
- Valgrind report
```
==838874== Conditional jump or move depends on uninitialised value(s)
==838874==    at 0x497B4B0: std::ostreambuf_iterator<char, std::char_traits<char> > std::num_put<char, std::ostreambuf_iterator<char, std::char_traits<char> > >::_M_insert_int<long>(std::ostreambuf_iterator<char, std::char_traits<char> >, std::ios_base&, char, long) const (in /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.29)
==838874==    by 0x4988CAB: std::ostream& std::ostream::_M_insert<long>(long) (in /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.29)
==838874==    by 0x10923B: main (in /mnt/es/ness/fokxon/st/Lab06/a.out)
==838874== 
==838874== Use of uninitialised value of size 8
==838874==    at 0x497B1EB: int std::__int_to_char<char, unsigned long>(char*, unsigned long, char const*, std::_Ios_Fmtflags, bool) (in /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.29)
==838874==    by 0x497B4DA: std::ostreambuf_iterator<char, std::char_traits<char> > std::num_put<char, std::ostreambuf_iterator<char, std::char_traits<char> > >::_M_insert_int<long>(std::ostreambuf_iterator<char, std::char_traits<char> >, std::ios_base&, char, long) const (in /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.29)
==838874==    by 0x4988CAB: std::ostream& std::ostream::_M_insert<long>(long) (in /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.29)
==838874==    by 0x10923B: main (in /mnt/es/ness/fokxon/st/Lab06/a.out)
==838874== 
==838874== Conditional jump or move depends on uninitialised value(s)
==838874==    at 0x497B1FD: int std::__int_to_char<char, unsigned long>(char*, unsigned long, char const*, std::_Ios_Fmtflags, bool) (in /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.29)
==838874==    by 0x497B4DA: std::ostreambuf_iterator<char, std::char_traits<char> > std::num_put<char, std::ostreambuf_iterator<char, std::char_traits<char> > >::_M_insert_int<long>(std::ostreambuf_iterator<char, std::char_traits<char> >, std::ios_base&, char, long) const (in /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.29)
==838874==    by 0x4988CAB: std::ostream& std::ostream::_M_insert<long>(long) (in /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.29)
==838874==    by 0x10923B: main (in /mnt/es/ness/fokxon/st/Lab06/a.out)
==838874== 
==838874== Conditional jump or move depends on uninitialised value(s)
==838874==    at 0x497B50F: std::ostreambuf_iterator<char, std::char_traits<char> > std::num_put<char, std::ostreambuf_iterator<char, std::char_traits<char> > >::_M_insert_int<long>(std::ostreambuf_iterator<char, std::char_traits<char> >, std::ios_base&, char, long) const (in /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.29)
==838874==    by 0x4988CAB: std::ostream& std::ostream::_M_insert<long>(long) (in /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.29)
==838874==    by 0x10923B: main (in /mnt/es/ness/fokxon/st/Lab06/a.out)
==838874== 
3
==838874== 
==838874== HEAP SUMMARY:
==838874==     in use at exit: 0 bytes in 0 blocks
==838874==   total heap usage: 2 allocs, 2 frees, 73,728 bytes allocated
==838874== 
==838874== All heap blocks were freed -- no leaks are possible
==838874== 
==838874== Use --track-origins=yes to see where uninitialised values come from
==838874== For lists of detected and suppressed errors, rerun with: -s
==838874== ERROR SUMMARY: 4 errors from 4 contexts (suppressed: 0 from 0)
```

## ASan skipping
```cpp
#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	int a[8] = {1, 1, 1, 1, 1, 1, 1, 1};
	int b[8] = {2, 2, 2, 2, 2, 2, 2, 2};

	a[16] = 3;
	cout << b[0] << "\n";
}
```
- ASan report
```
3
```
(no report)

## TL;DR


| | Valgrind | ASan |
| -------- | -------- | -------- |
| Heap out-of-bounds | :white_check_mark: | :white_check_mark: |
| Stack out-of-bounds | :x: | :white_check_mark: |
| Global out-of-bounds | :x: | :white_check_mark: |
| Use-after-free | :white_check_mark: | :white_check_mark: |
| Use-after-return | :white_check_mark: | :x: |
