"""
But sometimes you want to know more - for example, the name of the OS which hosts Python,
and some characteristics describing the hardware that hosts the OS.

There is a module providing some means to allow you to know where you are and what components work for you.
The module is named
platform
We'll show you some of the functions it provides to you.

The platform module lets you access the underlying platform's data, i.e.,
hardware, operating system, and interpreter version information.

There is a function that can show you all the underlying layers in one glance, named platform, too.
It just returns a string describing the environment; thus,
its output is rather addressed to humans than to automated processing (you'll see it soon).
This is how you can invoke it:
platform(aliased = False, terse = False)
"""

from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))

print(platform(0, 1))
