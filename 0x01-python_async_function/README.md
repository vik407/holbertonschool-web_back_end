# 0x01. Python - Async

## Resources:books:
Read or watch:
* [Async IO in Python: A Complete Walkthrough](https://intranet.hbtn.io/rltoken/0FDY9iHLQ_UcSGoYLfv_tQ)
* [asyncio - Asynchronous I/O](https://intranet.hbtn.io/rltoken/mr49MheJNH97N-xHbDUk_w)
* [random.uniform](https://intranet.hbtn.io/rltoken/2d9o-mvWPygQ46-4snE99w)

---
## Learning Objectives:bulb:
What you should learn from this project:

* A README.md file, at the root of the folder of the project, is mandatory
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
* All your files should end with a new line
* All your files must be executable
* The length of your files will be tested using wc
* The first line of all your files should be exactly #!/usr/bin/env python3
* Your code should use the pycodestyle style (version 2.5.x)
* All your functions and coroutines must be type-annotated.
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'

---

### [0. The basics of async](./0-basic_async_syntax.py)
* Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.


### [1. Let's execute multiple coroutines at the same time with async](./1-concurrent_coroutines.py)
* Import wait_random from the previous python file that you’ve written and write an async routine called wait_n that takes in 2 int arguments: max_delay and n. You will spawn wait_random n times with the specified max_delay.


### [2. Measure the runtime](./2-measure_runtime.py)
* From the previous file, import wait_n into 2-measure_runtime.py.


### [3. Tasks](./3-tasks.py)
* Import wait_random from 0-basic_async_syntax.


### [4. Tasks](./4-tasks.py)
* Take the code from wait_n and alter it into a new function task_wait_n.  The code is nearly identical to wait_n except task_wait_random is being called.

---

## Author
* **Victor Hernandez** - [vik407](https://github.com/vik407)