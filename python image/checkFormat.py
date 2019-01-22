import re

u_id = input("Input User ID: ") #DECLARE u_id : string

rex = re.compile("^[A-Z]{1}[a-z]{2}[0-9]{3}$")
if rex.match(u_id):
    print("Correct format")
else:
    print("Incorrect")