import re

data = """
Mr. Anderson
Ms. Thareja
Mrs. Morris
Mr. Roy
Ms. Gandhi
Mrs. Modi
https://www.google.com
http://www.udemy.com
www.udacity.com
https://www.stackoverflow.com
http://www.djsce.ac.in
https://plus.google.com
rishit.grover@gmail.com
kapeesh.grover@yahoo.co.in
abhishek.shah@gmail.com
shahp98@gmail.com
demo_user@gmail.com
rolflmoa@yahoo.co.in
27777647
233*333*88
455-78-888
022-240-93836
02642*221*381
"""

names = re.findall(r'(?:Mr\.|Ms\.|Mrs\.)\s([A-Za-z]+)', data)
print("Names:", names)

websites = re.findall(r'https?://(www\.)?([A-Za-z0-9.-]+)', data)
print("Website Names:", [site[1] for site in websites])

emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', data)
print("Email IDs:", emails)

numbers = re.findall(r'\b(?:\d{3}[-.\*]?)?\d{3}[-.\*]?\d{2,4}\b', data)
print("Phone Numbers:", numbers)