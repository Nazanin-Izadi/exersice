word = str()
words = []
while True:
    word = input("please enter word : ")
    if len(word) != 0:
        words.append(word)
    else:
        break
words.sort()
print(words[-1])