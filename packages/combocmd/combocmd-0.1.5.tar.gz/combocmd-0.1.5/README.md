**Install**
```
pip install combocmd
```

**Examples**

```
combocmd --strings hello world
hello,hello;hello,world;world,world

combocmd --strings hello world --ABfmt "{A} {B}" --PsepP ", "
hello hello, hello world, world world
```

```
combocmd --strings hello world --cmdABBA "echo {A} {B}"
world world
world hello
hello world
hello hello
```

```
combocmd --strings 1 2 --cmdAB "echo cmdAB x={A} y={B}" --cmdBA "echo cmdBA x={A} y={B}" --AisB cmdAB
cmdAB x=1 y=1
cmdAB x=1 y=2
cmdBA x=2 y=1
cmdAB x=2 y=2
```

```
combocmd --strings 1 2 --cmdABBA "echo {A}{A}{A}{B}{B}{B}"
111111
222111
111222
222222
```

```
mkdir -p demo; combocmd --strings 1 2 --cmdABBA "echo '{A}{B}' > demo/{A}{B}"; combocmd --strings demo/* --cmdABBA "echo {A} {B}"
demo/21 demo/21
demo/22 demo/21
demo/22 demo/12
demo/12 demo/21
demo/11 demo/22
demo/22 demo/22
demo/11 demo/12
demo/21 demo/11
demo/22 demo/11
demo/12 demo/12
demo/12 demo/22
demo/21 demo/12
demo/21 demo/22
demo/11 demo/11
demo/11 demo/21
demo/12 demo/11
```

```
combocmd --strings 1 2 --cmdAB "echo '{wcA}{wcB}'" --cmdBA "echo '{wcA}{wcB}'" --A {wcA} --B {wcB}
12
11
22
21
combocmd --strings 1 2 --cmdAB "echo '{A}{B}'" --cmdBA "echo '{A}{B}'" --runRepeats
11
11
12
21
22
22
```
