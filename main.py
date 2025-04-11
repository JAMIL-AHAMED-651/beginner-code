#Variable and Data Type
name="Jamil Ahamed"
age=24
student=True
print(f"Data type of name {type(name)} age {type(age)} student {type(student)}")
#Arithmatic operation
n=3
print(f"summation {age+n} subs {age-n} mul {age*n} div {age/n} ")
#Comparison operator
if age==18:
    print("You should have an ID card ")
elif age>18:
    print("DO marry")
else:
    print("Hey baby,Go to school")
#Logical operator
if age==24 and name=="Jamil Ahamed":
    print(f"{name} is our current student")
elif age==24 or name=="Jamil Ahamed":
    print("Give complete info")
else :
    print("No student found")
#Assignment Operator
value=int(input("Enter value"))
for _ in range(1):
    value+=1
print(f"Next value {value}")
value=int(input("Enter value"))
for _ in range(1):
    value-=1
print(f"previous value {value}")
value=int(input("Enter value"))
for _ in range(1):
    value*=value
print(f"Square of value {value}")
value=int(input("Enter value"))
for _ in range(1):
    value/=1
print(f"same value {value}")
#Identity operator
name1="Juwel"
if name is not age:
    print("Name is not age")
if type(name) is type(name1):
    print(f"Both are string")
#Membership operator
students=["jamil","Juwel","Sabbir","Shishir"]
student=input("Enter name :")
if student in students:
    print("He is a student")
elif student not in students:
    print(f"{student} is not our student")