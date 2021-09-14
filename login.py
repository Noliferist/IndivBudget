count = 0

def login():
    user = input("Username: ")
    passw = input("Password: ")
    f = open("users.txt", "r")
    for line in f.readlines():
        us, pw = line.strip().split("|")
        if (user in us) and (passw in pw):
            print("Login successful!")
            return True
    print("Wrong username/password")
    return False

def menu():
    ##main menu to be coded
    return True


def main():
    login()
    log = login()
    if log == True:
         menu()

class User:
    def __init__(self, id, username, password,):
        self.id = id
        self.username = username
        self.password = password

User1 = User(count, "John", "1234")
count = count+1

print(User1.id)
print(User1.username)
print(User1.password)

##if __name__ == "__main__":
    ##main()



