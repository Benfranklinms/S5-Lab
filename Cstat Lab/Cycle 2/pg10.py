#count vowels, consonants, words and "?"

def check(text):
    vowels = "aeiouAEIOU"
    v = 0
    c = 0
    w = 0
    q = 0

    for ch in text:
        if ch in  vowels:
            v += 1
        elif ch.isalpha():
            c += 1
        elif ch == "?":
            q += 1
        else:
            print("Not specified")

        w = len(text.split())

    return v, c, w, q


text = input("Enter a text : ")
v, c, w, q = check(text)
print("Vowels : ", v)
print("Characters : ", c)
print("Words : ", w)
print("Question mark : ", q)
            
