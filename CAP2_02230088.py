######################################
#Tenzin Wangyel
#02230088
#1st Electrical Engineering
######################################
# CSF Assignment 2
# CAP2_02230088.py
######################################
#Refference
# https://www.youtube.com/watch?v=UEO1B_llDnc
# https://www.youtube.com/watch?v=W6cjx7t39d4&t=11s
# https://www.youtube.com/watch?v=d038LZp_Jhk
# chatgpt.com
######################################




import random

class Acc:
    def __init__(self, acc_no, password, acc_type, balance=0):
        self.acc_no = acc_no  # Store account number
        self.password = password  # Store password
        self.acc_type = acc_type  # Store acc type
        self.balance = balance  # Store balance

    def deposit(self, amount):
        self.balance += amount  # Add up deposited amount to balance
        return self.balance  # Return updated balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"  # Amount should not exceed balance
        self.balance -= amount  # Deduct withdrawal amount from balance
        return self.balance  # Return updated balance

    def send_money(self, receiver_acc, amount):
        if amount > self.balance:
            return "Insufficient funds"  # If amount to send exceeds balance
        receiver_acc.deposit(amount)  # Transfer amount to receiver's acc
        self.balance -= amount  # Deduct sent amount from balance
        return self.balance  # Return updated balance


class Bank:
    def __init__(self):
        self.accs = {}  

    def create_acc(self, acc_type):
        acc_no = random.randint(100000000, 999999999)  # Generate random acc number of nine digit
        password = 'password123'  # Generate random password
        acc = Acc(acc_no, password, acc_type)  # Create new acc
        self.accs[acc_no] = acc  # Add acc to dictionary []
        return acc  # Return newly created acc

    def login(self, acc_no, password):
        acc = self.accs.get(acc_no)  # Get acc with given acc number
        if acc and acc.password == password:
            return acc  # Return acc if found and password matches
        return None  # Return None if acc is not found or password mismatch

    def delete_acc(self, acc_no):
        if acc_no in self.accs:
            del self.accs[acc_no]  # Delete acc if exists
            return True  # For successful deletion
        return False  # Return False if acc does not exist

    def check_balance(self, acc_no):
        if acc_no in self.accs:
            return self.accs[acc_no].balance  # Return balance if acc exists
        return None  # Return None if acc does not exist


def main():
    bank = Bank()  # Create Bank instance

    while True:
        print("\nWelcome to the Terminal Bank")
        print("1. Create Account(acc)")
        print("2. Login")
        print("3. Exit")
        choice = input("Choice from 1-3: ") 

        if choice == '1':
            acc_type = input("Enter acc type (Personal/Business): ").lower()  # Prompt for acc type
            acc = bank.create_acc(acc_type)  # Create acc
            print("Acc created successfully.") # Succefully created
            print("Your acc number is:", acc.acc_no) # random acc no
            print("Your default password is: password123")  # Print acc details

        elif choice == '2':
            acc_no = int(input("Enter your acc number: "))  # Prompt for acc number
            password = input("Enter your password: ")  # Prompt for password
            acc = bank.login(acc_no, password)  # Login to acc
            if acc:
                print("Login successful.")  # Print login success message
                while True:
                    print("\n1. Check Balance")
                    print("2. Deposit money")
                    print("3. Withdraw money")
                    print("4. Send Money")
                    print("5. Delete Acc")
                    print("6. Logout")
                    option = input("Choice any from 1-6: ")  

                    if option == '1':
                        print("Your balance:", acc.balance)  # Print acc balance

                    elif option == '2':
                        amount = float(input("Enter amount to deposit: "))  # Prompt for deposit amount
                        acc.deposit(amount)  # Deposit amount
                        print("Deposit successful. Your balance:", acc.balance)  # Updated balance

                    elif option == '3':
                        amount = float(input("Enter amount to withdraw: "))  # Prompt for withdrawal amount
                        result = acc.withdraw(amount)  # Withdraw amount
                        if isinstance(result, str):
                            print(result)  # Print error if withdrawal fails
                        else:
                            print("Withdrawal successful. Your balance:", result)  # Print updated balance

                    elif option == '4':
                        receiver_acc_no = int(input("Enter receiver's acc number: "))  # Prompt for receiver's acc number
                        amount = float(input("Enter amount to transfer: "))  # Prompt for amount to send
                        receiver_acc = bank.accs.get(receiver_acc_no)  # Get receiver's acc
                        if receiver_acc:
                            result = acc.send_money(receiver_acc, amount)  # Send money to receiver's acc
                            if isinstance(result, str):
                                print(result)  # Print error if sending money fails
                            else:
                                print("Money transfered successfully. Your acc balance:", result)  # Print updated balance
                        else:
                            print("Receiver's acc doesnt exist.")  # Print error message if receiver's acc does not exist

                    elif option == '5':
                        confirm = input("Do you want to delete your acc for sure? (yes/no): ")  # Confirm acc deletion
                        if confirm.lower() == 'yes':
                            if bank.delete_acc(acc_no):
                                print("Acc deleted.")  # Print acc deletion success message
                                break
                            else:
                                print("Failed acc deletion.")  # Print acc deletion failure message
                                break

                    elif option == '6':
                        break  # Logout

        elif choice == '3':
            print("Thank you for using our services.")  # Print exit message
            break  # Exit the program

        else:
            print("Invalid. Try again.")  # Print error message for invalid choice


if __name__ == "__main__":
    main()
