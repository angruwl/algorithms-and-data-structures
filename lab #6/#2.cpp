#include<iostream>
#include<cstdlib>
#include<ctime>
using namespace std;

// очередь на указателях
struct QueueNode{
    int data;
    QueueNode* next;
};

struct Queue{
    QueueNode* front;
    QueueNode* back;
};

Queue createQueue(){
    Queue q;
    q.front=nullptr;
    q.back=nullptr;
    return q;
}

void push(Queue& q, int val){
    QueueNode* newNode= new QueueNode;
    newNode->data=val;
    newNode->next=nullptr;
    if (q.back==nullptr){
        q.front = newNode;
        q.back=newNode;
    }else{
        q.back->next=newNode;
        q.back = newNode;
    }
}

int pop(Queue& q){
    if (q.front==nullptr) return -1;
    int val=q.front->data;
    QueueNode* temp = q.front;
    q.front = q.front->next;
    if (q.front==nullptr) q.back=nullptr;
    delete temp; 
    return val;
}

bool empty(Queue& q){
    return q.front==nullptr;
}

Queue merge(Queue& q1, Queue& q2){
    Queue res= createQueue();
    while(!empty(q1)&&!empty(q2)){
        int a= q1.front->data;
        int b =q2.front->data;
        if(a<=b){
            push(res, pop(q1));
        }else{
            push(res, pop(q2));
        }
    }
    while(!empty(q1)) push(res, pop(q1));
    while(!empty(q2)) push(res, pop(q2));
    return res;
}

struct QueueArr{
    int data[100];
    int size;
};

QueueArr createQueArr(){
    QueueArr q;
    q.size=0;
    return q;
}

void pushArr(QueueArr& q, int val){
    if (q.size>100) return;
    q.data[q.size]=val;
    q.size++;
}

int popArr(QueueArr& q){
    if (q.size==0) return -1;
    int val = q.data[0];
    for( int i = 0;i<q.size-1;i++){
        q.data[i]=q.data[i+1];
    }
    q.size--;
    return val;
}

bool emptyArr(QueueArr& q){
    return q.size==0;
}

QueueArr mergeArr(QueueArr& q1, QueueArr& q2){
    QueueArr res= createQueArr();
    while(!emptyArr(q1)&&!emptyArr(q2)){
        if(q1.data[0]<=q2.data[0]){
           pushArr(res, popArr(q1)); 
        }else{
            pushArr(res, popArr(q2));
        }
    }
    while(!emptyArr(q1)) pushArr(res, popArr(q1));
    while(!emptyArr(q2)) pushArr(res,popArr(q2));
    return res;
}

int main(){
    srand(time(0));
    int size1=rand()%8+3;
    int size2=rand()%8+3;

    int* arr1=new int[size1];
    int* arr2=new int[size2];
    arr1[0]=rand()%5+1;
    for(int i=1; i<size1; i++){
        arr1[i]=arr1[i-1]+rand()*5+1;
    }
    arr2[0]=rand()%5+1;
    for (int i=1; i<size2;i++){
        arr2[i]=arr2[i-1]+rand()%5+1;
    }
    cout<<"Pointer\n";
    Queue q1=createQueue();
    Queue q2=createQueue();
    cout<<"Queue 1: ";
    for(int i=0; i<size1; i++){
        push(q1, arr1[i]);
        cout<<arr1[i]<<" ";
    }
    cout<<endl;
    cout<<"Queue 2: ";
    for(int i=0; i<size2; i++){
        push(q2, arr2[i]);
        cout<<arr2[i]<<" ";
    }
    cout<<endl;

    Queue m=merge(q1, q2);
    cout<<"Result: \n";
    while(!empty(m)){
        cout<<pop(m)<<' ';
    }

    cout<<endl;

    cout<<"Array\n";
    QueueArr qa1=createQueArr();
    QueueArr qa2=createQueArr();
    cout<<"Queue 1: "<<endl;
    for (int i=0; i<size1;i++){
        pushArr(qa1, arr1[i]);
        cout<<arr1[i]<<" ";
    }
    cout<<endl;
    cout<<"Queue 2: ";
    for (int i=0; i<size2; i++){
        pushArr(qa2, arr2[i]);
        cout<<arr2[i]<<' ';
    }
    cout<<endl;
    QueueArr mA=mergeArr(qa1, qa2);
    cout<<"Result: "<<endl;
    while (!emptyArr(mA)){
        cout<<popArr(mA)<<" ";
    }
    delete[] arr1;
    delete[] arr2;
}