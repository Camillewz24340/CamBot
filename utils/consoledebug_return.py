from termcolor import colored as color
from datetime import datetime


def Info(m:str):
    return color(("[INFO] " + m), "white" ) + "  " + color(str(datetime.now()), "white")
    
def Error(m:str):
    return color(("[ERROR] " + m), "red" ) + "  " + color(str(datetime.now()), "white")
    
def DuringOperation(m:str):
    return color(("[...] " + m), "white" ) + "  " + color(str(datetime.now()), "white")
    
def Success(m:str):
    return color(("[SUCCESS] " + m), "green" ) + "  " + color(str(datetime.now()), "white")
    
def Fatal(m:str):
    return color(("[FATAL] " + m), "red" ) + "  " + color(str(datetime.now()), "white")

def Warn(m:str):
    print(color(("[WARN] " + m), "yellow" ) + "  " + color(str(datetime.now()), "white"))