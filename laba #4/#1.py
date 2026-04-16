import random
import copy
import time
#сортировка прямыми включениями
def insertionSort(arr):
    iterations=0
    comparisons=0
    permutations=0
    start = time.perf_counter()
    for i in range (1,len(arr), 1):
        iterations+=1
        value=arr[i]
        index = i
        while (index>0 and arr[index-1]>value):
            comparisons+=1
            arr[index]=arr[index-1]
            permutations+=1
            index-=1
        if index>0:
            comparisons+=1
        arr[index] = value
    end=time.perf_counter()
    time_ms=(end-start) * 1000
    return {
        'iterations': iterations,
        'comparisons': comparisons,
        'permutations': permutations,
        'time': time_ms
    }
def insertionSortForTask(arr):
    for i in range (1,len(arr)):
        value=arr[i]
        index = i
        while (index>0 and arr[index-1]<value):
            arr[index]=arr[index-1]
            index-=1
        arr[index] = value
    return arr

#сортировка прямым выбором
def selectionSort(arr):
    iterations=0
    comparisons=0
    permutations=0
    start=time.perf_counter()
    for i in range(0, len(arr)-1, 1):
        iterations+=1
        min=i
        for j in range(i+1, len(arr), 1):
            comparisons+=1
            if arr[j]<arr[min]:
                min=j
        temp = arr[i]
        arr[i]=arr[min]
        arr[min]=temp
        permutations+=1
    end=time.perf_counter()
    time_ms=(end - start)*1000
    return {
        'iterations': iterations,
        'comparisons': comparisons,
        'permutations': permutations,
        'time':time_ms
    }

#сортировка прямым обменом
def bubbleSort(arr):
    iterations=0
    comparisons=0
    permutations=0
    start=time.perf_counter()
    for i in range(0,len(arr)-1, 1):
        iterations+=1
        for j in range(len(arr)-1, i, -1):
            comparisons+=1
            if arr[j-1]>arr[j]:
                temp=arr[j-1]
                arr[j-1]=arr[j]
                arr[j]=temp
                permutations+=1
    end=time.perf_counter()
    time_ms=(end-start) * 1000
    return {
        'iterations': iterations,
        'comparisons': comparisons,
        'permutations': permutations,
        'time':time_ms
    }
    
#быстрая сортировка
def quickSort(arr):
    iterations=0
    comparisons=0
    permutations=0
    start=time.perf_counter()
    def canISort(left, right):
        nonlocal iterations, comparisons, permutations
        if left>=right:
            return 
        i=left
        j=right
        pivot=arr[left]
        while (i<j):
            iterations+=1
            while(arr[j]>pivot and i<j):
                comparisons+=1
                j-=1
            comparisons+=1
            if (i != j):
                arr[i]=arr[j]
                i+=1
                permutations+=1
            while (arr[i]<pivot and i<j):
                comparisons+=1
                i+=1
            comparisons+=1
            if (i!=j):
                arr[j]=arr[i]
                j-=1
                permutations+=1
        arr[i] = pivot
        index=i
        canISort(left, index-1)
        canISort(index+1, right)
    canISort(0, len(arr)-1)
    end=time.perf_counter()
    time_ms=(end-start) * 1000
    return {
        'iterations': iterations,
        'comparisons': comparisons,
        'permutations': permutations,
        'time':time_ms
    }

def random_array(n):
    return [random.randint(-100, 100) for _ in range(n)]

def array_sorted(n):
    return list(range(1, n+1))

def array_reverced(n):
    return list(range(n, 0, -1))

def array_partially(n, p):
    arr=list(range(1, n+1))
    border = int(n*p / 100)
    tail= arr[border:]
    random.shuffle(tail)
    return arr[:border]+ tail
    
def check_size():
    while True:
       size=input("Введите размер массива для анализа сортировок при различных состояниях: ")
       if len(size)==0:
        print('Пустовато...')
        continue
       if size[0]=='-':
           print('Введите положительное число')
           continue
       if not size.isdigit():
           print('Надо целое число')
           continue
       if int(size)==0:
           print('Массив не может быть пустым')
           continue
       return int(size)

methods={
    'Прямое включение': insertionSort,
    'Прямой выбор': selectionSort,
    'Прямой обмен': bubbleSort,
    'Быстрая': quickSort
}
size=[20, 500, 1000, 3000, 5000, 10000]
res_1={}
for s in size:
    array=random_array(s)
    res_1[s]={}
    for name, func in methods.items():
        sort_array=func(array.copy())
        res_1[s][name]={
            'итерации': sort_array['iterations'],
            'сравнения': sort_array['comparisons'],
            'перестановки': sort_array['permutations'],
            'время':sort_array['time']
        }
    for m in methods.keys():
        print(f"Размер массива: {s}\n")
        iter=res_1[s][m]['итерации']
        cmp=res_1[s][m]['сравнения']
        prm=res_1[s][m]['перестановки']
        t=res_1[s][m]['время']
        print(f'{m}:итерации = {iter}, сравнений = {cmp}, перестановок = {prm}, время = {t}')
        print()


state=['Random', 'Sorted', 'Reversed', '25 Sorted', '50 Sorted', '75 Sorted']
n=check_size()
arrays={
    'Random':random_array(n),
    'Sorted':array_sorted(n),
    'Reversed':array_reverced(n),
    '25 Sorted':array_partially(n, 25),
    '50 Sorted':array_partially(n, 50),
    '75 Sorted':array_partially(n, 75)
}
res_2={}
for st in state:
    res_2[st]={}
    for name, func in methods.items():
        array_res=func(arrays[st].copy())
        res_2[st][name]={
            'итерации': array_res['iterations'],
            'сравнения': array_res['comparisons'],
            'перестановки': array_res['permutations'],
            'время':array_res['time']
        }
for st in state:
    print(f"Состояние массива: {st}\n")
    for m in methods.keys():
        iter=res_2[st][m]['итерации']
        cmp=res_2[st][m]['сравнения']
        prm=res_2[st][m]['перестановки']
        t=res_2[st][m]['время']
        print(f'{m}:итерации = {iter}, сравнений = {cmp}, перестановок = {prm}, время = {t}')
        print()

#еще почитать
array_for_negative=random_array(20)
negatives=[]
index=[]
for i in range(0, 20):
    if array_for_negative[i]<0:
        negatives.append(array_for_negative[i])
        index.append(i)
s_negatives=insertionSortForTask(negatives)
result=array_for_negative.copy()
for i, value in zip(index, s_negatives):
    result[i]=value
print(f'Изначальный массив: {array_for_negative}')
print(f'Результирующий: {result}')