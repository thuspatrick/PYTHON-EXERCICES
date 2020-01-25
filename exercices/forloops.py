# Nettoyer la console avant le demarrage du programme #
import os
os.system('clear')
#######################################################

##################
# Les Dictionnaires #
#################
favorite_color = {
	"patrick" : "blue",
	"lionel" : "red",
	"adrien" : "green",
	"nathan" : "lightblue",
	"maxime" : "rose",
}

# looping in dictionnaries

print("The keys are :")
for key,value in favorite_color.items():
	print(key)

print("The values are :")
for key,value in favorite_color.items():
	print(value)