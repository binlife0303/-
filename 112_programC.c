#include <stdio.h>
#include <stdlib.h>

void main()
{
    int i, L, R, n, m, count, index;
    n=8;
    long long int ans;
    ans=0;
    L=1;
    R=n;
    index=1;
    count = n/index;
    while(1)
    {
        if (index>n)break;
        while(L<=R)
        {
            m=(L+R)>>1;
            if(n/m<count)R=m-1;
            else L=m+1;
        }
        ans+=(long long int)(index+R)*(R-index+1)*(n/index)/2;
        index=R+1;
        count=n/index;
        l=index;
        R=n;
    }
    printf("%lld\n", ans-1);
}