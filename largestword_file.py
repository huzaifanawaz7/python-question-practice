with open ("sentence.txt","r") as f :
    data=f.read()
    # print(data)

def find_largest_word():
    with open ("sentence.txt","r") as f :
        data=f.read()
        word=""
        largest_word=""

    for ch in range(len(data)):
        if data[ch]!=" " and data[ch]!="\n":
            word+=data[ch]
        else:
            if len(word)>len(largest_word):
                largest_word=word
            word=""
    if len(word)>len(largest_word):
        largest_word=word
    # word=""
    print("so the largest word is ",largest_word)
    print("the length is ",len(largest_word))
find_largest_word()


          
          
              

        
            

         
                 