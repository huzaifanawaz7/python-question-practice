with open("sentence.txt","r") as f :
    data=f.read()
# print (data) 
def frequency1():
    with open("sentence.txt","r") as f :
        data=f.read()
        word=""
        frequency={}
    for i in range(len(data)):
        if data[i] !="\n":
            word+=data[i]
        else:
            if word in frequency:
                frequency[word]+=1
            else:
                frequency[word]=1
            word=""
    if word!="":
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
    print("the frequency of the words are ")
    for i in frequency:
        print (i," : ",frequency[i])

frequency1()






                    





        # for j in range(data):

        #     if data[i]!="\n":
        #         word+=data[i]
        # else:

