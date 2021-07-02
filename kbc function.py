#********************************...........KBC...............********************



print("welcome ....to...KBC")
question_list=["know many continents are there?",
"what is the capital of india?",
"NG mai kaun se course padhaya jata hai?",
]
options_list=[["Four","Nine","Seven","Eight"],
["chandhihar","bhopal","chennai","delhi"],
["Softwere Engineering","Counseling","Tourism","Agriculture"]
]
solution_list=[3,4,1]
ans=["3.seven","4.eight","2.bhopal","4.delhi","1.softwere engineering"]
m=0
r=1
g=0
count=0
while m<len(question_list):
    m1=question_list[m]
    print(m1)
    j=0 
    k=m
    while j<len(options_list[m]):
        l=options_list[k][j]
        print(j+1,l)
        j=j+1
    lifeline1=input("Do you want5050 lifeline:")
    if lifeline1=="yes":
        if count==0:
            print(ans[g+m])
            print(ans[g+r])
            n=int(input("enter the answer:"))
            if n==solution_list[m]:
                print("right")
            else:
                print("wrong")
                break
            count=count+1
        else:
            print("you already used lifeline")
            n=int(input("enter answer"))
            if n==solution_list[m]:
                print("right")
            else:
                print("wrong")
    elif lifeline1=="no":
        u=int(input("choose the answer"))
        if u==solution_list[m]:
            print("your answer is correct")
        else:
            print("your answer is wrong")
            break
    else:
        print("error")
    m=m+1
    r=r+1
    g=g+1