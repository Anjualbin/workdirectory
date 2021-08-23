

class Person:
    def pvalue(self,name,age):
        self.name=name
        self.age=age

class Child(Person):
    def cvalue(self,address):
        self.address=address
        print(self.name,self.address)

class student(Child):
    def info(self):
        print(self.name)
        print(self.address)
ch=Child()
ch.pvalue("Anu",12)
ch.cvalue("ert")

st=student()
st.pvalue("anju",15)
st.cvalue("abc")
st.info()