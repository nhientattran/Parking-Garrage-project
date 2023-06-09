from time import sleep
from IPython.display import Image 
from IPython.display import display
import time

parking_image = 'parking.png'

class Parking_garrage():
    def __init__(self, num_tickets, num_parking_spaces):
        self.tickets = list(range(1, num_tickets + 1))
        self.parking_spaces = list(range(1, num_parking_spaces + 1))
        self.current_tickets = {}

    def take_ticket(self):
        if self.tickets:
            ticket_numbers = self.tickets.pop(0)
            parking_spaces = self.parking_spaces.pop(0)
            self.entry_time = time.time()
            self.current_tickets[ticket_numbers] ={
                'num_ticket_number': ticket_numbers,
                'num_parking_space': parking_spaces,
                'paid': False,
                'entry_time': self.entry_time
            }
            print(f"Please take your ticket! Your ticket number is {ticket_numbers} and your parking space is {parking_spaces}. Please wait a moment for the gate to be opened!")
            sleep(1)
            print("-----------------------------------------")
            sleep(1)
            print("Door is opened! Please enter now!")

        else:
            print("Sorry, there are no availables tickets. Please wait.")

    
    def pay_for_parking(self):
        exit_time = time.time()
        num_ticket = int(input("Please enter your ticket number: "))
        entry_time = self.current_tickets[num_ticket]['entry_time']
        time_park = exit_time - entry_time
        price_park = round(time_park * 2)
        payment = int(input(f"You have been parked for {time_park} seconds. Your will be charged for ${price_park}. Please make a paymennt now! Please enter your payment: "))
        while True:
            if payment == price_park:
                print("Your ticket has been paid and you have 15 minutes to leave. Drive safe!")
                self.current_tickets[num_ticket]["paid"] = True
                break
            elif payment < price_park:
                balance = price_park - payment
                print(f"Sorry, we missing your payment. The remaining amout is ${balance}")
                price_park = balance
                payment = int(input(f"Please pay the amount of ${balance}. Enter your payment: "))


    def leave_garage(self):
        leave = int(input("What is your ticket number? "))
        if self.current_tickets[leave]['paid'] == True:
            print("Thank you! Be safe!")
            self.parking_spaces.append(self.current_tickets[leave]['num_parking_space'])
            self.tickets.append(self.current_tickets[leave]['num_ticket_number'])
            
        else:
            self.pay_for_parking()
    

class Main:
    
    display(Image(parking_image))
    
    def show_instruction():
        print("""
            Welcome to the Parking, the price will be $2 for each second you parked, please choose one of the options below:
            [1] Take ticket
            [2] Pay the ticket
            [3] Leave parking
        """)
    
    def run():
        Main.show_instruction()
        park = Parking_garrage(10,10)

        while True:
            choice = input("What would you like to do?: ")
            if choice == "1":
                park.take_ticket()

            elif choice == "2":
                if park.current_tickets == {}:
                    print("You have not enter the parking yet, please enter first!")
                else:
                    park.pay_for_parking()
            
            elif choice == "3":
                if park.current_tickets == {}:
                    print("Thank you, hope to see you again!")
                    break
                else:
                    park.leave_garage()
            else:
                print("Your choice is not valid, please try again.")

Main.run()
