# Multiple inheritance  -- inherit a class from two parent classes

class Person:
    def pvalue(self,name,age):
        self.name=name
        self.age=age

class Child:
    def cvalue(self,address):
        self.address=address

class student(Person,Child):
    def info(self):
        print(self.name)
        print(self.address)

st=student()
st.pvalue("Anu",12)
st.cvalue("abc")
st.info()
