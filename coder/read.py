AllZeichen = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","p","Q","R","S","T","U","V","W","X","Y","Z", 1,2,3,4,5,6,7,8,9,0,"!",'"',"§","$","%","&","/","(",")","=","?","`","*","+","#","-","_",":",";","<",">","|","{","}","[","]","\\","~","^","°","²","³","@","€","µ","£","'",".",","," "]


def read(inputText, key):
    inputText = list(inputText)
    key = list(key)
    emptyList = []
    emptyWord = ""
    for Buchstabe in inputText:
        if Buchstabe in key:
            index = key.index(Buchstabe)
            emptyList.append(AllZeichen[index])
        elif str(Buchstabe.lower()) in key:
            index = key.index(str(Buchstabe.lower()))
            emptyList.append(AllZeichen[index]) 
        else:
            print("Fehler bei dem Buchstaben " + Buchstabe)
            print("WRONG KEY")
            return "WRONG KEY"

    emptyWord = emptyWord.join(emptyList)
    print(emptyWord)
    return emptyWord

#Test
key = ">ZQiK1TdRMU#8vu:7!*P[2eF_&n5%mjXHy-a$Ob?VCgh@l(sBf0A€LqYxwrSDGN;,Jc<9t4o/=E§"

read("na>+l3_SOP3On&S>aDeP3>ane&>1lSx>!gn&>na>OaS>3PDe>3ODeS>aP>kn&+n_S>(>3!L!", key)