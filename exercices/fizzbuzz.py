# Nettoyer la console avant le demarrage du programme #
import os
os.system('clear')
#######################################################

##################
# FIZZBUZZ #
#################

num = 1

while num <= 100:
	if ((num % 3) == 0) and ((num % 5) == 0):
		print("FIZZBUZZ " + str(num) + "est divisible par 3 et 5")
	elif (num % 5) == 0:
		print("BUZZ " + str(num) + "est divisible par 5")
	elif (num % 3) == 0:
		print("FIZZ " + str(num) + "est divisible par 3")
	else:
		print(num)
	num += 1
#	print(num)
	
