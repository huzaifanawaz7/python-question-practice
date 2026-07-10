with open("gpt-practice.txt","r") as f:
    data=f.read()
# print(data)

def find_odd():
    with open("gpt-practice.txt","r") as f:
        data=f.read()
    count=0
    num="" 
    for i in range(len(data)):
        if data[i]==",":
            if int(num)%2!=0:
                count+=1
                num=""
        else:   
            num+=data[i]
    if num!="":
        if int(num)%2!=0:
            count+=1
    print("total odd numbers are in the file ",count)

find_odd()


    