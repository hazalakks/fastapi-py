"""
String Formatting
"""


first_name = "Eric"

sentence = "Hi {} {}"
last_name = "Roby"
print(sentence.format(first_name, last_name))

print(f"Hi {first_name} {last_name} I hope you are learning")

"""
User Input
"""

first_name = input("Enter your first name: ")
days = input("How many days before your birthday: ")
print(f"Hi {first_name}, only {days} days "
      f"before your birthday!")