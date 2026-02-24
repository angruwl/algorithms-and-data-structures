import random
while True:
    n=input("Введите цeлочисленный размер массива: ")
    if len(n)==0:
        print ("Недопустимое значение")
        continue
    if  not n.isdigit():
        print("Значение не является корректным")
        continue
    if n=="0":
        print("Массив не может быть пустым")
        continue
    n=int(n)
    break

randoms_num=[random.uniform(0.0,100.0) for i in range(n)]

file=open("test2.txt", 'w')
for i in range (n):
    file.write(f'{randoms_num[i]}\n')
print("Числа записаны в файл")
file.close()
file_again=open('test2.txt')
data=[float(line) for line in file_again]
middle_sum=sum(data)/len(data)
count=0
print(f'Среднее арифметическое чисел в массиве - {middle_sum}')
print("Ниже выведены значения, меньшие среднеафриметического")
for i in range(len(data)):
    if data[i]<middle_sum:
        print(data[i])
        count+1
print(f"Чисел меньше среднеарифметического - {count}")


