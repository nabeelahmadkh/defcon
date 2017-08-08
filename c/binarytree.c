/*
 *			Program for defining a binary tree 
 *			Coded by Nabeel Ahmad Khan
 *			Coded on 29/09/2014
 *			
 */
 
#include<stdio.h>
#include<string.h>
#include<stdio.h>

#define long long int vlong;
 
 struct binarytree
 {
 	int data;
 	binarytree *lptr,*rptr;
 }root;

 void insert()
 {
 	binarytree *ptr;
 	ptr=malloc(sizeof(binarytree));
 	printf("Enter the data in the node\n");
 	scanf("%d",&ptr->data);
 	ptr->lptr="NULL";
 	ptr->rptr="NULL";
 }

 void delete()
 {

 }

 void view()
 {
 	
 }

void main()
{
	printf("Enter the data in the root of the tree\n");
	scanf("%d",&root.data);
	root.lptr=root.rptr="NULL";
	int i=1;
	while(i<3)
	{
		printf("Enter \n1. to insert in the binary tree\n2. to delete in the binary tree \n3. view the binary tree\n4. to exit\n");
		scanf("%d",&i);
		switch(i)
		{
			case 1:
				insert();
			case 2:
				delete();
			case 3:
				view();
			default:
				printf("Wrong choice entered\n");
		}
	}
}