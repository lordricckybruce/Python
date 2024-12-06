#!/usr/bin/env python3
message = "Hello world"
print(message)
print(message.title())
name = 'Alex'
lname = 'Ebuka'
fullname = name+ " "  + lname
print(f"hello, {fullname.title()}")

name = 'Theophilus Sunday'
print(f"Apostle {name.upper()}")
print(f'His name is {name.lower()}')
print(f'Apostle {name.title()}')


bikes = ['toshiba','supersport','toyota','nissan']
for n in bikes:
	#print(n)
	print(f'I love {n.title()}')
	print(n[0:3])
	print(n[1:4:2].title())
tr = ['abike','tosin']
tr.append("tayo")
print(tr)
