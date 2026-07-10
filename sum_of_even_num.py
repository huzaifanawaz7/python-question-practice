
def find_even():

    num=""
    count=0
    t_sum=0
    with open("gpt-practice.txt","r") as f:
        data=f.read()
    for i in range(len(data)):
        if data[i]==",":
            if int(num)%2==0:
                count+=1
                t_sum+=int(num)
            num="" 
        else:
            num+=data[i]
    if num!="":
        if int(num)%2==0:
            count+=1
            t_sum+=int(num)
    print("the number of even are are re :",count)   
    print("the sum of even numbers are ",t_sum)      

find_even()