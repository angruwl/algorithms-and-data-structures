def count_meet(str):
    count=dict()
    for i in str:
        if i not in count:
            count[i]=0
        count[i]+=1
    single_char=[]
    for key in count:
        if count.get(key)==1:
            single_char.append(key)
    return ",".join(single_char)
while True:
    a=input("Введите строку: ")
    if not a or not len(a)<1:
        print("Недостаточно символов!")
        continue
    if not a[-1]=='.':
        print("Введите строку, которая будет оканчиваться точкой")
        continue
    if not all('a'<=char<='z' for char in a[:-1]):
        print("Введите строку, которая содаржит только маленькие латинские буквы")
        continue
    print(f"Ваша строка - {a[:-1]}")
    break
a=a[:-1]
print(f"В введенной строке один раз встречаются: {count_meet(a)}")
