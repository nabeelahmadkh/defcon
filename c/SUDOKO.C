#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>
main()
{
 char ch;
 int i,j,k,l=1,o;
 char b[25];
 char a[10][10];
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
    a[i][j]=ch;
    ch=fgetc(fp);
   }
 }
 for(i=1;i<=9;i++)
  for(j=1;j<=9;j++)
   printf("%c",a[i][j]);
 fclose(fp);
 
 
 
 
 
 
 for(i=1;i<=1;i++)
  {
    for(j=1;j<=1;j++)
     {
		if(a[i][j]==' ')
		 {
		   	for(k=1;k<=9;k++)
			 {
				if(k!=i)
				 {			
	 		       if(a[i][k]!=' ')
			          b[l++]=a[i][k];
				 }			            
			    if(k!=j)
			     { 
				   if(a[k][j]!=' ')
				    b[l++]=a[k][j];	
				 }
		    }
		    if(i==1 || i==4 || i==7)
		    {
			  if(j==1 || j==4 || j==7)
			   {
			    if(a[i+1][j+1]!=' ')
			     b[l++]=a[i+1][j+1];
			    if(a[i+1][j+2]!=' ')
			     b[l++]=a[i+1][j+2];
			    if(a[i+2][j+1]!=' ')
			     b[l++]=a[i+2][j+1];
				if(a[i+2][j+2]!=' ')
			     b[l++]=a[i+2][j+2];  
			   }
			  if(j==2 || j==5 || j==8)
			   {
			    if(a[i+1][j-1]!=' ')
			     b[l++]=a[i+1][j-1];
			    if(a[i+1][j+1]!=' ')
			     b[l++]=a[i+1][j+1];
			    if(a[i+2][j-1]!=' ')
			     b[l++]=a[i+2][j-1];
			    if(a[i+2][j+1]!=' ')
			     b[l++]=a[i+2][j+1];
			   }  	
			  if(j==3 || j==6 || j==9)
			   {
			    if(a[i+1][j-1]!=' ')
			     b[l++]=a[i+1][j-1];
			    if(a[i+1][j-2]!=' ')
			     b[l++]=a[i+1][j-2];
			    if(a[i+2][j-1]!=' ')
			     b[l++]=a[i+2][j-1];
			    if(a[i+2][j-2]!=' ')
			     b[l++]=a[i+2][j-2];
			   }
			 }
		    if(i==2 || i==5 || i==8) 
			{
			 if(j==1 || j==4 || j==7)
			   {
			    if(a[i+1][j+1]!=' ')
			     b[l++]=a[i+1][j+1];
			    if(a[i+1][j+2]!=' ')
			     b[l++]=a[i+1][j+2];
			    if(a[i-1][j+1]!=' ')
			     b[l++]=a[i-1][j+1];
				if(a[i-1][j+2]!=' ')
			     b[l++]=a[i-1][j+2];  
			   }
			  if(j==2 || j==5 || j==8) 
			   {
			    if(a[i-1][j-1]!=' ')
			     b[l++]=a[i-1][j-1];
			     if(a[i+1][j-1]!=' ')
			     b[l++]=a[i+1][j-1];
			      if(a[i-1][j+1]!=' ')
			     b[l++]=a[i-1][j+1];
			      if(a[i+1][j+1]!=' ')
			     b[l++]=a[i+1][j+1];
			   }  	
			  if(j==3 || j==6 || j==9)
			   {
			    if(a[i-1][j-1]!=' ')
			     b[l++]=a[i-1][j-1];
			     if(a[i-1][j-2]!=' ')
			     b[l++]=a[i-1][j-2];
			      if(a[i+1][j-1]!=' ')
			     b[l++]=a[i+2][j-1];
			      if(a[i+1][j-2]!=' ')
			     b[l++]=a[i+1][j-2];
			   }
			}
	        if(i==3 || i==6 || i==9)
			{
             if(j==1 || j==4 || j==7)
			   {
			    if(a[i-1][j+1]!=' ')
			     b[l++]=a[i-1][j+1];
			    if(a[i-2][j+1]!=' ')
			     b[l++]=a[i-2][j+1];
			    if(a[i-1][j+2]!=' ')
			     b[l++]=a[i-1][j+2];
				if(a[i-2][j-2]!=' ')
			     b[l++]=a[i-2][j-2];  
			   }
			  if(j==2 || j==5 || j==8)
			   {
			    if(a[i-1][j-1]!=' ')
			     b[l++]=a[i-1][j-1];
			     if(a[i-2][j-1]!=' ')
			     b[l++]=a[i-2][j-1];
			      if(a[i-1][j+1]!=' ')
			     b[l++]=a[i-1][j+1];
			      if(a[i-2][j+1]!=' ')
			     b[l++]=a[i-2][j+1];
			   }  	
			  if(j==3 || j==6 || j==9)
			   {
			    if(a[i-1][j-1]!=' ')
			     b[l++]=a[i-1][j-1];
			     if(a[i-1][j-2]!=' ')
			     b[l++]=a[i-1][j-2];
			      if(a[i-2][j-1]!=' ')
			     b[l++]=a[i-2][j-1];
			      if(a[i-2][j-2]!=' ')
			     b[l++]=a[i-2][j-2];
			   }
			 
			
			}
	
					
	    }
	    
	printf("\n\n\n");
   for(o=0;o<l;o++)
    printf(" %c",b[o]);	 	
 }
}
 getch();
}
