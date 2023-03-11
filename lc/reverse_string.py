strng = "Hello world"

# reverse with first letter capitalized
print(strng[::-1].capitalize())

# reverse with all letters capitalized
print(strng[::-1].upper())

# reverse with all letters lowercased
print(strng[::-1].lower())

# reverse with all letters capitalized except the first letter
print(strng[::-1].capitalize()[0:-1] + strng[::-1].capitalize()[-1].lower())
