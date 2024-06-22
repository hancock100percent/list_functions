# enter a list ie.. mountains, rivers, countries, cities, languages, etc...
# create the list and use each function you know at least once
# guest list 

# letters to words Dictionary
letters_to_words = {
    'a': "Alpha", 'b': "Bravo", 'c': "Charlie", 'd': "Delta",
    'e': "Echo", 'f': "Foxtrot", 'g': "Golf", 'h': "Hotel",
    'i': "India", 'j': "Juliet", 'k': "Kilo", 'l': "Lima",
    'm': "Mike", 'n': "November", 'o': "Oscar", 'p': "Papa",
    'q': "Quebec", 'r': "Romeo", 's': "Sierra", 't': "Tango",
    'u': "Uniform", 'v': "Victor", 'w': "Whiskey", 'x': "X-Ray",
    'y': "Yankee", 'z': "Zulu"
}


# change letters to words Dictionary mapping
letters_to_words['z'] = "Zebra"
letters_to_words['b'] = "Brett"

# email_providers list
email_providers = [
    "Gmail (Google)",
    "Outlook.com (Microsoft)",
    "Yahoo Mail",
    "iCloud Mail (Apple)",
    "AOL Mail",
    "ProtonMail",
    "Zoho Mail",
    "Mail.com",
    "GMX Mail",
    "Yandex Mail"
]

# insert into email_providers list
email_providers.insert(2, 'Hotmail')
email_providers.insert(2, 'temp mail')


print(f"\n\t{len(email_providers)} email_providers list") 
print(email_providers)
# print(f"\{len(email_providers)} email_providers list") 


# great message list
great_message = [
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The best way to predict the future is to create it. - Abraham Lincoln",
    "In the middle of difficulty lies opportunity. - Albert Einstein",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "Nothing is impossible, the word itself says 'I'm possible'! - Audrey Hepburn",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll"
]

#letter mapping dictionary
# Example of using letters instead of numbers
# Replace numbers with letters as per your requirement
letter_mapping = {
    'a': email_providers[0],
    'b': email_providers[1],
    'c': email_providers[2],
    'd': email_providers[3],
    'e': email_providers[4],
    'f': email_providers[5],
    'g': email_providers[6],
    'h': email_providers[7],
    'i': email_providers[8],
    'j': email_providers[9]
}

# map2 dictionary
# Example of using letters instead of numbers
# Replace numbers with letters as per your requirement
map2 = {
    'a': great_message[0],
    'b': great_message[1],
    'c': great_message[2],
    'd': great_message[3],
    'e': great_message[4],
    'f': great_message[5],
    'g': great_message[6],
    'h': great_message[7],
    'i': great_message[8],
    'j': great_message[9]
}    

#guests list
guests = []
guests.append(letters_to_words['a'])
guests.append(letter_mapping['b'])
guests.append(letters_to_words['c'])
guests.append(letters_to_words['d'])
guests.append(letters_to_words['e'])
guests.append(letters_to_words['f'])
guests.append(letter_mapping['g'])
guests.append(letter_mapping['h'])
guests.append(letter_mapping['i'])
guests.append(letter_mapping['j'])

guests.insert(3, letter_mapping['f'])

del(guests[0])

# print len guests list
print(guests)
# print(f"\{len(guests)} guests list attending") 
# print(f"\n\t{len(guests)} guests attending") 

# messages list
messages = []
messages.append(map2['a'])
messages.append(map2['b'])
messages.append(map2['c'])
messages.append(map2['d'])
messages.append(map2['e'])
messages.append(map2['f'])
messages.append(map2['g'])
messages.append(map2['h'])
messages.insert(2, letters_to_words['y'])

# Print guests, len, and message
# Print number of guests and describe
# print(f"\n\t{len(guests)} Invitations") 
# print(guests)
print(f"\n\t{len(guests)} guests attending") 
print(guests)

del(guests[0])

# print(guests)
print(f"\n\t{len(guests)} resorted guests attending") 

# Creating a list of numbers
# guests = [10, 5, 8, 3, 1, 7]

# Using sorted() to create a new sorted list
sorted_guests = sorted(guests)
print("Sorted numbers using sorted():", sorted_guests)

# Print the original list order
print("original numbers using .sort():", guests)

# Using .sort() to sort the list in place
guests.sort()
print("Sorted numbers using .sort():", guests)

# Using sorted() with reverse=True to create a new sorted list in descending order
reverse_sorted_guests = sorted(guests, reverse=True)
print("Reverse sorted numbers using sorted(reverse=True):", reverse_sorted_guests)


# print(guests)
print(f"\n\t{len(guests)} guests attending") 


# print(guests)
msg = f"{guests[0].title()}"
print(msg)
msg = f"{guests[1].title()}"
print(msg)
msg = f"{guests[2].title()}"
print(msg)
msg = f"{guests[3].title()}"
print(msg)
msg = f"{guests[4].title()}"
print(msg)
msg = f"{guests[5].title()}"
print(msg)
msg = f"{guests[6].title()}"
print(msg)
msg = f"{guests[7].title()}"
print(msg)
msg = f"{guests[8].title()}"
print(msg)


# print message to new guest list
# Print number of guests and describe
print(f"\n\t{len(guests)} Invitations with messages") 
msg = f"Hello, {guests[0].title()},  {messages[0]}!"
print(msg)
msg = f"Hello, {guests[1].title()},  {messages[1]}!"
print(msg)
msg = f"Hello, {guests[2].title()},  {messages[2]}!"
print(msg)
msg = f"Hello, {guests[3].title()},  {messages[3]}!"
print(msg)
msg = f"Hello, {guests[4].title()},  {messages[4]}!"
print(msg)
msg = f"Hello, {guests[5].title()},  {messages[4]}!"
print(msg)
msg = f"Hello, {guests[6].title()},  {messages[3]}!"
print(msg)
msg = f"Hello, {guests[7].title()},  {messages[2]}!"
print(msg)
msg = f"Hello, {guests[8].title()},  {messages[1]}!"
print(msg)

# send message one at a time
print("\n\tdeclined")
removed_language = guests.pop()
print(removed_language,"is uninvited")
removed_language = guests.pop()
print(removed_language,"is uninvited")

# Print number of guests and describe
print(f"\n\t{len(guests)} Invitations") 

msg = f"Hello, {guests[0].title()},  {messages[1]}!"
print(msg)
msg = f"Hello, {guests[1].title()},  {messages[2]}!"
print(msg)
msg = f"Hello, {guests[2].title()},  {messages[3]}!"
print(msg)
msg = f"Hello, {guests[3].title()},  {messages[4]}!"
print(msg)
msg = f"Hello, {guests[4].title()},  {messages[3]}!"
print(msg)
msg = f"Hello, {guests[5].title()},  {messages[2]}!"
print(msg)
msg = f"Hello, {guests[6].title()},  {messages[1]}!"
print(msg)


"""
# list of lists
# list of dictionaries
# append, change, insert
# msg = f"Hello, {guests[3].title()},  {messages[3]}!"
# print(msg)
# msg = f"Hello, {guests[4].title()},  {messages[3]}!"
# print(msg)

# Print number of messages
# print(f"\n\t{len(messages)} messages") 
# print(messages)
# Example usage
"""
