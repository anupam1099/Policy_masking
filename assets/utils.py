import sys
import re


# start exection
def startExecution():
    print("\n ----- Policy Pdf Engine & Chassis Number Mask Checker Started -----\n")


# stop exection
def stopExecution():
    print("\n---- Execution Stopped! ----\n")
    sys.exit(0)


# regex matcher
def use_regex(input_text, regex):
    return re.match(regex, input_text)


# print error
def printError(e):
    print("--> ERROR : \n-->", e)
