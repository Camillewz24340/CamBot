import math
from datetime import datetime
import time
import re
from random import *
from utils import consoledebug_return as Debug
from math import *

def mathsingleexpr(expression, username):

    exit  = None
    license = None
    input = None
    help = None
    quit = None
    breakpoint = None
    repr = None
    locals = None

    Cam = {"name":"Camille", "age":None, "mom":"Someone", "dad":"Someone","discord":"@bluecamille", "discordId":660631616074547224}
    cam = Cam
    PI = pi
    pI = pi
    Pi = pi
    τ = tau
    π = pi

    try:
        for n in re.finditer("\*\*\d+", expression):
            if int(re.search("\d+", n.group()).group()) > int(2000):
                raise OverflowError("Too large numbers, please use smaller ones")

        result = eval(expression)

        # print("        " + Debug.Success("Calculated successfully ! Result: " + str(result)))

        if result == inf:
             result = "inf\n(positive infinity)"
        if result == -inf:
             result = "-inf\n(negative infinity)"
        if isnan(result):
            result = "nan\n(not a number)"

        print(result)
                
        return result
    
    except Exception as e:
        return ("An error has occured, please check your expression !\nError: `" + str(type(e)) + ": " + str(e) + "`")