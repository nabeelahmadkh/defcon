/*
 *			Program for finding wheather a given string is a substring of another string or not
 *			Coded by Nabeel Ahmad Khan
 *			Coded on 28/09/2014
 *			Algorithm used is Brute Force
 */

 #include<stdio.h>
 #include<string.h>
 #include<stdio.h>
 #define long long int verylong;
 void main()
 {
 	/* code */
 	int i,j,k,l,count=0,check,flag=0,stringlen,substringlen;
 	char str[100],substr[20];		//string for the carring the main string anf the subdtring
 	printf("Enter the string and the substring to be checked separated by enter\n");
 	scanf("%s",&str);
 	scanf("%s",&substr);
 	stringlen=strlen(str);
 	substringlen=strlen(substr);
 	for(i=0;i<stringlen;i++)            //applying brute force for the sub string alogrithm 
 	{
 		check=i;		// paeameters for checking 
 		count=0;
 		flag=0;
 		j=0;
 		if(str[i]==substr[0])
 		{
			while(str[i]==substr[j])
			{
				count++;
				i++;
				j++;
				if(substr[j]=='\0')
				{
					flag=1;
					break;
				}
				if(str[i]=='\0')
				{
					flag=2;
					break;
				}
			}
 		}
 		if(flag==1)
 		{
 			printf("string found at location %d\n",check+1);
 			i=check;
 			flag=0;
 		}
 		else if(flag==2)
 		{
 			break;
 		}
 		else
 		{
 			i=check;
 		}
 	}
 	return 0;
 }