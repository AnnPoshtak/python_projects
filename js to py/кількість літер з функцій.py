def getTextFromUser () :
    t = str(input("Введіть речення"))
    return t
def countLettersFrequency (r):
    index =0
    code=0
    a=[0]*26
    i = 0
    while i<len(r):
        code = ord(r[i])
        if code >= 65 and code <= 90 :
            index = code - 65
            a[index]+=1
        elif code >= 97 and code <= 122:
            index = code - 97
            a[index] +=1
        i+=1
    return a
def creatArrayEnglishLetters () :
    l = [""]*26
    i = 0
    while i<26:
        l[i]=chr(65+i)
        i+=1
    return l
def  sort (array_words_frequency, arrayLetters):
    s1 = ""
    s2 = ""
    i = 0
    m = 0
    while i<len(array_words_frequency):
        m = 0
        while m<len(array_words_frequency)-1:
            if array_words_frequency[m] < array_words_frequency[m + 1]:
                s1 = array_words_frequency[m]
                array_words_frequency[m] = array_words_frequency[m + 1]
                array_words_frequency[m + 1] = s1
                s2 = arrayLetters[m]
                arrayLetters[m] = arrayLetters[m + 1]
                arrayLetters[m + 1] = s2
            m+=1
        i+=1

def drawTable (array_words_frequency, arrayLetters):
    i = 0
    while i<26:
        if array_words_frequency[i] > 0:
            print(str(arrayLetters[i] )+ " - " + str(array_words_frequency[i]))
        i+=1
def main():
    r = getTextFromUser()
    print("Введене речення: " + r)
    array_words_frequency = countLettersFrequency(r)
    arrayLetters = creatArrayEnglishLetters()
    sort(array_words_frequency, arrayLetters)
    drawTable(array_words_frequency, arrayLetters)

main()