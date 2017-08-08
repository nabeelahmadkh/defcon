/*
 *			Program for finding wheather a given string is a substring of another string or not,,,wheather in sequence or  not
 *			Coded by Nabeel Ahmad Khan
 *			Coded on 28/09/2014
 *			Algorithm used is Brute Force
 */
#include<stdio.h>
#include<string.h>
#include<stdio.h>
#define long long int vlong;
void main()
{
	int stringlen,substringlen,i,j,k,l,flag=0,check=0,count=0,actualcount=100,small=0;
	char str[100],substr[20];

	printf("Enter the string for which u want to check \n");
	scanf("%s",&str);
	printf("Enter the string to be checked for substring\n");
	scanf("%s",&substr);

	stringlen=strlen(str);
	substringlen=strlen(substr);

	j=0;
	for(i=0;i<stringlen;i++)
	{
		j=0;
		check=i;
		count=0;
		flag=0;
		actualcount=0;
		if(str[i]==substr[j])
		{
			//while(str[i]!='\0')
			printf(" a ");
			while(i<=stringlen)
			{
				printf(" b ");
				count++;
				if(str[i]==substr[j])
				{
					printf(" c ");
					j++;
					actualcount++;
				}
				i++;
				if(str[i]=='\0' && count<substringlen)
				{
					printf(" d ");
					flag=2;
					break;
				}
				else if (actualcount>=substringlen && j==substringlen)
				{
					printf(" e ");
					flag=1;
					printf("\nThe smallest count is  new %d\n",actualcount);
					if(actualcount<small)
						small=actualcount;
					break;
				}
				else
					flag=3;
			}
		}
		//printf("\nThe smallest count is %d\n",actualcount);
		//if(actualcount < small)
		//{
		//	small=actualcount;
		//	printf("\nThe smallest count is %d\n",actualcount);
		//}
		if(flag==1)
		{
			printf("\nThe substring is found at %d location",check+1);
		}
		printf(" f ");
		if(flag!=0)
			i=check;
	}
	printf("The smallest count is %d\n",small);
}