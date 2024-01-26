#### Just for learning how to write and build a package

This is a simple example package. 

The author doesn't suggest anyone use it.





#### v0.1.16 exception


```

  Traceback (most recent call last):
    File "./0527_files.py", line 6, in <module>
      from dknovautils import *
    File "/home/dkadmin/.local/lib/python3.8/site-packages/dknovautils/__init__.py", line 12, in <module>
      from dknovautils.commons import *
    File "/home/dkadmin/.local/lib/python3.8/site-packages/dknovautils/commons.py", line 39, in <module>
      AT.never()
    File "/home/dkadmin/.local/lib/python3.8/site-packages/dknovautils/dkat.py", line 209, in never
      AT.assert_(False,  s if s is not None else 'should never come here')
    File "/home/dkadmin/.local/lib/python3.8/site-packages/dknovautils/dkat.py", line 348, in assert_
      dknovautils.commons.iprint_error(msg)
  AttributeError: partially initialized module 'dknovautils' has no attribute 'commons' (most likely due to a circular import)

```










