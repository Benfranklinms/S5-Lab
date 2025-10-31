file = open("sample.txt", "r")
text = file.read()
file.close()

characters = len(text)
word = len(text.split())
sentences = text.count(".") + text.count(",") + text.count("?")

print("characters : ", characters)
print("Words : ", word)
print("Sentences : ", sentences)

