class Teacher:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def info(self):
        print(self.name,self.id)

class Subject(Teacher):
    def set(self,subject):
        self.subject=subject
    def info(self):
        print("Subject:",self.subject)

sub=Subject("Sneha",123)
sub.set("English")
sub.info()