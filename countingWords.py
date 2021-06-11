name = input("Enter your name :")
print(name)
charecterCount = 0
wordCount = 1
for n in name:
    charecterCount = charecterCount +1
    if(n==' '):
        wordCount = wordCount + 1
print("Number of words in entered string")
print(wordCount)
print("Number of charecters in entered string")
print(charecterCount)