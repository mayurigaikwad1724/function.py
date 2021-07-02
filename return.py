# def even_odd(n):
#     if n%2==0:
#         return "it is even number"
#     else:
#         return "it is odd number"
# num=int(input("enter the number"))
# r=even_odd(num)
# print(r)

#####
def menu(day):
    if day == "monday":
        return "Butter Chicken"
    elif day == "tuesday":
        return "Mutton Chaap"
    elif day == "wednesday":
        return "matar panir"
    else:
        return "Chole Bhature"

    print ("Kya main print ho payungi? :-(")

mon_menu = menu("monday")
print (mon_menu)
tues_menu = menu("tuesday")
print (tues_menu)
wed_menu = menu("wednesday")
print (wed_menu)
fri_menu = menu("friday")
print (fri_menu) 