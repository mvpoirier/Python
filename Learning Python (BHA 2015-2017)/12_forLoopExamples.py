for i in range(10):
	print(i)

for i in range(10):
	print(i, end = " ")

for icecream in range(5):
	print("Bacon!")

myFood = ["Bacon", "Pizza", "Perogies", "Cheese"]
for i in myFood:
	print(i)

for i in range(100):
	print("Physics is awesome!")

for i in range(1, 11):
	if i < 5:
		print("%s is < 5." % (str(i)))
	else:
		print("%s is >= 5." % (str(i)))

for baconIcecreamPopsicle in range(100):
	if baconIcecreamPopsicle % 2 == 0:
		print("%s is even." % (str(baconIcecreamPopsicle)))
	else:
		print("%s is odd." % (str(baconIcecreamPopsicle)))

for a in range(5):
	for i in range(5):
		print("-"*i + "*")
	for i in range(5):
		print("-"*(4 - i) + "*")
