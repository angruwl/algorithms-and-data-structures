import time
import random
import matplotlib.pyplot as plt

def linearSearch(arr, num):
    cmp=0
    first_enter=-1
    for i in range(len(arr)):
        cmp+=1
        if arr[i]==num:
            return cmp
    return cmp


def linearSearchWithBarier(arr, num):
    cmp=0
    arr.append(num)
    i=0
    while True:
        cmp+=1
        if arr[i]==num:
            break
        i+=1
    arr.pop()
    if i==len(arr)-1:
        return cmp
    return cmp

def BinarySearch(arr, num):
    cmp=0
    first=0
    last=len(arr)-1
    index=-1
    while(first<=last) and (index==-1):
        cmp+=1
        mid=(first+last)//2
        if arr[mid]==num:
            index=mid
        else:
            if num<arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return cmp

def randomArray(size):
    return [random.randint(-100,100) for _ in range(size)]

sizes=[20, 500, 1000, 3000, 5000, 10000]
n=100

linear_times=[]
linear_cmp=[]
barier_times=[]
barier_cmp=[]

for size in sizes:
    array = randomArray(size)

    t_lin=[]
    c_lin=[]
    t_br=[]
    c_br=[]

    for i in range(n):
        elem=random.choice(array)

        start=time.perf_counter()
        res_l = linearSearch(array.copy(), elem)
        t_lin.append((time.perf_counter()-start)*1000000)
        c_lin.append(res_l)

        start=time.perf_counter()
        res_b=linearSearchWithBarier(array.copy(), elem)
        t_br.append((time.perf_counter()-start)*1000000)
        c_br.append(res_b)
    linear_times.append(sum(t_lin)/n)
    linear_cmp.append(sum(c_lin)/n)
    barier_times.append(sum(t_br)/n)
    barier_cmp.append(sum(c_br)/n)

print("linear_cmp =", linear_cmp)
print("barier_cmp =", barier_cmp)

fig, (ax1, ax2)=plt.subplots(1,2, figsize=(14,5))
ax1.plot(sizes, linear_times,'o-', label='Линейный поиск', color="green", linewidth=2, markersize=8)
ax1.plot(sizes, barier_times, 's-', label="Поиск с барьером", color="orange", linewidth=2, markersize=8)
ax1.set_xlabel("Размер массива", fontsize=12)
ax1.set_ylabel("Сред. время(мкс)", fontsize=12)
ax1.legend(fontsize=10)
ax2.plot(sizes, linear_cmp, 'o-', label="Линейный поиск", color = 'blue', linewidth=2, markersize=8)
ax2.plot(sizes, barier_cmp, 's-', label="Поиск с барьером", color='pink', linewidth=2, markersize=8)
ax2.set_xlabel("Размер массива", fontsize=12)
ax2.set_ylabel("Сред. кол-во сравнений", fontsize=12)
ax2.legend(fontsize=10)
plt.tight_layout()
plt.savefig("task1.png", dpi=300)
plt.show()

for size in sizes:
    array=randomArray(size)

    time_l=[]
    time_br=[]

    for i in range(n):
        elem = array[0]

        start=time.perf_counter()
        linearSearch(array, elem)
        time_l.append((time.perf_counter()-start)*1000000)

        start=time.perf_counter()
        linearSearchWithBarier(array, elem)
        time_br.append((time.perf_counter()-start)*1000000)
    avg_lin=sum(time_l)/len(time_l)
    avg_br=sum(time_br)/len(time_br)
    print()
    print(f"Для размера {size} среднее время выполнения в ЛУЧШЕМ случае \n линейного - {avg_lin}, линейного с барьером - {avg_br}\n")

for size in sizes:
    array=randomArray(size)

    time_l=[]
    time_br=[]

    for i in range(n):
        elem = array[-1]

        start=time.perf_counter()
        linearSearch(array, elem)
        time_l.append((time.perf_counter()-start)*1000000)

        start=time.perf_counter()
        linearSearchWithBarier(array, elem)
        time_br.append((time.perf_counter()-start)*1000000)
    avg_lin=sum(time_l)/len(time_l)
    avg_br=sum(time_br)/len(time_br)
    print()
    print(f"Для размера {size} среднее время выполнения в ХУДШЕМ случае \n линейного - {avg_lin}, линейного с барьером - {avg_br}\n")

#сравнение линейного и двоичного поиска 
# элемент присутствует
for size in sizes:
    array=randomArray(size)
    array.sort()
    
    t_lin=[]
    c_lin=[]
    t_bin=[]
    c_bin=[]

    for i in range(n):
        elem=random.choice(array)

        start=time.perf_counter()
        comp=linearSearch(array, elem)
        t_lin.append((time.perf_counter()-start)*1000000)
        c_lin.append(comp)

        start=time.perf_counter()
        comp=BinarySearch(array, elem)
        t_bin.append((time.perf_counter()-start)*1000000)
        c_bin.append(comp)
    avg_t_lin=sum(t_lin)/n
    avg_c_lin=sum(c_lin)/n
    avg_t_bin=sum(t_bin)/n
    avg_c_bin=sum(c_bin)/n

    print(f"Для размера {size} \n среднее время линейного поиска - {round(avg_t_lin,2)}, среднее время бинарного поиска - {round(avg_t_bin,2)}\n среднее число сравнений линейного поиска - {round(avg_c_lin,2)}, бинарного поиска - {round(avg_c_bin,2)}")
    print() 