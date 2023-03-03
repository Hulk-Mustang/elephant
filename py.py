#Enter the number of your coffee starting from zero
coffee = ["Café Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"]

choice = int(input())

try:
	print(coffee[choice])
except:
	print("There is no such number")
finally: 
	print("Have a good day")
