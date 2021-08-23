users={
    1000:{"acconu_num":1000,"password":"user1","balance":3000},
    1001: {"acconu_num": 1001, "password": "user2", "balance": 4000},
    1002: {"acconu_num": 1002, "password": "user2", "balance": 5000},
    1003: {"acconu_num": 1003, "password": "user3", "balance": 6000}
}


# Check for username and password

def validate(**kwargs):
    accno=kwargs["accno"]
    passw=kwargs["password"]
    if accno in users:
        if passw==users[accno]["password"]:
            print("Succes")
        else:
            print("Wrong password")
    else:
        print("Invalid accountno")

user=int(input("Enter the account number:"))
passw=input("Enter the password:")
validate(accno=user,password=passw)