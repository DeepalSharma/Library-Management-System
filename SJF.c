#include<stdio.h>

int main()
{
    int P[10],BT[10],WT[10],TAT[10],n,i,j,t,min,Pos,total,avg_WT,avg_TAT;
   printf("Enter Number of Process:");
   scanf("%d",&n);
   printf("Input Bus Time BT:");
   for(i=0;i<n;i++)
   {
       scanf("%d",BT[i]);
       P[i]=i+1;
   }
   for(i=0;i<n;i++)
   {
       min=BT[i];Pos=i;
       for(j=i+1;j<n;j++)
       {
           if(min>BT[j])
           {
               Pos=j;
               min=BT[i];
           }
           if(Pos!=i)
           {
               t=BT[Pos];
               BT[Pos]=BT[i];
               BT[i]=t;
               
               t=P[Pos];
               P[Pos]=P[i];
               P[i]=t;
                }
                 WT[0]=0;            
  
   
    for(i=1;i<n;i++)
    {
        WT[i]=0;
        for(j=0;j<i;j++)
            WT[i]=WT[i]+BT[j];
            total=total+WT[i];
    }
  
    avg_WT=(float)total/n;      
    total=0;
  
    printf("nProcesst    Burst Time    tWaiting TimetTurnaround Time");
    for(i=0;i<n;i++)
    {
        TAT[i]=BT[i]+WT[i];   
        total+=TAT[i];
        printf("np%dtt  %dtt    %dttt%d",P[i],BT[i],WT[i],TAT[i]);
    }
  
    avg_TAT=(float)total/n; 
       }
   }
}