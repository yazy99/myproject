#------------------------------------1---------------------------------

stuff=[-7, 5/6, True,None, [5,8], "Beautiful", {"books": "Lolita", "Author": "Nabokov"},(3,8)]
for i, val in enumerate (stuff,1):
    print(f"{i}){val}-{type(val)}")

#------------------------------------2-----------------------------------

stuff = input("-1-0-1"). split()
for i in range (1, len(stuff), 2):
    stuff[i-1], stuff[i]=stuff[i], stuff[i-1]
print(stuff)

#------------------------------------3----------------------------------

seasons = {"осень":[9,10,11],"зима":[12,1,2],"весна":[3,4,5],"лето":[6,7,8]}
mounts=int(input('номер месяца: '))
if mounts in sum(seasons.values(),[]):
    for i in season.items():
        if mounts in i [1]:
            print(i[0])
            break

#----------------------------------4------------------------------------

text = input("enter text : ")
T = text.split()
for x, y in enumerate (T, start=1) :
    if len(y) > 11 :
        y = y[:10]
        print(x, y)
    else :
        print (x,y)

#---------------------------------5-----------------------------------

rate_list = [7, 5, 3, 3, 2]
frq = int(input("How many rates do you want to add?\n\t ENTER QUANTITY: "))
for j in range(frq):
    add_new = int(input("What's rate do you want to add?\n\t ENTER RATE: "))
    if add_new in rate_list:
        i = rate_list.index(add_new)
        while (i + 1) <= (len(rate_list) - 1) and (rate_list[i] == rate_list[i + 1]):
            i += 1
        rate_list.insert(i, add_new)
        print(f"Updated rate_list {rate_list}")
    else:
        if add_new <= rate_list[-1]:
            rate_list.append(add_new)
            print(f"Updated rate_list {rate_list}")
        else:
            rate_list.insert(0, add_new)
            print(f"Updated rate_list {rate_list}")




