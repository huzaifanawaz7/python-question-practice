with open("gpt-practice.txt","w+") as f :
    f.write("1,2,34,56,56,456,6,7654,45,555")
    data=f.read()
with open("gpt-practice.txt","r") as f:
    data=f.read()
    # print(data)

# find all the even numbers from the file 

def find_even():

    num=""
    count=0
    with open("gpt-practice.txt","r") as f:
        data=f.read()
    for i in range(len(data)):
        if data[i]==",":
            if int(num)%2==0:
                count+=1
                num="" 
        else:
            num+=data[i]
    if num!="":
        if int(num)%2==0:
            count+=1
    print("the number of even are :",count)         

find_even() 