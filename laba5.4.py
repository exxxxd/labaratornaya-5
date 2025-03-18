import random
maxerror = 3
correctanswers = 0
error = 0
while error < maxerror:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    otvet = int(input(f"{num1} + {num2} = "))
    if otvet == num1 + num2:
        print("Правильно!")
        correctanswers += 1
    else:
        print("Ответ неверный")
        error += 1
print(f"Игра окончена. Правильных ответов: {correctanswers}")
