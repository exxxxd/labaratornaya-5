result = ""
while True:
    word = input()
    if word == "stop":
        break
    if result:
        result += " "
    result += word
print(result)
