# Nettoyer la console avant le demarrage du programme #
import os
os.system('clear')
#######################################################
user = "patrick"
print("1 - Bonjour tout le monde...")
print("2 - Bonjour " + user + "\n")
##################
# Les tuples #
#################
tuple1 = ("Angelina", "Gabriela", "Daniela")
tuple2 = ("Flore",)
mytuple = tuple1 + tuple2

print(mytuple[0:3])

##################
# Les Dictionnaires #
#################
favorite_color = {
	"patrick" : "blue",
	"lionel" : "red",
	"adrien" : "vert",
	"nathan" : "lightblue",
	"maxime" : "rose",
}

print(favorite_color)

#print(favorite_color["maxime"])
# Delete key_value pair(s) in dictionnary
# del favorite_color["adrien"]

# add key_value pair(s) in dictionnary
# favorite_color.update({"megan":"yellow"})

print("The new dictionnary is")
print(favorite_color)