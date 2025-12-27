age = int(input("Enter the Age:"))
match age:
    case _ if(age<=5 and age >=0):
        print("Free Entry")
    case _ if(age>5 and age<=18):
        print("50")
    case _ if(age>18 and age <=70):
        print("100")
    case _ if(age>50 and age<100):
        print("Free Entry")
    case _ :
        print("Please Enter valid age")