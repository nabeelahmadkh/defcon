/*to implement linked list and
  to show add, delete , swap , display function in the linked list
  coded by--->>>NABEEL AHMAD KHAN
                11-PEB-146
                GG-00-44
                COMPUTER ENGG. DEPT.
                FACULTY OF ENGG. & TECHNOLOGY
                A.M.U. ,ALIGARH
*/

#include<stdio.h>

void add();
void del();
void swap();
void display();

struct node
{
    int data;
    node *ptr;
};

node *start=NULL,*end=NULL;

main()
{
    int ch=0;
    while(ch<5)
    {
        printf("\n1. To add node\n2. To delete node\n3. To swap node \n4. To display the linked list");
        printf("\n\nEnter your choice");
        scanf("%d",&ch);
        switch(ch)
        {
            case(1):    add();
                        break;
            case(2):    del();
                        break;
            case(3):    swap();
                        break;
            case(4):    display();
                        break;
            default:
                        printf("wrong choice entered /");
        }
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
        node *n;
        n=start;
        int num,check=0,flag2=0;
        display();
        printf("\nenter the number after which you want to enter the number");
        scanf("%d",&num);
        do
        {
            if(flag2!=0)
                n=n->ptr;
            flag2=1;
            if(n->data==num)
            {
                printf("\nenter the nummber you want to enter");
                scanf("%d",&temp->data);
                temp->ptr=n->ptr;
                n->ptr=temp;
                check=1;
                break;
            }

        }while(n->ptr!=NULL);
        if(check==0)
            printf("\n no such number found");
        else
            printf("element successfully inserted");
    }
}
void del()
{
    int num,no,flag=0,check=0;
	node* lte,* pre;
	pre=start;
	lte=start;
	printf("\nEnter the element to be deleted--->");
	scanf("%d",&num);
		if(num==start->data)
		{
			start=start->ptr;
			check=1;
		}
		else
		{
			do
			{
				if(num==lte->data)
				{
					pre->ptr=lte->ptr;
					check=1;
					break;
				}
				if(flag>0)
					pre=pre->ptr;
				flag++;
				lte=lte->ptr;
			}while(lte!=NULL);
		}
      if(check==0)
       printf("\n    Element not found");
      else
       printf("\n    Element deleted");

}

void swap()
{
    display();
    int num1,num2,flag=0;
    node *pre1=start,*pre2=start,*on1=NULL,*on2=NULL,*after1=NULL,*after2=NULL;
    printf("Enter the elements to be swapped");
    scanf("%d%d",&num1,&num2);
    if(num1==start->data || num2==start->data)
    {
        on1=start;
        after1=start->ptr;
        flag=1;
        if(num1==start->data)
            pre1=NULL;
        else
            pre2=NULL;
    }

    {
        if(flag==0)
            on1=start->ptr;
        on2=start->ptr;
        while(on1!=NULL || on2!=NULL)
        {
            if((on1->data==num1 || on1->data==num2) && flag==0 )
            {
                after1=on1->ptr;
                flag=1;
                pre2=pre2->ptr;
                on2=on2->ptr;
                continue;
            }
            if((on2->data==num1 || on2->data==num2) && flag==1)
            {
                after2=on2->ptr;
                break;
            }
            if(flag==0)
                {
                    pre1=pre1->ptr;
                    on1=on1->ptr;
                }
            pre2=pre2->ptr;
            on2=on2->ptr;
        }
    }
    if(pre1==NULL && on1->ptr==on2)
    {
        start=on2;
        on2->ptr=on1;
        on1->ptr=after2;
    }
    else if(on1->ptr==on2)
    {
        pre1->ptr=on2;
        on2->ptr=on1;
        on1->ptr=after2;
    }
    else if(pre1==NULL)
    {
        start=on2;
        on2->ptr=after1;
        pre2->ptr=on1;
        on1->ptr=after2;
    }
    else if(on1->ptr==on2 && after2==NULL)
    {
        pre1->ptr=on2;
        on2->ptr=on1;
        on1->ptr=NULL;
        end=on2;

    }
    else
    {
        pre1->ptr=on2;
        on2->ptr=after1;
        pre2->ptr=on1;
        on1->ptr=after2;
    }
    display();
}
void display()
{
    node *temp;
    temp=start;
    printf("\nSTART");
    while(temp!=NULL)
    {
        printf("---->%d",temp->data);
        temp=temp->ptr;
    }
    printf("--->END");
}
