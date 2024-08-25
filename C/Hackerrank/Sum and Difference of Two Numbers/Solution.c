#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int int1,int2;
    float float1,float2;

    scanf("%d %d %f %f", &int1 ,&int2, &float1, &float2);

    printf("%d %d\n", (int1+int2), (int1-int2));
    printf("%0.1f %0.1f", (float1+float2), (float1-float2));

    return 0;
}