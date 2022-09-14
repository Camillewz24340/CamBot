from termcolor import colored as color
from datetime import datetime


def Info(m:str):
    print(color(("[INFO] " + m), "white" ) + "  " + color(str(datetime.now()), "white"))
    
def Error(m:str):
    print(color(("[ERROR] " + m), "red" ) + "  " + color(str(datetime.now()), "white"))
    
def DuringOperation(m:str):
    print(color(("[...] " + m), "white" ) + "  " + color(str(datetime.now()), "white"))
    
def Success(m:str):
    print(color(("[SUCCESS] " + m), "green" ) + "  " + color(str(datetime.now()), "white"))
    
def Fatal(m:str):
    print(color(("[FATAL] " + m), "red" ) + "  " + color(str(datetime.now()), "white"))