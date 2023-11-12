driving = input('Did you ever drive car? ')
if driving != 'yes' and driving != 'no':
	print('only can reply yes or no')
	raise SystemExit

age = input('how old are you? ')
age =  int(age)
if driving == 'yes':
	if age >= 18:
		print('pass')
	else:
		print('fail')
elif driving == 'no':
	if age >= 18:
		print('you can get the license')
	else:
		print('you can get the license several years later')