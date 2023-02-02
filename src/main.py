import re
import os
os.chdir("/Users/antony.vargasulead.ac.cr/BigData/Clase2/")

file = open("data/data.txt", "r")
txt = file.read()

email_regex = r"\w+[.|]+\w+@\w+\.\w+"

def extract_email(text):
	return re.findall(email_regex, text)

emails = extract_email(text=txt)
print(emails)
print("\n" + str(len(emails)))
