AllZeichen = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '§', '$', '%', '&', '/', '(', '[', '=', '?', '@', '€', '+', '*', '#', '-', '_', ':', ',', ';', '<', '>', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú', 'â', 'ê', 'î', 'ô', 'û', 'Â', 'Ê', 'Î', 'Ô', 'ß', ' ',"ö","Ö","ä","Ä","ü","Ü"]
print(len(AllZeichen))


def write(inputText,key):
    inputText = list(inputText)
    key = list(key)
    emptyList = []
    emptyWord = ""
    for Buchstabe in inputText:
        if Buchstabe in AllZeichen:
            index = AllZeichen.index(Buchstabe)
            emptyList.append(key[index])
        else:
            print("Fehler bei dem Buchstaben " + Buchstabe)
    emptyWord = emptyWord.join(emptyList)
    print(emptyWord)
    return emptyWord

#Test
#key = "kpB:YE9rf*xbQyV17,2siC>?$4%=P+/zlv3j-u6OAhG[aFZ#mcd&WLHJ0X<oI_q€M;(@!NUweRSn"
#write("ES FUNKTIONIERT schon sehr gut, aber es ist noch nicht so PERFEKT & naja", key)
