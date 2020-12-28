# question=1

def calculate_sum(a,b):
    sum = a+b
    print(sum)
calculate_sum(4,5)


# question=2

def multi(a,b):
    multiply=a*b
    return multiply
print(multi(3,4))


# question=3

def Avg(number1,number2,number3):
    avg=number1+number2+number3/3
    print(avg)
Avg(1,3,2)

# question=4

def voter(age):
    if age > 18:
        print("eligible")
    else:
        print("not eligible")
voter(20)


# question=5

def distance(kms):
        if kms < 20:
            print("close")
        elif kms < 50:
            print("median")
        else:
            Print("far")
distance(20) 


# question=6

def welcome():
    print("Welcome to function")
welcome()


# question=7

def sum():
    print(12+13)
sum() 

# question=8

def isEven():
    if(12%2==0):
        print("Even Number")
    else:
        print("Old Number") 
isEven()

# question=9

def greet(*names):
    for name in names:
        print("Welcome", name)


greet("Rinki", "Vishal", "Kartik", "Bijender")

# question=10

def info(name, age = "16"):
   print(name + " is " + age + " years old")

info("Sonu")
info("Sana", "17")
info("Umesh", "18") 


# question=11

def studentDetails(name,currentMilestone,mentorName):
    print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)

studentDetails("Akshara","Function","Manisha") 
