import sqlite3
import random

#connection
conn = sqlite3.connect("BankABC.db")
cur = conn.cursor()

class DBMS:
    def __init__(self):
        self.choosing = True
        self.table_name = "bankdb"
        self.options = {1: "Create Account",
                        2: "Deposit",
                        3: "Withdraw",
                        4: "Account Summary",
                        5: "Quit"}

        # create table if does not exist
        cur.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name}(ac_no int primary key, name varchar(40), balance int)")

    def create_account(self):
        print("\nWelcome to the Account Creation Portal")
        name = input("Enter your name: ")
        ac_no = random.randint(1000000000000000,9999999999999999)
        print("Account number : ",ac_no)

        cur.execute(f"INSERT INTO {self.table_name} (ac_no, name, balance) VALUES (?,?,0)",(ac_no, name))

        print("Account successfully created")

        self.delay_home()

    def deposit(self):
        print("\nWelcome to the Money Deposit Portal")
        
        # account login
        ac_no = int(input("Enter account number: "))

        cur.execute(f"SELECT ac_no FROM {self.table_name}")

        # if account exists
        if (ac_no,) in cur.fetchall():

            cur.execute(f"SELECT name FROM {self.table_name} WHERE ac_no = ?",(ac_no,))

            print("Name:", cur.fetchone()[0])

            cur.execute(f"SELECT balance FROM {self.table_name} WHERE ac_no = ?",(ac_no,))
            initial_bal = cur.fetchone()[0]
            print("Initial Balance:", initial_bal)

            # deposit amount
            amount = int(input("Enter Amount to deposit: "))

            new_bal = amount + initial_bal
            
            cur.execute(f"UPDATE {self.table_name} SET balance = ? WHERE ac_no = ?",(new_bal,ac_no))

            print("Successfully deposited amount")

            # saving changes
            conn.commit()
        else:
            print("Account not found")
        self.delay_home()

    def withdraw(self):

        print("\nWelcome to the Money Withdraw Portal")
        
        # account login
        ac_no = int(input("Enter account number: "))

        cur.execute(f"SELECT ac_no FROM {self.table_name}")

        # if account exists
        if (ac_no,) in cur.fetchall():

            cur.execute(f"SELECT name FROM {self.table_name} WHERE ac_no = ?",(ac_no,))
            print("Name:", cur.fetchone()[0])

            cur.execute(f"SELECT balance FROM {self.table_name} WHERE ac_no = ?",(ac_no,))
            initial_bal = cur.fetchone()[0]
            print("Initial Balance:", initial_bal)

            # withdraw amount
            amount = int(input("Enter Amount to withdraw: "))

            # if withdrawal is possible
            if amount < initial_bal:
                new_bal = initial_bal - amount
                
                cur.execute(f"UPDATE {self.table_name} SET balance = ? WHERE ac_no = ?",(new_bal,ac_no))

                print("Successfully withdrawn amount.")

                # saving changes
                conn.commit()
            else:
                print("Cannot Withdraw Amount")

        else:
            print("Account not found")

        self.delay_home()

    def summary(self):
        
        ac_no = int(input("Enter account number: "))

        
        cur.execute(f"SELECT ac_no FROM {self.table_name}")

        # if account exists
        if (ac_no,) in cur.fetchall():
            cur.execute(f"SELECT name,balance FROM {self.table_name} WHERE ac_no = ?",(ac_no,))
            for row in cur.fetchall():
                print("Name:", row[0])
                print("Main Balance:", row[1])
        else:
            print("Account not found")
    
        self.delay_home()

    def delay_home(self):
        _ = input("Press Enter to return to home page.")
        self.home()

    def home(self):
        self.choosing = True
        print("\nWelcome to ABC Bank \n")

        while self.choosing:
            for option in self.options:
                print(option,":",self.options.get(option))
            choice = input("Enter number corresponding to the desired option: ")

            self.choosing = False
            if choice == '1': self.create_account()
            elif choice == '2': self.deposit()
            elif choice == '3': self.withdraw()
            elif choice == '4': self.summary()
            elif choice == '5': 
                print("Thank You")
                cur.close()
                conn.close()
                quit()
            else: self.choosing = True
    
My_DBMS = DBMS()

My_DBMS.home()
