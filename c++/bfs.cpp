#include<stdio.h>
#include<stdlib.h>
void pop();
struct node
{
    char data;
    int status;
    node *nxt;
    node *edge;
};
node *tmp2;
node * start,*end;
node * temp3;
node *quesrt,*queend;
main()
{
    int count=0;
    start=NULL;
    end=NULL;
    char ch='y';
    printf("\nEnter the nodes");
    while(ch=='y')
    {
        node *temp=new node;
        printf("\nEnter the node element");
        fflush(stdin);
        scanf("%c",&temp->data);
        temp->status=1;
        if(start==NULL)
        {
            start=temp;
            end=temp;
            temp->nxt=NULL;
            temp->edge=NULL;
        }
        else
        {
            end->nxt=temp;
            temp->nxt=NULL;
            end=temp;
            temp->edge=NULL;
        }
        printf("\nDo u want to enter more elements");
        fflush(stdin);
        scanf("%c",&ch);
    }
    printf("\nThe nodes u entered are");
    node *temp;
    temp=start;
    while(temp!=NULL)
    {
        printf("%c-->",temp->data);
        temp=temp->nxt;
        count++;
    }
    printf("\nYou have entered %d nodes",count);
    temp=start;
    while(temp!=NULL)
    {
        char choice;
        node * endtemp;
        endtemp=NULL;
        printf("\nDo u want to enter the edge nodes of '%c' node(y/n)",temp->data);
        fflush(stdin);
        scanf("%c",&choice);
        while(choice=='y')
        {
            node * temp2;
            temp2=start;
            node *nw=new node;
            printf("\nEnter the node");
            fflush(stdin);
            scanf("%c",&nw->data);
            if(endtemp==NULL)
            {
                temp->edge=nw;
                nw->edge=NULL;
                endtemp=nw;
                while(temp2!=NULL)
                {
                    if(nw->data==temp2->data)
                    {
                        nw->nxt=temp2;
                    }
                    temp2=temp2->nxt;
                }
            }
            else
            {
                endtemp->edge=nw;
                endtemp=nw;
                nw->edge=NULL;
                while(temp2!=NULL)
                {
                    if(nw->data==temp2->data)
                    {
                        nw->nxt=temp2;
                    }
                    temp2=temp2->nxt;
                }
            }
            printf("\nDo u want to enter edge node to '%c' node",temp->data);
            fflush(stdin);
            scanf("%c",&choice);
        }
        temp=temp->nxt;
    }
    temp=start;
    while(temp!=NULL)
    {
        printf("\n%c-->",temp->data);
        node *tempnew;
        node *tempnew2;
        tempnew=temp->edge;
        while(tempnew!=NULL)
        {
            printf(" %c ",tempnew->data);
            tempnew2=tempnew->nxt;
            printf("%c",tempnew2->data);
            tempnew=tempnew->edge;
        }
        temp=temp->nxt;
    }

    // bsf algorithm starts here
    printf("enter the node from which u want to start traversing");
    char choice1;
    fflush(stdin);
    scanf("%c",&choice1);
    node * con;
    con=start;
    while(con!=NULL)
    {
        if(con->data==choice1)
        {
            break;
        }
        con=con->nxt;
    }

    quesrt=con;
    queend=con;
    int check3=0;
    printf("\n%c",quesrt->data);
    node * temp4;
    quesrt->data=3;
    quesrt=quesrt->edge;
    temp4=quesrt;
    while(temp4!=NULL)
    {
        node *ptr2=new node;
        if(check3==0)
        {
            check3=1;
            quesrt=ptr2;
        }
        else
        {
            queend->edge=ptr2;
        }
        ptr2->data=temp4->data;
        ptr2->edge=temp4->edge;
        ptr2->nxt=temp4->nxt;
        temp4=temp4->edge;
        queend=ptr2;
    }
    while(quesrt!=NULL)
    {
        pop();
    }
}
void pop()
{
    tmp2=quesrt->nxt;
    printf("\n%c",quesrt->data);
    tmp2->status=3;
    quesrt=quesrt->edge;
    tmp2=tmp2->edge;
    while(tmp2!=NULL)
    {
        node *tmp4;
        tmp4=tmp2->nxt;
        if(tmp4->status==1)
        {
            node * ptr3=new node;
            ptr3->data=tmp2->data;
            printf("%c",ptr3->data);
            ptr3->nxt=tmp2->nxt;
            ptr3->edge=NULL;
            queend->edge=ptr3;
            queend=ptr3;
        }
        tmp2=tmp2->edge;
    }

}
