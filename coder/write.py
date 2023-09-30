AllZeichen = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","p","Q","R","S","T","U","V","W","X","Y","Z", 1,2,3,4,5,6,7,8,9,0,"!",'"',"§","$","%","&","/","(",")","=","?","`","*","+","#","-","_",":",";","<",">","|","{","}","[","]","\\","~","^","°","²","³","@","€","µ","£","'",".",","," "]
print(len(AllZeichen))

def write (inputText,key):
    inputText = list(inputText.upper())
    key = list(key)
    emptyList = []
    for Buchstabe in inputText:
        if Buchstabe in AllZeichen:
            index = AllZeichen.index(Buchstabe)
            emptyList.append(key[index])
        elif str(Buchstabe.lower()) in AllZeichen:
            index = AllZeichen.index(Buchstabe.lower())
            emptyList.append(key[index]) 
        else:
            print("Fehler bei dem Buchstaben " + Buchstabe)
    print(inputText)
    print(emptyList)


Key = "uk?:jyYelbNFZ{=[;ET-n]€c§QizvsWUMxDd#JI_)/V}tLq$go+<*pK(>HaX%RhAr!m&fOGPCSw,"
write("Hallo",Key)