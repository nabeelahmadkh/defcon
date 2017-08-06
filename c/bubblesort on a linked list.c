#include<stdio.h>
void add();
void display();
void sort();
struct node
{
    int data;
    node *ptr;
};
node *start,*end;
main()
{
    start=end=NULL;
    int choice;
    printf("\n   Enter the choice ");
    printf("\n   1. To add node\n2. To sort the linked list\n3. To display the linked list\n");
    scanf("   %d",&choice);
    switch(choice)
    {
        case(1):
                add();
                break;
        case(2):
                sort();
                break;
        case(3):
                display();
                break;
        default:
                printf("\n   Wrong choice entered");
    }
}

void add()
{
    node *temp=new node;
    if(start==NULL)
    {
        printf("\nEnter the data to be entered--->");
        scanf("%d",&temp->data);
        temp->ptr=NULL;
        start=temp;
        end=temp;
    }
    else
    {
        end->ptr=temp;
        end=temp;
    }
}
void display()
{
    node *temp=new node;
    temp=start;
    while(temp!=NULL)
    {
        printf("%d",temp->data);
        temp=temp->ptr;
    }
}
void sort()
{

}
