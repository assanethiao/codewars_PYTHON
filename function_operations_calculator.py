"""
  Description:
  This time we want to write calculations using functions and get the results. Let's have a look at some examples:

  seven(times(five()));   //  must return 35
  four(plus(nine()));     //  must return 13
  eight(minus(three()));  //  must return 5
  six(dividedBy(two()));  //  must return 3
  Requirements:

  There must be a function for each number from 0 ("zero") to 9 ("nine")
  There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy
  Each calculation consist of exactly one operation and two numbers
  The most outer function represents the left operand, the most inner function represents the right operand
  Division should be integer division. For example, this should return 2, not 2.666666...:
  eight(dividedBy(three()));
"""

def zero(op=None):   return 0 if not op else op(0)
def one(op=None):    return 1 if not op else op(1)
def two(op=None):    return 2 if not op else op(2)
def three(op=None):  return 3 if not op else op(3)
def four(op=None):   return 4 if not op else op(4)
def five(op=None):   return 5 if not op else op(5)
def six(op=None):    return 6 if not op else op(6)
def seven(op=None):  return 7 if not op else op(7)
def eight(op=None):  return 8 if not op else op(8)
def nine(op=None):   return 9 if not op else op(9)

def plus(y):         return lambda x: x + y
def minus(y):        return lambda x: x - y
def times(y):        return lambda x: x * y
def divided_by(y):   return lambda x: x // y  # Division entière
