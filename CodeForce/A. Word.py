word = input()

countlow = 0
countupp = 0
for i in word:
    if i.islower():
        countlow += 1
    if i.isupper():
        countupp += 1

if countlow >= countupp:
    print(word.lower())


if countupp > countlow:
    print(word.upper())