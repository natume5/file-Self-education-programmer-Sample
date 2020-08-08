import re


l = "Beautiful is better than ugly."
matches = re.findall("Beautiful", l, re.IGNORECASE)


print(matches)
