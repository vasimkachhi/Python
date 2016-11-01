import re

str = "My name is vasim. My dob is 24-April 1990 ." \
     "My home towm is Karad. I am graduate in ComputerScience and Enginnering from Shivaji University. " \
     "I stay in Kondwa Pune and work as Python developer from 2015." \
     "My phone number is 9096720223 form 2009 "
str1 = "I live in Kondwa"

years = re.findall(' \d{4} ', str)
print(years)

dates = re.findall('(\d+\-\w+ \d+)', str)
print(dates)

graduation = re.match( r'(.*) graduate in (.*) .\s(\w+)', str, re.M|re.I)
print graduation.group(2)

profile = re.match( r'(.*) work as (.*) from (.*)', str, re.M|re.I)
print profile.group(2)

address = re.match( r'(.*) I stay in (.*) and (.*)', str, re.M|re.I)
print address.group(2)

print str1.index("Kondwa")
print [{r.start(): r.end()} for r in re.finditer("I stay in ", str)]
