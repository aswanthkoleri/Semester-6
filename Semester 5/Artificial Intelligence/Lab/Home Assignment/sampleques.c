/*#include<stdio.h>
#include<math.h>
int main()
{
    int q;
    scanf("%d",&q);
    while(q--)
    {
        int x,y,i,c=0,k=0,j;
        scanf("%d %d",&x,&y);
        for(i=x;i<=y;i++)
        {
        if(i!=1){
            int flag=0;
         for(j=2;j<=sqrt(i);j++) 
         {
             if(i%j==0){
                flag=1;
                break;
             }
         }
         if(flag==0){
            c++;
         }
        }
        }
         printf("%d\n",c);
        }
    return 0;
}*/

#include<stdio.h>
int main(void)
{
    int q,x,y,i,c=0,k=0,j;
    scanf("%d",&q);
    while(q!=0)
    {
        scanf("%d %d",&x,&y);
        for(i=x;i<=y;i++)
        {
            c=0;
         for(j=1;j<=i;j++) 
         {
             if(i%j==0)
             c=c+1;
         }
         printf("%d\n",c);
         if(c==2)
         k=k+1;
        }
         printf("%d\n",k);
        q=q-1;
    }
    return 0;
}

/*sample input */

/*
[2,_,_,_,9,_,_,_,1,3,_,9,_,_,7,_,_,_,_,_,1,_,4,_,_,7,_,_,6,_,_,_,_,_,_,_,_,_,_,_,_,3,_,_,_,_,_,8,6,_,_,7,9,_,6,_,_,7,_,_,8,_,_,1,2,3,_,_,8,_,_,_,_,8,7,_,_,4,3,_,_*/
[[2,_,_,_,9,_,_,_,1],[3,_,9,_,_,7,_,_,_],[_,_,1,_,4,_,_,7,_],[_,6,_,_,_,_,_,_,_],[_,_,_,_,_,3,_,_,_],[_,_,8,6,_,_,7,9,_],[6,_,_,7,_,_,8,_,_],[1,2,3,_,_,8,_,_,_],[_,8,7,_,_,4,3,_,_]]
[
    [2,X12,X13,X14,9,X16,X17,X18,1],
    [3,X22,9,X24,X25,7,X27,X28,X29],
    [X31,X32,1,X34,4,X36,X37,7,X39],
    [X41,6,X43,X44,X45,X46,X47,X48,X49],
    [X51,X52,X53,X54,X55,3,X57,X58,X59],
    [X61,X62,8,6,X65,X66,7,9,X69],
    [6,X72,X73,7,X75,X76,8,X78,X79],
    [1,2,3,X84,X85,8,X87,X88,X89],
    [X91,8,7,X94,X95,4,3,X98,X99]
]

[
    ['B','X','X','X','I','X','X','X','A'],
    ['C','X','I','X','X','G','X','X','X'],
    ['X','X','A','X','D','X','X','G','X'],
    ['X','F','X','X','X','X','X','X','X'],
    ['X','X','X','X','X','C','X','X','X'],
    ['X','X','H','F','X','X','G','I','X'],
    ['F','X','X','G','X','X','H','X','X'],
    ['A','B','C','X','X','H','X','X','X'],
    ['X','H','G','X','X','D','C','X','X']
]