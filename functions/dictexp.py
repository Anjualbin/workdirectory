dict={
    1000:{"eid":1000,"name":"Amal","salary":25000,"Designation":"Developer"},
    1001:{"eid":1001,"name":"Akhil","salary":35000,"Designation":"Developer"},
    1002:{"eid":1002,"name":"Albin","salary":25000,"Designation":"Tester"},
    1003:{"eid":1003,"name":"Sneha","salary":32000,"Designation":"Analyst"},
    }

print(dict[1002]["name"])
print(dict[1002]["Designation"])

id=int(input("Enter the id:"))
value = input("Enter the detail that you want, available options are:eid,name,salary,Designation:")
if id in dict and value in dict[id]:
    print(dict[id][value])
else:
    print("Invalid id or property")

