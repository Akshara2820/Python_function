# return function

def add(a,b):
    c=a+b
    return c
    x=int(input("enter 1st no :"))
    y=int(input("enter 2nd no :"))
sm=add(18,20)
print(sm)

# question =6

def driver(speed):
    if speed<70:
        return "ok"
    else:
        if speed>70:
            point=(speed-70)//5
            if point>12:
                return "License suspended"
            return point

N=int(input("enter no :"))
print(driver(N))


# question =8

def func(N):
    dict={}
    for i in range(1,N+1):
        dict[i]=i**2
    return dict

Number=int(input("enter no :"))
print(func(Number))


# question code spnit=2

def prime_no(num):
    if num>1:
        a=2
        while a<num:
            if num%a==0:
                print(num,"not prime no.")
                break
            a+=1
        else:
            print(num,"prime no.")
    else:
        print(num,"not prime no.")
num=int(input("enter no :"))
prime_no(num)


# become a programer
# question=1

def name(a):
    i=0
    while i<a:
        print("ek baar")
        i+=1
name(5)


# question=8

def number(a):
    d={}
    i=0
    while i<a:
        n=int(input("enter no= :"))
        j=1
        s=[]
        while j<=n:
            s.append(j)
            j+=1
        d[n]=s
        i+=1
    return d
        
num=int(input("enter no=="))
print(number(num))


# question=2
# main cofounder hu

def print_line(a,b):
    print(a,b,sep="\n")
print_line("mera name Rishabh hai "," main Navgurukul ka Co-Founder hu")

# question=4
# part=1

def number(num1,num2):
    print(num1+num2)
number(56,12)

# part=2

def add_number():
    a=[50,60,10]
    b=[10,20,13]
    i=0
    l=len(a)
    while i<l:
        s=a[i]+b[i]
        print(s)
        i+=1
add_number()


# question=5
# part=1

def check_number(num1,num2):
    if num1%2==0 and num2%2==0:
        return("both are even")
    else:
        return("both are not even")
n=int(input("enter no :"))
n1=int(input("enter no :"))
print(check_number(n,n1))

# part=2

def check_number_list():
    list1=[2, 6, 18, 10, 3, 75]
    list2=[6, 19, 24, 12, 3, 87]
    i=0
    l=len(list1)
    while i<l:
        if list1[i]%2==0 and list2[i]%2==0:
            print("both are even")
        else:
            print("both are not even")
        i+=1
check_number_list()


# question=6
# part=1

def calculator(num1,num2,operation):
    if operation=="add":
        return(num1+num2)
    elif operation=="sub":
        return(num1-num2)
    elif operation=="multiply":
        return(num1*num2)
    elif operation=="divied":
        return(num1/num2)
    else:
        print("please write correct operation")
n=int(input("enter no :"))
n1=int(input("enter no :"))
n2=input("enter operation:")
print(calculator(n,n1,n2))

# part=2

def calculator(num1,num2,operation):
    if operation=="add":
        add_result=num1+num2
        return(add_result)
    elif operation=="sub":
        sub_result=num1-num2
        return(sub_result)
    elif operation=="multiply":
        multiply_result=num1*num2
        return(multiply_result)
    elif operation=="divied":
        divied_result=num1/num2
        return(divied_result)
    else:
        return("enter correct operation")

n=int(input("enter no :"))
n1=int(input("enter no :"))
n2=input("enter operation :")
print(calculator(n,n1,n2))

# part=3

def list_change():
    list1=[5, 10, 50, 20]
    list2=[2, 20, 3, 5]
    i=0
    s=[]
    l=len(list1)
    while i<l:
        s.append(list1[i]*list2[i])
        i+=1
    print(s)
list_change()


def first_function():
    s = "I love India"
    def second_function():
        a= "MY NAME IS JACK"
        print(a)
             
    second_function()
    print(s)
first_function() 

        
        
def name(name):
    return(name)
    def name2(name1):
        return(name2)
    print(name2("mishra"))
    print(name)
name("akshra")



