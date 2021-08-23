class Bank:
    users = {
        1000: {"acconu_num": 1000, "password": "user1", "balance": 3000},
        1001: {"acconu_num": 1001, "password": "user2", "balance": 4000},
        1002: {"acconu_num": 1002, "password": "user2", "balance": 5000},
        1003: {"acconu_num": 1003, "password": "user3", "balance": 6000}
    }
    session={}
    def validate_accno(self,accno):
        if accno in self.users:
            return True
        else:
            return False

    def authenticate(self,**kwargs): #kwargs={"accno":1000,"password"="user1}
        acc_no=kwargs["accno"]
        passw=kwargs["password"]
        valid=self.validate_accno(acc_no)
        if valid==True:
            if passw==self.users[acc_no]["password"]:
                self.session["person"]=acc_no
                #print("login successful")
                return acc_no
            else:
                #print("Incorrect password")
                return -1
        else:
            #print("invalid")
            return 0

    def balance_enquiry(self,accno):
        if self.session["person"]==accno:
            print(self.users[accno]["balance"])
        else:
            print("You must login")


    def fund_transfer(self,user,toacc_no,amount):
        if self.validate_accno(toacc_no):

            if self.users[user]["balance"]<amount:
                print("insufficient balance")
            else:
                self.users[toacc_no]["balance"]=self.users[toacc_no]["balance"]+amount
                self.users[user]["balance"]=self.users[user]["balance"]-amount

    def logout(self):
        self.session["person"]=0




obj=Bank()
person=obj.authenticate(accno=1001,password="user2")    # return either account no or,0,or -1 to person
if (person==0 or person==-1):
    print("Login failed")
else:
    obj.balance_enquiry(person) # if login successful person has the returned accno, so using thet doing balance enquiry

obj.fund_transfer(1000,1001,2000)
obj.balance_enquiry(1001)
obj.logout()


