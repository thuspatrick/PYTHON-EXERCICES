# Nettoyer la console avant le demarrage du programme #
import os
os.system('clear')
#######################################################

##################
# counting FIZZBUZZ #
#################

num = 1
fizzes = 0
buzzes = 0
fizzbuzzes = 0
fizval = []
buzval = []
fizbuzval = []

while num <= 1000:
	if ((num % 3) == 0) and ((num % 5) == 0):
		print("FIZZBUZZ " + str(num) + " est divisible par 3 et 5")
		fizzbuzzes += 1
		fizbuzval.append(num)
	elif (num % 5) == 0:
		print("BUZZ " + str(num) + " est divisible par 5")
		buzzes += 1
		buzval.append(num)
	elif (num % 3) == 0:
		print("FIZZ " + str(num) + " est divisible par 3")
		fizzes += 1
		fizval.append(num)
	else:
		print(num)
	num += 1
print("\nFizzes = " + str(fizzes))
print("All Fizzes : " + str(fizval))
print("\nBuzzes = " + str(buzzes))
print("All Buzzes : " + str(buzval))
print("\nFizzbuzzes = " + str(fizzbuzzes))
print("All Fizzbuzzes : " + str(fizbuzval))