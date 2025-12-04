#include <stdio.h>
#include <stdlib.h>


// Function to create a new node
struct node{
    int data;
    struct node* next;
};

struct node* createnode(int data){
    struct node* newnode=(struct node*)malloc(sizeof(struct node));
    newnode->data=data;
    newnode->next=NULL;
    return newnode;
}

struct node* insertatbeg(struct node* head,int data){
    struct node* newnode=(struct node*)malloc(sizeof(struct node));
    newnode->data=data;
    newnode->next=head;
    head=newnode;
    return newnode;
}

struct node* insertabeg(struct node* head,int data){
    struct node* newnode=createnode(data);
    newnode->next=head;
    return newnode;
    
}
struct node* insertatend(struct node* head,int data){
    struct node* newnode=createnode(data);
    if(head==NULL){
        return newnode;
    }
    struct node* temp=head;
    while(temp->next !=NULL){
        temp=temp->next;

    }
    temp->next=newnode;
    return head;
}

struct node* insertatposition(struct node* head,int data,int position){
    struct node* newnode=createnode(data);
    
    struct node* temp=head;
    for (int i=0;i<position-1;i++){
        temp=temp->next;
    }
    if(temp==NULL){
        printf("Position out of bounds\n");
        free(newnode);
        return head;
    }
    newnode->next=temp->next;
    temp->next=newnode;
    return head;

}
void print(int data){
    struct node* temp;
    if(temp!=NULL){
        temp=temp->next;
        print("%d->",data);
        print("\n NULL");
    }

}

int main(){
    struct node* head=NULL;
    createnode(10);
    createnode(20);
    createnode(30);
    head=insertatbeg(head,5);
    insertatposition(head,40,3);
    print();

}