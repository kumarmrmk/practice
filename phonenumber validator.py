# validating phone nnumber
import re
def phonenumvalidation(phn):
    pattern = "^[6-9][0-9]{9}$"
    if re.match(pattern,phn):
        print("valid")
    else:
        print("Invalid")
phn=input()
phonenumvalidation(phn)
