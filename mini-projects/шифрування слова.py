word = str(input("Ваше слово: "))
w = [""]*len(word)
i = 0
m = 0
k=0
w2 = ""
print("Зашифроване слово: ")
while i<len(word) :
    w[i]=""
    w[i]+=word[i]
    i+=1

while m<len(word):
    w2+=w[len(word)-m-1]
    m +=1
print(w2)