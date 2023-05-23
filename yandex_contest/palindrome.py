sentence = [i for i in input().lower() if i.isalnum()]
print(sentence == sentence[::-1])
