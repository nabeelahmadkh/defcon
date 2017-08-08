#include<stdio.h>
#include<conio.h>
main()
{
    int i,j,k=0,n,a[5][5],pos[5][5],check[5][5];
    int var[16];
    printf("\nEnter the number of min terms ");
    scanf("%d",&n);
    for(i=1;i<5;i++)
        for(j=1;j<5;j++)
        {
            check[i][j]=0;
        }
    pos[1][1]=1;pos[1][2]=2;pos[1][3]=4;pos[1][4]=3;pos[2][1]=5;pos[2][2]=6;pos[2][3]=8;
    pos[2][4]=7;pos[3][1]=13;pos[3][2]=14;pos[3][3]=16;pos[3][4]=15;pos[4][1]=9;
    pos[4][2]=10;pos[4][3]=12;pos[4][4]=11;
    printf("\nEnter the min terms");
    for(i=0;i<n;i++)
    {
        scanf("%d",&var[i]);
    }
    for(i=1;i<5;i++)
        for(j=1;j<5;j++)
        {
            if(pos[i][j]==var[k])
            {
                a[i][j]=var[k++];
            }
        }
    for(i=1;i<5;i++)
    {
        for(j=1;j<5;j++)
            printf("   %d",a[i][j]);
         printf("\n");
    }
}