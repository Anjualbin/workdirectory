users={
    1000:{"acconu_num":1000,"password":"user1","balance":3000},
    1001: {"acconu_num": 1001, "password": "user2", "balance": 4000},
    1002: {"acconu_num": 1002, "password": "user2", "balance": 5000},
    1003: {"acconu_num": 1003, "password": "user3", "balance": 6000}
}


# Check for username and password

def validate(accno,passw):
    if accno in users:
        if passw==users[accno]["password"]:
            print("Succes")
        else:
            print("Wrong password")
    else:
        print("Invalid accountno")

user=int(input("Enter the account number:"))
passw=input("Enter the password:")
validate(user,passw)


# getbalance

def getbalance(accno):
    if accno in users:
        print(users[accno]["balance"])
    else:
        print("Invalid account no")

getbalance(1003)