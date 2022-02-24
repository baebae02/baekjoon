#include <stdio.h>

#include <stdlib.h>

int N, count;

int queen[15];

int abs(int a) 
{
    if (a >= 0)
        return (a);
    else
        return (-a);
}

int pass(int line)
{
    for (int i = 0; i < line; i++)
    {
        if (queen[i] == queen[line] || abs(queen[line] - queen[i]) == line - i)
            return 0;
    }
    return 1;
}
#include <unistd.h>
#include <stdio.h>
void print_arr(int arr[])
{
    int i;

    i = 0;
    while(i < 10)
    {
       printf("%d",arr[i]);
       i++;
    }
    printf("\n");
}
#include <stdio.h>
void nQueen(int line)
{
    if (line == N - 1)
    {
        count++;
        print_arr(queen);
        return;
    }
    for (int i = 0; i < N; i++)
    {
        queen[line + 1] = i;
        if (pass(line + 1))
        {
            nQueen(line + 1);
        }
    }
}

int main()
{
    scanf("%d", &N);
    nQueen(-1);
    printf("%d", count);
}

