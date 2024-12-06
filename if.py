#!/bin/python3

cars = ['audi','bmw','benz','dodge','f1','lambogini','chevorett']
for s in cars:
	if s == 'bmw':
		print(f'Damn {s.title()}')
	else:
		print('miras')
'''
questionaire = input("Enter your betting platform: ")
vets = ['msport','bet9ja','sportybet','kingbet']
if questionaire in vets:
	print(f'{vets} are True')
else:
	print(f'{vets} not verified')


print(input("WELCOME TO TEST CENTER"))
print('Grading systems are followed by the cutoff marks of the educational systems provided')
grade = 400
score = int(input("Input your score: "))
if score >= 180:
	print("Congratulations, University levelup")
elif score >= 160:
	print("Polytechnic")
elif score != 150:
	print("Reapply")
'''

usernames = ['ada','felix','festus','oyindamola','chika']
for s in usernames:
	print(f'Hello, {s.title()}')
usernames.append('admin')
print(usernames)
print(f'Hello, {usernames[5].title()}, would you like to see status report?')
if usernames != s:
	print(s)
else:
	print("Hello Eric")
