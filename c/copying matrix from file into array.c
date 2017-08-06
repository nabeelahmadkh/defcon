#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
main()
{
 char ch;
 int i,j;
 char A[10][10];
 FILE *fp;
 fp=fopen("test.txt","r");
 if(fp==NULL)
  {
	printf("\n File cannot be opened");
	exit(1);
  }
 ch=fgetc(fp);
 while(ch!=EOF)
 {    
  for(i=1;i<=9;i++)
   for(j=1;j<=9;j++)
   {
	 if(A[i][j]=='\n')	
	    ch=fgetc(fp);		  
     A[i][j]=ch;
     ch=fgetc(fp);
   }
 }
 for(i=1;i<=9;i++)
 {
	for(j=1;j<=9;j++)
       printf("%c",A[i][j]);
    printf("\n");  
 } 
 fclose(fp);
}
