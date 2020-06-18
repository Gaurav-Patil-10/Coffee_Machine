
# # water = int(input('Write how many ml of water the coffee machine has:\n'))

# # milk = int(input('Write how many ml of milk the coffee machine has:\n'))

# # coffee = int(input('Write how many grams of coffee beans the coffee machine has:\n'))

# # cups = int(input('Write how many cups of coffee you will need:\n'))
# # # # 200 water * 50 milk  * 15 gm coffee
# # cups_made = min(water//200,milk//50,coffee//15)

# # if cups == cups_made:
# #     print("Yes,I can make that amount of cofee")

# # elif cups_made < cups :
# #     print(f"No, I can make only {cups_made} cups of coffee")

# # elif cups_made > cups :
# #     print(f"Yes,I can make that amount of cofee (and even {cups_made - cups} more than that)")


# print(f'''The coffee machine has:
# {water} of water
# {milk} of milk
# {coffee_beans} of coffee beans
# {disposable_cups} of disposable cups
# {money} of money\n''')

water = 400
milk = 540
coffee_beans = 120 
disposable_cups = 9
money = 550
def buy(n):
    global water , milk , coffee_beans , disposable_cups , money
    if n==1:
        water = water - 250
        coffee_beans = coffee_beans - 16
        money = money + 4
        disposable_cups = disposable_cups - 1
        print("I have enough resources, making you a coffee!\n")
    elif n == 2:
        water = water - 350
        milk = milk - 75
        coffee_beans = coffee_beans - 20
        money = money + 7
        disposable_cups = disposable_cups - 1
        print("I have enough resources, making you a coffee!\n")
    elif n==3 :
        water = water - 200
        milk = milk - 100
        coffee_beans = coffee_beans - 12
        money = money + 6
        disposable_cups = disposable_cups - 1
        print("I have enough resources, making you a coffee!\n")


def fill(w,m,c,cups):
    global water , milk , coffee_beans , disposable_cups , money
    water = water + w
    milk = milk + m
    coffee_beans = coffee_beans + c 
    disposable_cups = disposable_cups + cups  


def remaining():
    global water , milk , coffee_beans , disposable_cups , money
    print(f'''\nThe coffee machine has:
{water} of water
{milk} of milk
{coffee_beans} of coffee beans
{disposable_cups} of disposable cups
{money} of money\n''')


def take ():
    global money
    print(f"I gave you ${money}\n")
    money = 0
    
    

    

exit_ = True

while True:
        
    action = input("Write action (buy, fill, take, remaining, exit):\n")
    if action == "buy":
        num = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if num == "1":
            if water < 250 :
                print("Sorry, not enough water!\n")
            elif coffee_beans < 16:
                print("Sorry, not enough coffee beans!\n")
            elif disposable_cups < 1:
                print("Sorry, not enough disposable cups!\n")
            else:
                buy(int(num))
        elif num == "2":
            if water < 350 :
                print("Sorry, not enough water!\n")
            elif coffee_beans < 20:
                print("Sorry, not enough coffee beans!\n")
            elif disposable_cups < 1:
                print("Sorry, not enough disposable cups!\n")
            elif milk < 75:
                print("Sorry, not enough milk!\n")
            else:
                buy(int(num))
        elif num =="3":
            if water < 200 :
                print("Sorry, not enough water!\n")
            elif coffee_beans < 12:
                print("Sorry, not enough coffee beans!\n")
            elif disposable_cups < 1:
                print("Sorry, not enough disposable cups!\n")
            elif milk < 100:
                print("Sorry, not enough milk!\n")
            else:
                buy(int(num))
        else:
            continue
            
    elif action == "fill":
        w = int(input("\nWrite how many ml of water do you want to add:\n"))
        m = int(input("Write how many ml of milk do you want to add:\n"))
        c = int(input("Write how many grams of coffee beans do you want to add:\n"))
        cups =  int(input("Write how many disposable cups of coffee do you want to add:\n"))
        print()
        fill(w,m,c,cups)

    elif action == "remaining":
        remaining()

    elif action == "exit":
        break
    else:
        take()

    # print(f'''\nThe coffee machine has:
    # {water} of water
    # {milk} of milk
    # {coffee_beans} of coffee beans
    # {disposable_cups} of disposable cups
    # {money} of money''')




