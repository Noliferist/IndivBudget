import login
import createUser
import categories

def menu():
    x = input("Please select an action to perform")
    print("1. create new account")
    print("2. Update income")
    print("3. Check budget")
    print("4. Check savings")
    print("5. Update savings")
    x = int(x)
    if x == 1:
        createUser()
        return True
    elif x == 2:
        ##updateIncome()
        return False
    elif x == 3:
        ##checkBudget()
        return False
    elif x == 4:
        ##checkSavings()
        return False
    elif x == 5:
        ##updateSavings()
        return False
    else:
        print("Selected an invalid option! \n Please try again")



def main():
    login()
    if login() == True:
        menu()

main()