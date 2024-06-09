#include <stdio.h>
#include <math.h>
int *lst_hamsaye_fun(int now, int n);
int aval(int n);

int main()
{
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        int n;
        scanf("%d", &n);
        int lst_khaneh[n * n];
        for (int i = 0; i < n * n; i++)
        {
            int adad;
            scanf("%d", &adad);
            lst_khaneh[i] = adad;
        }
        int shoroo_1, shoroo_2, payan_1, payan_2, shoroo, payan, now;
        scanf("%d%d", &shoroo_1, &shoroo_2);
        scanf("%d%d", &payan_1, &payan_2);
        shoroo = shoroo_1 * n + shoroo_2 + 1;
        payan = payan_1 * n + payan_2 + 1;
        now = shoroo;
        int hamsaye_arr[4] = lst_hamsaye_fun(now, n);

        for (int index = 0; index < 4; index++)
        {
            if (aval(lst_khaneh[hamsaye_arr[index]]) == 1)
            {
                int now1 = lst_khaneh[hamsaye_arr[index]];
                if (now1 - now == 1)
                {
                    printf("R");
                }
                else if (now1 - now == -1)
                {
                    printf("L");
                }
                else if (now1 - now == n)
                {
                    printf("D");
                }
                else if (now1 - now == -n)
                {
                    printf("U");
                }
            }
        }
    }

    return 0;
}

int aval(int n)
{
    int a = 1;
    for (int i = 2; i < sqrt(n); i++)
    {
        if (n % i == 0)
            a = 0;
    }
    if (a == 0)
        return 0; // avval nist
    else
        return 1; // avval ast
}

int *lst_hamsaye_fun(int now, int n)
{
    int satr = now / n;
    int sotoon = now % n;
    int *lst_hamsaye;
    if (satr != 0 && sotoon != 0)
    {
        int lst_hamsaye[4] = {now + 1, now - 1, now + n, now - n};
    }

    else if (satr == 0 && now != 0 && now != n - 1)
    {
        int *lst_hamsaye[4] = {now - 1, now + 1, now + n};
    }
    else if (satr == n - 1 && now != n * n - 1 - n && now != n * n - 1)
    {
        int *lst_hamsaye[4] = {now + 1, now - 1, now - n};
    }
    else if (sotoon == 0 && now != 0 && now != n * n - 1 - n)
    {
        int *lst_hamsaye[4] = {now + 1, now - n, now + n};
    }
    else if (sotoon == n - 1 && now != n - 1 && now != n * n - 1)
    {
        int *lst_hamsaye[4] = {now - 1, now - n, now + n};
    }
    else
    {
        if (now == 0)
        {
            int *lst_hamsaye[4] = {now + 1, now + n};
        }
        else if (now == n - 1)
        {
            int *lst_hamsaye[4] = {now - 1, now + n};
        }
        else if (now == n * n - 1)
        {
            int *lst_hamsaye[4] = {now - 1, now - n};
        }
        else if (now == n * n - 1 - n)
        {
            int *lst_hamsaye[4] = {now + 1, now - n};
        }
    }

    return lst_hamsaye;
}