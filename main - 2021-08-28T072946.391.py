#These notes are highly specialized are are for the CS Test-out on May 15th. Running code on Python for simiplity, this covers all the information needed. 

#Number Bases
#There are a total of 4 different Number Base systems.
#Binary(0,1)
#Octal(0,1,2,3,4,5,6,7,)
#Decimal(0,1,2,3,4,5,6,7,8,9)
#Hexadecimal(0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F (A=10, B=11, C=12, D=13, E=14, F=15))

#To convert between such bases, there is memorization required. Base 2 can convert into octal through a cht, which represents the value of all the various octal values. Scroll Beow to view the chart.

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


thisdict={
	"brand":"Ford",
  "model":"Mustang",
	 "year":"1964"
}

for x in thisdict:
	print(thisdict[x])

for x,y in thisdict.items()
	print(x,y)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict)