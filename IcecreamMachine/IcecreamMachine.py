from enum import Enum
# make a tests folder under the folder you're putting these files in
# add an empty __init__.py to the tests folder
from IcecreamExceptions import ExceededRemainingChoicesException, InvalidChoiceException, NeedsCleaningException, OutOfStockException
from IcecreamExceptions import InvalidPaymentException

class Usable:
    name = ""
    quantity = 0
    cost = 99

    def __init__(self, name, quantity = 5, cost=99):
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def use(self):
        self.quantity -= 1
        if (self.quantity < 0):
            raise OutOfStockException("Item is out of stock.")# UCID se352, Date 19 October 2022
        return self.quantity 

    def in_stock(self):
        return self.quantity > 0

class Container(Usable):
    pass

class Flavor(Usable):
    pass

class Toppings(Usable):
    pass

class STAGE(Enum):
    Container = 1
    Flavor = 2
    Toppings = 3
    Pay = 4

class IceCreamMachine:
    # Constants https://realpython.com/python-constants/
    USES_UNTIL_CLEANING = 100
    MAX_SCOOPS = 3
    MAX_TOPPINGS = 3


    containers = [Container(name="Waffle Cone", cost=1.5), Container(name="Sugar Cone", cost=1), Container("Cup", cost=1)]
    
    flavors = [Flavor(name="Vanilla", quantity=100, cost=1), Flavor(name="Chocolate", quantity=100, cost=1), Flavor(name="Strawberry", quantity=100, cost=1)]
    
    toppings = [Toppings(name="Sprinkles", quantity=200, cost=.25), Toppings(name="Chocolate Chips", quantity=200, cost=.25), Toppings(name="M&Ms", quantity=200, cost=.25), \
    
    Toppings(name="Gummy Bears", quantity=200, cost=.25), Toppings(name="Peanuts", quantity=200, cost=.25)] 


    # variables
    remaining_uses = USES_UNTIL_CLEANING
    remaining_scoops = MAX_SCOOPS
    remaining_toppings = MAX_TOPPINGS
    total_sales = 0
    total_icecreams = 0

    inprogress_icecream = []
    currently_selecting = STAGE.Container

    # rules
    # 1 - container must be chosen first
    # 2 - can only use items if there's quantity remaining
    # 3 - scoops can't exceed max
    # 4 - toppings can't exceed max
    # 5 - a container and at least 1 scoop or toppings must be selected
    # 6 - proper cost must be calculated and shown to the user
    # 7 - cleaning must be done after certain number of uses before any more icecreams can be made
    # 8 - total sales should calculate properly based on cost calculation
    # 9 - total_icecreams should increment properly after a payment
    

    def pick_container(self, choice):
        for c in self.containers:
            if c.name.lower() == choice:
                c.use()
                self.inprogress_icecream.append(c)
                return
        raise InvalidChoiceException("Invalid choice of container.")# UCID se352, Date 19 October 2022

    def pick_flavor(self, choice):
        if self.remaining_uses <= 0:# UCID se352, Date 19 October 2022
            raise NeedsCleaningException("Couldn't add the flavor. Icecream Machine needs cleaning")
        if self.remaining_scoops <= 0:# UCID se352, Date 19 October 2022
            raise ExceededRemainingChoicesException("Didn't add the scoop. You have exceeded the maximum scoop limit")
        for f in self.flavors:
            if f.name.lower() == choice:
                f.use()
                self.inprogress_icecream.append(f)
                self.remaining_scoops -= 1
                self.remaining_uses -= 1
                return
        raise InvalidChoiceException("Invalid choice of flavor.")# UCID se352, Date 19 October 2022

    def pick_toppings(self, choice):
        if self.remaining_toppings <= 0:# UCID se352, Date 19 October 2022
            raise ExceededRemainingChoicesException("Did not add the toppings. You have exceeded the maximum toppings limit")
        for t in self.toppings:
            if t.name.lower() == choice:
                t.use()
                self.inprogress_icecream.append(t)
                self.remaining_toppings -= 1
                return
        raise InvalidChoiceException("Invalid choice of Toppings.")# UCID se352, Date 19 October 2022

    def reset(self):
        self.remaining_scoops = self.MAX_SCOOPS
        self.remaining_toppings = self.MAX_TOPPINGS
        self.inprogress_icecream = []
        self.currently_selecting = STAGE.Container

    def clean_machine(self):
        self.remaining_uses = self.USES_UNTIL_CLEANING
        
    def handle_container(self, container):
        self.pick_container(container)
        self.currently_selecting = STAGE.Flavor

    def handle_flavor(self, flavor):
        if flavor == "next":
            self.currently_selecting = STAGE.Toppings
        else:
            self.pick_flavor(flavor)

    def handle_toppings(self, toppings):
        if toppings == "done":
            self.currently_selecting = STAGE.Pay
        else:
            self.pick_toppings(toppings)

    def handle_pay(self, expected, total):
        if total == str(expected):
            print("Thank you! Enjoy your icecream!")
            self.total_icecreams += 1
            self.total_sales += float(expected) # only if successful
            self.reset()
        else:
            raise InvalidPaymentException("Invalid Payment")# UCID se352, Date 19 October 2022
            
    def calculate_cost(self):
        # UCID - se352, Date - 17th October 2022
        # inprogress_icecream is a list containing different class objects like Container, Flavour & Toppings.
        # To calculate the total cost, simply summing up the "cost" instance attribute of each class will do the job.
        # I have writtten a for loop that iterates through the list of objects and grabs the cost of each item. 
        # Append those items to a list and total cost can be calculated by using the sum() method.
        # finally the currency variable is used to store the formatted value of the sum. (upto two decimal places was asked)
        x = self.inprogress_icecream
        y = []
        for each_item in x:
            y.append(each_item.cost)
            z = float(sum(y))
            currency = f'{z:.2f}'

        return currency

    def run(self):
        if self.currently_selecting == STAGE.Container:
            try:#checks if there are any containers left in stock. only proceeds if there is atleast one container.
                if len(list(map(lambda c:c.name.lower(), filter(lambda c: c.in_stock(), self.containers)))) > 0:
                    container = input(f"Would you like a {', '.join(list(map(lambda c:c.name.lower(), filter(lambda c: c.in_stock(), self.containers))))}?\n")
                    self.handle_container(container)
                else:
                    print("no containers left, Sorry!")
                    exit()

                    
            # ucid - se352
            # Date October 19, 2022
            # OUT OF STOCK EXCEPTION
            except OutOfStockException as oos:
                print(oos)
                print("Please select from available options")
                self.currently_selecting = STAGE.Container


            # ucid - se352
            # Date October 19, 2022
            # INVALID CHOICE EXCEPTION
            except InvalidChoiceException as ice:
                print(ice)
                print("Please enter a valid item from the available containers.")
                self.currently_selecting = STAGE.Container



        # TODO ADD oos exception.
        elif self.currently_selecting == STAGE.Flavor:
            try:
                flavor = input(f"Would you like {', '.join(list(map(lambda f:f.name.lower(), filter(lambda f: f.in_stock(), self.flavors))))}? Or type next.\n")
                self.handle_flavor(flavor)


            # ucid - se352
            # Date October 19, 2022
            # INVALID CHOICE EXCEPTION
            except InvalidChoiceException as ice:
                print(ice)
                print("Please enter a valid item from the available flavors.")
                self.currently_selecting = STAGE.Flavor


            # ucid - se352
            # Date October 19, 2022
            # NEEDSCLEANING EXCEPTION TAKES INPUT FROM USER TO CONTINUE
            except NeedsCleaningException as nce:
                print(nce)
                do_clean = input("Do you want the machine to be cleaned?( yes or no ):")
                if (do_clean.lower() == "yes"):
                    self.clean_machine()
                    self.currently_selecting = STAGE.Flavor
                elif(do_clean.lower() == "no"):
                    exit()

            # ucid - se352
            # Date October 19, 2022
            # EXCEEDED REMAINING CHOICES EXCEPTION
            except ExceededRemainingChoicesException as erce:
                print(erce)
                print("Please enter 'next'")
                self.currently_selecting = STAGE.Flavor

            # ucid - se352
            # Date October 19, 2022
            # OUT OF STOCK EXCEPTION
            except OutOfStockException as oos:
                print(oos)
                print("Please select from available options")
                self.currently_selecting = STAGE.Flavor





            # TODO  add oos
        elif self.currently_selecting == STAGE.Toppings:
            try:
                toppings = input(f"Would you like {', '.join(list(map(lambda t:t.name.lower(), filter(lambda t: t.in_stock(), self.toppings))))}? Or type done.\n")
                self.handle_toppings(toppings)

            # ucid - se352
            # Date October 19, 2022
            # INVALID CHOICE EXCEPTION
            except InvalidChoiceException as ice:
                print(ice)
                print("Please enter a valid item from the available Toppings.")
                self.currently_selecting = STAGE.Toppings

            # ucid - se352
            # Date October 19, 2022
            # EXCEEDED REMAINING CHOICES EXCEPTION
            except ExceededRemainingChoicesException as erce:
                print(erce)
                print("Please enter 'done'")
                self.currently_selecting = STAGE.Toppings

            # ucid - se352
            # Date October 19, 2022
            # OUT OF STOCK EXCEPTION
            except OutOfStockException as oos:
                print(oos)
                print("Please select from available options")
                self.currently_selecting = STAGE.Toppings



        elif self.currently_selecting == STAGE.Pay:
            # Handling the conditions of atleast one topping or one flavor
            # The following snippet gives a set of options to the user to either choose a flavor or topping.
            # They can quit here if they don't want the icecream.
            if len(self.inprogress_icecream) == 1:
                select_option = input("Please select atleast one flavor (or) toppings, else enter 'quit' (flavor or toppings or quit):\n")
                if select_option.lower() == "flavor":
                    self.currently_selecting = STAGE.Flavor
                elif select_option.lower() == "toppings":
                    self.currently_selecting = STAGE.Toppings
                elif select_option.lower() == "quit":
                    exit()
                else:
                    exit()
            else:        
                expected = self.calculate_cost()
                try:
                    total = input(f"Your total is {expected}$, please enter the exact value.\n")
                    self.handle_pay(expected, total)
                    choice = input("What would you like to do? (icecream or quit)\n")
                    if choice == "quit":
                        exit()
                # ucid - se352
                # Date October 19, 2022
                # INVALID PAYMENT EXCEPTION
                except InvalidPaymentException as ipe:
                    print(ipe)
                    print(f"Wrong total amount entered, try again.")
                    self.currently_selecting = STAGE.Pay

        self.run()

    def start(self):
        self.run()

    
if __name__ == "__main__":
    icm = IceCreamMachine()
    icm.start()