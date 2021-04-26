import time

def callback_function(function):
    """
    @Parameter: function should be callable
    Function creates a callback after sleeping for 10 seconds.
    """

    time.sleep(10) # Sleeps 10 Seconds for effect.
    function() # This variable is callable because I sent in a function.

def f (): print("Hello World")

function = f # Pointer to function is name of function like C

callback_function(function) #Execution

def a(): print('a') # One Line Function Definition

def b(): print('b') # One Line Function Definition

def c(): print('c') # One Line Function Definition

def d(): print('d') # One Line Function Definition

function_list = [a, b, c, d]

for f in function_list:
  f()