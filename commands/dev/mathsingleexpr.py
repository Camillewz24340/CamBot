import math
import re
from random import *
from utils import consoledebug_return as Debug
from math import *

class InfinityWarning(Warning):
    pass

def mathsingleexpr(expression, username):

    print(Debug.Info(username + " used math command, expression: " + expression))

    forbiddenWords = ["\"","'",'"',"exec","os","sys", "str", "exit", "eval", "__.+__", "print", "license", "input", "help", "chr", "quit", "breakpoint", "repr", "ascii", "bytes", "forbiddenWords"]

    print("    " + Debug.DuringOperation("Checking expression validity"))
    
    for i in range(len(forbiddenWords)):

        print("        " + Debug.DuringOperation("Checking word: " + forbiddenWords[i]))

        if re.search(forbiddenWords[i], expression, flags=re.S):
                print("        " + Debug.Error("Forbidden word detected: " + forbiddenWords[i] + "\n    Calculation cancelled."))
                return("A forbidden expression has been entered, please don't start destroying me .-.\nNote: `Strings are not allowed`")
    
    print("        " + Debug.Success("Valid expression !"))
    print("    " + Debug.DuringOperation("Calculating expression"))

    try:
        for n in re.finditer("\*\*\d+", expression):
            if int(re.search("\d+", n.group()).group()) > int(2000):
                raise OverflowError("Too large numbers, please use smaller ones")

        result = eval(expression)

        print("        " + Debug.Success("Calculated successfully ! Result: " + str(result)))

        if result == -inf or result == inf:
            raise InfinityWarning
             
        return result
    
    except Warning as w:
         
        if type(w) == InfinityWarning:
            return ("Warning: The result of your expression is positive or negative infinity\nToo large numbers may trigger this warning")
    
    except Exception as e:

        print("        " + Debug.Error("Error while calculating"))
        return ("An error has occured, please check your expression !\nError: `" + str(type(e)) + ": " + str(e) + "`")