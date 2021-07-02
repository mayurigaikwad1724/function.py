def factor(number):
    sum=1
    while number>=1:
        sum=number
        number=number+1
        print("factor",sum)               
factor(int(input("enter number")))