import random
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
random = random.choice(list)
sproba=0
my=0
while my != random:
	my=int(input("Вам потрібно вгадати число, яке загадала машина для вас. Це число в діапазоні від 1 до 50: "))
	sproba+=1
	if my>random:
		print("Ваше число більше за загадане")
		print("--------------------------")
	if my<random:
		print("Ваше число менше за загадане")
		print("--------------------------")
	
if my==random:
	print("--------------------------")
	print("Вітаю ви вгадали число з ",sproba," спроби")
	