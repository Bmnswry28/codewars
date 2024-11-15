# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132
import re
def validate_pin(pin):
    if re.fullmatch("\d{4}|\d{6}", pin):
        return True
    else:
        return False