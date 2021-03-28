print()
print()

# String replace returns a new string
a = "Hello, World!"
print("a = ", a)
print("Length: ", len(a))
b = a.replace(a[0], "")
print("b = ", b)
print("Length: ", len(b))

print()
print()

# Index -1 is the last element of the string. Same as a.length()-1
print(a[-1])

# Slicing : acts as a without so this returns the string a without the last element
print(a[:-1])

# Prints Hel
print(a[0:3])

print(a[:1])
