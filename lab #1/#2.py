print("Вводите элемент множетва А. Чтобы остановиться, нажмите j")
A=set()
while True:
    a=input("A: ")
    if a=="j":
        break
    try:
        check=int(a)
        A.add(check)
    except ValueError:
        print("Множество может содержать только целые числа")
        continue
print(f"Множество A - {A}")

print('Вводите элементы для множества В. Когда закончите, введите i')
B=set()
while True:
    b=input("B: ")
    if b=='i':
        break
    try:
        check=int(b)
        B.add(b)
    except ValueError:
        print('Множество содержит целые числа')
        continue
print(f'Множество B - {B}')

formula=(A.union(B))-B
print(f"В результате применения выражения получаем множество - {formula}")
print(f"Напомним, из чего состоит множество A - {A}")
if formula==A:
    print("Равенство выполняется!")
else:
    print("О нет...не может быть...множество не равны")