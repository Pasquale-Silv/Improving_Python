# lstrip()
# rstrip()
# strip()

# Demonstrating the lstrip() method

print("[" + " tau ".lstrip() + "]")

# The one-parameter lstrip() method does the same as its parameterless version, but removes all characters enlisted in its argument (a string), not just whitespaces:

print("www.cisco.com".lstrip("w."))

print("pythoninstitute.org".lstrip(".org"))

# Demonstrating the rstrip() method
print("pythoninstitute.org".rstrip(".org"))
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))

# The trip() method combines the effects caused by rstrip() and lstrip()
# it makes a new string lacking all the leading and trailing whitespaces.
# Demonstrating the strip() method
print("[" + "   aleph   ".strip() + "]")
print("   dhdskhds    ".strip())
