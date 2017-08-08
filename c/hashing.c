/*
 *          Program for saving data entered using hash function.
 *          Coded by Nabeel Ahmad Khan
 *          Coded on 28/09/2014
 *          Algorithm used is Hashing Algo
 */

#include<stdio.h>
#include<conio.h>

int hash(int ky);
struct node
{
 int key;
 char name[20];
struct node* ptr;
};
main()
{
    char ch='y';
    struct node *ptr2;
    int n,i,add,sr,check;
    struct node *pointer[25];
    int keyg;
    int check2=0;
    for(i=0;i<25;i++)
        pointer[i]='null';

    while(ch=='y')
    {
        struct node *nwptr = malloc(sizeof(struct node));
        printf("\nEnter the data of the element\n");
        scanf("%d",&nwptr->key);
        printf("\nEnter the name of the element\n");
        scanf("%s",&nwptr->name);
        add=hash(nwptr->key);
        if(pointer[add]=='null')
            {
                pointer[add]=nwptr;
                pointer[add]->ptr='null';
            }
        else
            {
                printf("\n else part executed\n\n");
                ptr2=pointer[add];
                while(ptr2!='null')
                {
                    if(ptr2->ptr=='null')
                        {
                            ptr2->ptr=nwptr;
                            nwptr->ptr='null';
                            break;
                        }
                    else
                        ptr2=ptr2->ptr;

                }
            }
         printf("\ndo u want to enter more elements\n");
         fflush(stdin);
         scanf("%c",&ch);
    }
    printf("\nEnter the data to be searched\n");
    scanf("%d",&sr);
    check=hash(sr);
    printf("\nThe details of the individual are\n");
    ptr2=pointer[check];
      do
        {
            if(check2>0)
                ptr2=ptr2->ptr;
            if(ptr2->key==sr)
                printf("data->%d\nname->%s",ptr2->key,ptr2->name);
            check2++;
        }while(ptr2!='null');

}
int hash(int ky)
{
    int m;
    m=ky%25;
    return m;
}
