/*
 *			Program for converting the infix expression into reverse polish notation
 *			Coded by Nabeel Ahmad Khan
 *			Coded on 2/10/2014
 *			no specific algo is used
 */
#include<stdio.h>
#include<string.h>
#include<stdio.h>
#define long long int vlong;
void main()
{
	char stack[50],str[100],output[100];
	int i,j,k,pointer=0,flag=0;
	printf("enter the infix notation\n");
	scanf("%s",&str);
	int count=strlen(str);
	for (i = 0; i < count; ++i)
		{
			/* code */
			if( str[i]=='(' )
			{
				
			}
			else if (str[i]==')')
			{
				pointer--;
				output[flag++]=stack[pointer];
			}
			else if (str[i]=='+' || str[i]=='*' || str[i]=='/' || str[i]=='-' || str[i]=='^')
			{
				stack[pointer++]=str[i];
			}
			else
				output[flag++]=str[i];

		}
	for (i = 0; i < flag; ++i)
	{
		printf("%c",output[i]);
	}
}