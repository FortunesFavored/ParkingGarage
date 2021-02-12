class lot():
    
    cur = [1,2,3,4,5,6,7,8,9,10]
    
    def __init__(self):
        self.spaces = lot.cur

class tickets:
    
    current_ticket = 1
    #manage tickets for spaces in the lot
    def __init__(self, driver, spot, paid=False):
        self.driver = driver
        self.spot = int(spot)
        self.paid = paid
        
    def choseSpot(self):
        garage.spaces.remove(self.spot)
        
    def leaveSpot(self):
        garage.spaces.append(self.spot)
        
    def pay_ticket(self):
        self.paid = True

        
garage = lot()
    
    
    
def main():
    peeps = []
    names = []
    while True:
        print(f"Current available spots: {sorted(garage.spaces)}")
        action = input('Would you like a "Ticket", "Pay", or "Leave"? ').lower().strip()
        if action == 'ticket':
            print('Current Available Spots are: ', garage.spaces)
            driver = input('Who is the driver? ')
            spot = int(input('What spot did you park in? '))
            driver = tickets(driver,spot)
            driver.choseSpot()
            peeps.append(driver)
            names.append(driver.driver)
            continue
        elif action == 'pay':
            print(f"Current spot holders: {names}")
            customer = input('Who are you? ')
            for i in peeps:
                if customer == i.driver:
                    driver = i
                    break
            else:
                print("You don't have the right to be here. ")
                continue
            if driver.paid == True:
                print("youve already paid")
            else:
                x = input('How would you like to pay? (Cash, Credit, Bitcoin) ')
                driver.pay_ticket()
                print("You have paid! skiddadle")
        
        elif action == 'leave':
            print(names)
            customer = input('Who are you? ')
            for i in peeps:
                if customer == i.driver:
                    driver = i
                    break
            else:
                print("You're not even supposed to be here ")
                continue
            if driver.paid == True:
                driver.leaveSpot()
                print("Thank you come again ")
            else:
                print("I WANT MY MONEY SAM!! ")
                print(f"but foreal {driver.driver} you need to pay! ")
                
            
        elif action == 'quit':
            break
        else:
            print('Invalid Input please try again Sammy ')
        
    
    
main()