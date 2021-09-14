import csv

def createUser():
    f = open("user.txt", "a")
    username = input("Selected username: ")
    password = input("Selected password: ")
    f.writelines(username + " | " + password + "\n")
    f.close()

    budget_sheet_name = username + ".csv"
    header = ["Category", "Amount"]
    file = open(budget_sheet_name, "w")
    writer = csv.writer(file)
    writer.writerow(header)
    file.close()

createUser()