import os
import sys
import math
def check_string(line):
    parts=line.split()
    if len(parts)!=3:
        return None
    try:
        sides=[int(part) for part in parts]
        return sides
    except ValueError:
        return None

def this_triangle(sides):
    a,b,c=sorted(sides)
    return a+b>c
    
def perimetr(sides):
    return sum(sides)

def square(sides):
    a,b,c=sides
    p=perimetr(sides)/2
    return int(math.sqrt(p*(p-a)*(p-b)*(p-c)))

file_name=input("Введите имя файла для обработки: ")

if not os.path.exists(file_name):
    print("Файл под таким именем не существует")
    sys.exit(1)
if os.path.getsize(file_name)==0:
    print("у Вашего файла наблюдаются проблемы: он пуст")
    sys.exit(1)

file=open(file_name, "r")
result=open("res1.txt", 'a')
    
for line in file:
    line=line.strip()
    if not line: 
        continue
    sides = check_string(line)
    if sides is not None: 
        if this_triangle(sides):
            result.write(f'Треугольник со сторонами:{sides[0]} {sides[1]} {sides[2]} \
имеет периметр - {perimetr(sides)} и площадь - {square(sides)}\n')
            print('Результат занесен в файл')
        else:
            result.write(f"Треугольник со сторонами: {sides[0]} {sides[1]} {sides[2]} не существует\n")
            print('Результат занесен в файл')

    else: 
        print("Убедитесь, что в строке три числа написаны через пробел")
file.close()
result.close()






    

    
