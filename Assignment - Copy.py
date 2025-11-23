Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
guests=['Quinta','Keren','Grace']
print(guests[0])
Quinta
print(guests[1])
Keren
print(guests[2])
Grace
print(guests[0],'I am inviting you to have dinner with friends and i')
Quinta I am inviting you to have dinner with friends and i
print(guests[1],'I am inviting you to have dinner with friends and i')
Keren I am inviting you to have dinner with friends and i
print(guests[2],'I am inviting you to have dinner with friends and i')
Grace I am inviting you to have dinner with friends and i
print(guests[2],'Called saying that she would not make it for dinner')
Grace Called saying that she would not make it for dinner
guests[2]='Emmy'
print(guests)
['Quinta', 'Keren', 'Emmy']
print(guests[0],'I am inviting you to have dinner with friends and i')
Quinta I am inviting you to have dinner with friends and i
print(guests[1],'I am inviting you to have dinner with friends and i')
Keren I am inviting you to have dinner with friends and i
print(guests[2],'I am inviting you to have dinner with friends and i')
Emmy I am inviting you to have dinner with friends and i

guests.insert(3,'Kate')
print(guests)
['Quinta', 'Keren', 'Emmy', 'Kate']
guests.insert(4,'Tina')
print(guests)
['Quinta', 'Keren', 'Emmy', 'Kate', 'Tina']
guests.append('Princess')
print(guests)
['Quinta', 'Keren', 'Emmy', 'Kate', 'Tina', 'Princess']
print(guests[0],guests[1],guests[2],'Great news guys a bigger table has been found')
Quinta Keren Emmy Great news guys a bigger table has been found
print(guests[0],'I am inviting you to have dinner with friends and i')
Quinta I am inviting you to have dinner with friends and i
print(guests[1],'I am inviting you to have dinner with friends and i')
Keren I am inviting you to have dinner with friends and i
print(guests[2],'I am inviting you to have dinner with friends and i')
Emmy I am inviting you to have dinner with friends and i
print(guests[3],'I am inviting you to have dinner with friends and i')
Kate I am inviting you to have dinner with friends and i
print(guests[4],'I am inviting you to have dinner with friends and i')
Tina I am inviting you to have dinner with friends and i
>>> print(guests[5],'I am inviting you to have dinner with friends and i')
Princess I am inviting you to have dinner with friends and i
>>> 
>>> print(guests[2],guests[3],guests[4],guests[5],'Sorry guys but dinner has been cancelled for now due to inconvienences')
Emmy Kate Tina Princess Sorry guys but dinner has been cancelled for now due to inconvienences
>>> guests.pop(2)
'Emmy'
>>> guests.pop(3)
'Tina'
>>> guests.pop(4)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    guests.pop(4)
IndexError: pop index out of range
>>> print(guests[0],'You are still invited for dinner')
Quinta You are still invited for dinner
>>> print(guests[1],'You are still invited for dinner')
Keren You are still invited for dinner
>>> guests.pop(4)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    guests.pop(4)
IndexError: pop index out of range
>>> #removing guests
>>> guests.remove('Kate')
>>> print(guests)
['Quinta', 'Keren', 'Princess']
>>> guests.remove('Princess')
>>> print(guests)
['Quinta', 'Keren']
>>> guests.remove('Keren')
>>> print(guests)
['Quinta']
>>> guests.remove('Quinta')
>>> print(guests)
[]
