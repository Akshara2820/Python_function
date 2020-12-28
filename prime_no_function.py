# def prime_no(num):
#     if num>1:
#         a=2
#         while a<num:
#             if num%a==0:
#                 print(a,"not prime no.")
#                 break
#             a+=1
#         else:
#             print(a,"prime no.")
#     else:
#         print(num,"not prime no.")
# num=int(input("enter no :"))
# prime_no(num)

a="akshara"
l=len(a)
b=" "
while l>0:
    b=(a[l-1])
    l-=1
    print(b)