#include <iostream>
#include <locale.h>
#include <random>
using namespace std;

int* segment1=new int [8];
int* segment2=new int [50];


random_device rd;
mt19937 gen(rd());
uniform_int_distribution <> distrib (-50, 50);
void NewPointer(int** p, int byte){
    int flag=0;
    if (8 < byte){
        cout<<"В сегменте 1 недосаточно места."<<endl;
    }
    else{
        *p = segment1;
        for (int i=0; i<byte; i++){
            *(segment1+i)=distrib(gen);
        }
        flag=1;
        cout<<"Массив создан в сегменте 1, его размер - "<<byte<<endl;
    }
    if (50 < byte){
        cout<<"В сегменте 2 недосаточно места.";
    }
    else if(flag==0){
        *p=segment2;
        for (int i=0; i<byte; i++){
            *(segment2+i)=distrib(gen);
        }
    cout<<"Массив создан в сегменте 2, его размер - "<<byte<<endl;
    }  
}

void WritePointer(int* p, int value){
    *p=value;
}

int ReadPointer(int* p){
    if (p!=nullptr){
        return *p;
    }
    else{
        cout<<"Указатель пуст :(";
        return 0;
    }
}

void SetPointer(int* p,int* b){
    *p = *b;
}

void FreePointer(int* p){
    if (p==segment1){
        delete[] segment1;
        p=nullptr;
    }
    else if(p==segment2){
        delete[] segment2; 
        p=nullptr;
    }

}
int CheckSize() {
    int value;
    cout << "Введите положительное число: ";
    cin >> value;
    
    while (cin.fail() || value <= 0) {
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cout << "Ошибка! Введите целое положительное число: ";
        cin >> value;
    }
    
    return value;
}

 
int main(){
    setlocale(LC_ALL, "rus");
    cout<<"Определяем первый массив"<<endl;
    int size1=CheckSize();
    
    int* array1=nullptr;
    NewPointer(&array1, size1);
    int product_negative=1;
    int count_negative=0;
    for (int i=0; i<size1; i++){
        cout<< i+1 <<"элемент массива = "<< ReadPointer(array1+i)<<endl;
        if (ReadPointer(array1+i)<0){ 
            product_negative*= ReadPointer(array1+i);
            count_negative+=1;
        }
    if (count_negative==0){
        product_negative=0;
    }
        
    }
    cout<<"Произведние отрицательных элементов массива =  "<<product_negative<<endl;

    
    cout<<"Определим второй массив"<<endl;
    int size2=CheckSize();
    int* array2=nullptr;
    NewPointer(&array2, size2);
    int max_value=-100;
    for (int i=0; i<size2; i++){
        cout<< i+1 <<" элемент массива = "<< ReadPointer(array2+i)<<endl;
        if (ReadPointer((array2+i))>=max_value){
            max_value=ReadPointer(array2+i);
        }
    }
    cout<<"Максимальный элемент в массиве = "<<max_value<<endl;
    FreePointer(array1);
}