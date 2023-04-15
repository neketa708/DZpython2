#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
import random

x = random.randint(0, 1000)
y = random.randint(0, 1000)

sum = x+y
productofnumbers = x*y

for i in range(0, 1000):
    for j in range(0, 1000):
        if i+j == sum and i*j == productofnumbers:
            print('первое число ', i,'второе число ', j)
            break
        else:
            j+=1
    if i+j == sum and i*j == productofnumbers:
        break
    else:
        i+=1

print("значение1",x)
print("значение2",y)
