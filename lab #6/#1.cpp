#include <iostream>
#include <cstdlib>  
#include <ctime>
using namespace std;

// задание 1 через указатели
struct Node{
    int data;
    Node* next;
};

Node* createListN(){
    return nullptr;
}

Node* addElemN(Node* head, int val){
    Node* newNode = new Node;
    newNode->data=val;
    newNode->next=nullptr;

    if (head==nullptr){
        return newNode;
    }
    Node* current=head;
    while(current->next != nullptr){
        current=current->next;
    }
    current->next = newNode;
    return head;
}

Node* removeElemN(Node* head, int val){
    Node* current = head;
    Node* previous = nullptr;
    while(current!=nullptr){
        if (current->data == val){
            if (previous==nullptr){
                head=current->next;
            }else{
                previous->next=current->next;
            }
            delete current;
            return head;
        }
        previous=current;
        current=current->next;
    }
    cout<<"Not found"<<endl;
    return head;
}

Node* duplicateN(Node* head){
    if(head==nullptr){
        return nullptr;
    }
    Node* current = head;

    while(current!=nullptr){
        if (current->data % 2 !=0){
            Node* duplicate = new Node;
            duplicate->data=current->data;
            duplicate->next=current;
            if (current==head){
                head = duplicate;
            }else{
                Node* prev=head;
                while(prev->next != current){
                    prev = prev->next;
                }
                prev->next=duplicate;
            }
        }
        current = current -> next;
    }
    return head;
}
// задание 1 через массивы
struct ArrayList{
    int data[100];
    int size;
};

ArrayList createListM(){
    ArrayList arr;
    arr.size=0;
    return arr;
}

void addElemM(ArrayList& arr, int val){
    if (arr.size >= 100){
        cout<<"Memory is over"<<endl;
        return;
    }
    arr.data[arr.size]=val; 
    arr.size++;
}

bool removeElemM(ArrayList& arr, int val){
    int index=-1;
    for (int i =0; i<arr.size; i++){
        if (arr.data[i]==val){
            index=i;
            break;
        }
    }
    if (index==-1){
        cout<<"Not found"<<endl;
        return false;
    }
    for (int i = index; i<arr.size-1; i++){
        arr.data[i]=arr.data[i+1];
    }
    arr.size--;
    return true;
}

void duplicateM(ArrayList& arr){
    for (int i=arr.size-1; i>=0;i--){
        if (arr.data[i]%2!=0){
            for (int j=arr.size; j>i; j--){
                arr.data[j]=arr.data[j-1];
            }
            arr.data[i]=arr.data[i+1];
            arr.size++;
        }
    }
}

int main(){
    srand(time(0));
    
    Node* list=createListN();
    int n = rand()%11+5;
    int* data = new int[n];
    for (int i=0; i<n; i++){
        data[i]=rand()%20+1;
    }
    Node* list1=createListN();
    for (int i=0; i<n; i++){
        list1=addElemN(list1, data[i]);
    }
    cout<<"Pointer\n";
    cout<<"Create: ";
    Node* temp=list1;
    while(temp!=nullptr){
        cout<<temp->data<<" ";
        temp=temp->next;
    }
    list1=duplicateN(list1);
    cout<<"Result: ";
    temp=list1;
    while (temp!= nullptr){
        cout<<temp->data<<" ";
        temp=temp->next;
    }

    while (list1 != nullptr){
        Node* del = list1;
        list1= list1->next;
        delete del;
    }
    cout<<endl;
    cout<<"Array\n";
    ArrayList list2=createListM();
    for (int i=0; i<n; i++){
        addElemM(list2,data[i]);
    }
    cout<<"Create: ";
    for (int i=0; i<list2.size; i++){
        cout<<list2.data[i]<<' ';
    }
    duplicateM(list2);

    cout<<"Result: ";
    for(int i=0; i<list2.size; i++){
        cout<<list2.data[i]<<" ";
    }
    delete[] data;


}