#age = int(input("How old are you? "))
#if age == 100 :
#    print("You are a century old!")
#elif age >=18 :
#    print("You're an adult!")
#elif age < 0 :
#    print("You haven't been born yet!")
#else :
#    print("You're a child!")

#temp = int(input("What is the temperature outside? "))
#if temp >= 0  and  temp <= 30:
    #print("The temperature is good today!")
    #print("Go outside!")
#elif temp < 0 or temp > 30:
    #print("The temperature is bad today!")
    #print("Stay inside!")
#if not(temp >= 0  and  temp <= 30):
    #print("The temperature is bad today!")
    #print("Stay inside!")
#elif not(temp < 0 or temp > 30):
    #print("The temperature is good today!")
    #print("Go outside!")

#while 1==1:
    #print("Help! I'm stuck in a loop!")
#name = ""
#while len(name) == 0:
    #name = input("Enter your name: ")
#print("Hello " + name)
#name = None
#while not name:
    #name = input("Enter your name: ")
#print("Hello "+name)

#for i in range(10):
    #print(i+1)
#for i in range(50,100+1,2):
    #print(i)
#for i in "Renan Santos Pires":
    #print(i)
#import time
#for seconds in range (10,0,-1):
    #print(seconds)
    #time.sleep(1)
#print("Happy New Year!")

#rows = int(input("How many rows? "))
#columns = int(input("How many columns? "))
#symbol = input("Enter a symbol to use: ")
#for i in range (rows):
    #for j in range(columns):
        #print(symbol, end="")
    #print()

#while True :
    #name = input("Enter your name: ")
    #if name != "":
        #break
#phone_number = "123-456-7890"
#for i in phone_number:
    #if i == "-":
        #continue
    #print(i, end="")

#for i in range(1,21):
    #if i == 13:
        #pass
    #else:
        #print(i)

#food = ["pizza", "hamburger","hotdog", "spaghetti"]
#print (food[2])
#food[0] = "sushi"
#print (food[0])
#food.append("ice cream")
#food.remove("hotdog")
#food.pop()
#food.insert(0,"cake")
#food.sort()
#food.clear()
#for x in food:
    #print(x)

#drinks = ["coffe", "soda", "tea"]
#dinner = ["pizza","hamburger", "hotdog"]
#dessert = ["cake", "ice cream"]
#food = [drinks,dinner,dessert]
#print(food)
#print(food[2])
#print(food[1][2])

#student = ("Renan", 26, "male")
#print(student.count("Renan"))
#print(student.index("male"))
#for x in student :
    #print(x)
#if "Renan" in student:
    #print("Renan is here!")

#utensils = {"fork","spoon", "knife", "knife", "knife", "knife"}
#dishes = {"bowl", "plate", "cup", "knife" }
#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#utensils.update(dishes)
#dinner_table = utensils.union(dishes)
#for x in utensils:
    #print(x)
#for x in dinner_table:
    #print(x)
#print(utensils.difference(dishes))
#print(utensils.intersection(dishes))

#capitals = {'USA':'Washington DC',
            #'India' : 'New Dehli',
            #'China': 'Beijing',
            #'Brazil': 'Brasilia'}
#print(capitals['Brazil'])
#print(capitals['Germany'])
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())
#for key,value in capitals.items():
    #print(key,value)
#capitals.update({'Germany':'Berlin'})
#capitals.update({'USA':'New York'})
#capitals.pop('China')
#capitals.clear()
#for key,value in capitals.items():
    #print(key,value)

#name = "renan Pires"
#if(name[0].islower()):
    #name = name.capitalize()
#print(name)
#first_name = name[:5].upper()
#last_name = name[6:].lower()
#last_character = name[-1]
#print(first_name)
#print(last_name)
#print(last_character)



