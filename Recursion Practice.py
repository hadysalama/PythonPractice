# Stack OverFlow in Python
def helloworld():
    print()
    "hello world"
    helloworld()


# helloworld()

# Recursively counts down
def countdown(num):
    if num != 0:
        print(num)
        num = num - 1
        countdown(num)


countdown(100)


# Recursively counts up
def countup(start, end):
    if start <= end:
        print(start)
        start = start + 1
        countup(start, end)


countup(0, 100)


# Checks if the string is a Palindrome Recursively
def ispalindrome(str):
    """
    :param str: string
    :return: str: string
    """
    val = False
    if len(str) <= 1:
        val = True
    else:
        if str[-1] == str[0]:
            a = str.replace(str[0], "")
            b = str.replace(str[-1], "")
            val = ispalindrome(b)
    return val


print()
print()
print(ispalindrome("shoohs"))
print()
print()


# String Reversal Recursively
def reverse(str):
    """
    :param str: string
    :return a: string
    """
    if len(str) == 0:
        a = ""
    else:
        a = str[-1] + reverse(str[:-1])
    return a


print(reverse("cat"))
