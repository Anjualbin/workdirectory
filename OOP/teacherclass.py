class Teacher:
    school="Bishop cotton high school"
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
    def info(self):
        print("Name:",self.name)
        print("Subject:",self.subject)
        print("School:",Teacher.school)

tea1=Teacher("Anu","Physics")
tea1.info()