# coffee machine using Class methods

class Coffee_machine:

    def __init__(self, water, milk, coffee_beans, disposable_cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money

    def buy(self, water, milk, coffee_beans, money):
        self.water -= water
        self.milk -= milk
        self.coffee_beans -= coffee_beans
        self.money += money
        self.disposable_cups -= 1

    def fill(self, water, milk, coffee_beans, cups):
        self.water += water
        self.milk += milk
        self.coffee_beans += coffee_beans
        self.disposable_cups += cups

    def take(self):
        money_given = self.money
        print(f"I gave you ${money_given}\n")
        self.money = self.money - money_given

    def __str__(self):
        return f'''\nThe coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee_beans} of coffee beans
{self.disposable_cups} of disposable cups
${self.money} of money\n'''


machine = Coffee_machine(400, 540, 120, 9, 550)

exit_ = True

while True:
        
    action = input("Write action (buy, fill, take, remaining, exit):\n")
    if action == "buy":
        num = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if num == "1":
            if machine.water < 250 :
                print("Sorry, not enough water!\n")
            elif machine.coffee_beans < 16:
                print("Sorry, not enough coffee beans!\n")
            elif machine.disposable_cups < 1:
                print("Sorry, not enough disposable cups!\n")
            else:
                print("I have enough resources, making you a coffee!\n")
                machine.buy(250,0,16,4)
        elif num == "2":
            if machine.water < 350 :
                print("Sorry, not enough water!\n")
            elif machine.coffee_beans < 20:
                print("Sorry, not enough coffee beans!\n")
            elif machine.disposable_cups < 1:
                print("Sorry, not enough disposable cups!\n")
            elif machine.milk < 75:
                print("Sorry, not enough milk!\n")
            else:
                print("I have enough resources, making you a coffee!\n")
                machine.buy(350,75,20,7)
        elif num =="3":
            if machine.water < 200 :
                print("Sorry, not enough water!\n")
            elif machine.coffee_beans < 12:
                print("Sorry, not enough coffee beans!\n")
            elif machine.disposable_cups < 1:
                print("Sorry, not enough disposable cups!\n")
            elif machine.milk < 100:
                print("Sorry, not enough milk!\n")
            else:
                print("I have enough resources, making you a coffee!\n")
                machine.buy(200,100,12,6)
        else:
            continue
            
    elif action == "fill":
        w = int(input("\nWrite how many ml of water do you want to add:\n"))
        m = int(input("Write how many ml of milk do you want to add:\n"))
        c = int(input("Write how many grams of coffee beans do you want to add:\n"))
        cups =  int(input("Write how many disposable cups of coffee do you want to add:\n"))
        print()
        machine.fill(w,m,c,cups)

    elif action == "remaining":
        print(machine)

    elif action == "exit":
        break
    else:
        machine.take()
