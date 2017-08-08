/*
**** Program to find HAMILTONIAN PATH in a given matrix ****
**** coded by--->NABEEL AHMAD KHAN ****
**** dated   --->30/10/2013 ****
**** code this program again by recursion method ****
*/

#include<stdio.h>
struct node
{
    char a;
};
main()
{
    int n,i,j,k=0,check,l,p;
    printf("\nenter the number of elements you want to enter ");
    scanf("%d",&n);
    struct node arr[n+1];
    char list[10];
    int mat[n][n];
    for(i=1;i<n;i++)
        mat[i][i]=0;
    for(i=1;i<=n;i++)
    {
        fflush(stdin);
        scanf("%c",&(arr[i].a));
    }
    for(i=1;i<=n;i++)
    {
        printf("%c\n",arr[i].a);
    }
    mat[1][2]=1;
    mat[1][3]=1;
    mat[1][4]=1;
    mat[2][1]=1;
    mat[2][3]=0;
    mat[2][4]=1;
    mat[3][1]=1;
    mat[3][2]=0;
    mat[3][4]=0;
    mat[4][1]=1;
    mat[4][2]=1;
    mat[4][3]=0;
    //for(i=1;i<=n;i++)    matrix embedded into the program to save time to input the matrix
    //{
      //  for(j=1;j<n;j++)
        //{
          //  if(i!=j)
            //{
              //  printf("is there an edge between %c and %c (enter 1 for edge and 0 for no edge)",arr[i].a,arr[j].a);
                //scanf("%d",&mat[i][j]);
            //}
        //}
    //}
    int abc=0;
    int loop=0;
    list[++k]=arr[3].a;
    for(p=1;p<=4;p++)
    {
        abc=0;
        k=0;
        list[++k]=arr[p].a;
      for(i=p;i<=n;)
      {
        abc++;
        printf("1");
        check=0;
        for(j=1;j<=n;j++)
        {
            check=0;
            printf("2");
            if(mat[i][j]==1)
            {
                for(l=1;l<=k;l++)
                {
                    printf("3");
                    if(list[l]==arr[j].a)
                    {
                        printf("5");
                        check=1;
                    }
                }
                if(check==0)
                {
                    printf("4");
                    list[++k]=arr[j].a;
                    i=j;
                    goto label;
                }
            }
        }
        label:
        if(abc>4)
            break;
    }
    printf("\n\n");
    for(i=1;i<=k;i++)
        printf("%c ",list[i]);
    printf("\n\n\n");
  }
}
