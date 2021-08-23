class Employee():
    empl = {}
    f1=open("info","r")
    for i in f1:
        dict = {}
        lst=i.split(",")
        dict["id"]=lst[0]
        dict["name"]=lst[1]
        dict["desig"]=lst[2]
        dict["no"]=lst[3]
        dict["salary"]=lst[4].rstrip()
        empl.update({lst[0]:dict})

    def prop_value(self,eid,**kwargs):
        if eid in Employee.empl.keys():
            print(Employee.empl[eid]["name"])
            for arg in kwargs.values():
                print(Employee.empl[eid][arg])
        else:
            print("invalid id")




emp=Employee()
emp.prop_value("1001")
emp.prop_value("1002",prop="salary")



