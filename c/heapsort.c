/**
 *
 * @author NABEEL AHMAD KHAN
 * dated 22/10/2013
*/
#include<stdio.h>
#include<math.h>
int arr[100],n;
int sorarr[100];
main()
{
      int i,k,j,l,count=50;
      printf("\nEnter the number of elements to entered");
      scanf("%d",&n);
      k=log(n)+1;
      printf("\nEnter the array elements");
      for(i=1;i<=n;i++)
          scanf("%d",&arr[i]);
      printf("\nThe number entered are");
      for(i=1;i<=n;i++)
          printf("%d ",arr[i]);
      for(i=n/2;i>0;i--)
          heap(i);
      printf("\nThe num after heapfying operation are");
       for(i=1;i<=n;i++)
          printf("%d ",arr[i]);
      printf("\nThe heap in tree form");
      for(i=1;i<=k+1;i++)
      {
          printf("\n");
          for(j=pow(2,i-1);j<2*(pow(2,i-1));j++)
          {
           if(i==2)
             for(l=0;l<8;l++)
                printf(" ");
           if(i==3)
             for(l=0;l<4;l++)
                printf(" ");

           if(j<=n)
             {
                for(l=0;l<count/i;l++)
                 {
                    printf(" ");
                 }
                    printf("%d",arr[j]);
             }
          }
      }
      del();
      printf("\nthe sorted array is");
      for(i=0;i<n;i++)
           printf("%d ",sorarr[i]);
      getch();
}
heap(int i)
{
         int temp,num;
         int flag=0;
         if(arr[i]<arr[2*i])
         {
            if(arr[2*i]>arr[2*i+1])
            {
               temp=arr[2*i];
               arr[2*i]=arr[i];
               arr[i]=temp;
               flag=2*i;
            }
         }
         if(arr[i]<arr[2*i+1])
         {
            if(arr[2*i+1]>arr[2*i])
            {
               temp=arr[2*i+1];
               arr[2*i+1]=arr[i];
               arr[i]=temp;
               flag=2*i+1;
            }
         }
         if(flag!=0)
         {
                    int check=0;
                    while(flag<=n/2)
                    {
                           if(arr[flag]<arr[2*flag])
                           {
                             if(arr[2*flag]>arr[2*flag+1])
                             {
                              temp=arr[2*flag];
                              arr[2*flag]=arr[flag];
                              arr[flag]=temp;
                              flag=2*flag;
                              check=1;
                             }
                           }
                            if(arr[flag]<arr[2*flag+1])
                            {
                             if(arr[2*flag+1]>arr[2*flag])
                             {
                              temp=arr[2*flag+1];
                              arr[2*flag+1]=arr[flag];
                              arr[flag]=temp;
                              flag=2*flag+1;
                              check=1;
                             }
                            }
                           if(check==0)
                             break;
                    }
         }
}
del()
{
     int j=0,temp;
     int flag=1;
     int d=n;
     int check=0;
     sorarr[j++]=arr[1];
     arr[1]=arr[n];
     d--;
     while(d>0)
     {
               check=0;
               flag=1;
               //printf("a");
               while(flag<=d/2)
                    {
                           check=0;
                           //printf("b");
                           if(arr[flag]<arr[2*flag])
                           {
                             if(arr[2*flag]>arr[2*flag+1] || (2*flag+1)>d)
                             {
                              temp=arr[2*flag];
                              arr[2*flag]=arr[flag];
                              arr[flag]=temp;
                              flag=2*flag;
                              check=1;
                             }
                           }
                            if(arr[flag]<arr[2*flag+1] && (2*flag+1)<=d)
                            {
                             if(arr[2*flag+1]>arr[2*flag])
                             {
                              temp=arr[2*flag+1];
                              arr[2*flag+1]=arr[flag];
                              arr[flag]=temp;
                              flag=flag*2+1;
                              check=1;
                             }
                            }
                           if(check==0)
                             break;
                             //printf("c");

                    }
             sorarr[j++]=arr[1];
             arr[1]=arr[d];
             d--;
      }
}
