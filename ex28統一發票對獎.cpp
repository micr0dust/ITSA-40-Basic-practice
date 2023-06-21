#include <bits/stdc++.h>

using namespace std;
string sp,h1,h2,h3;

int price(string str){
    if(str==sp) return 0;
    int min=7;
    for (int i = 7; i >=0; i--)
        if(str[i]==h1[i] && i+1<min)
            min=i+1;
        else if(str[i]!=h1[i]) break;
    for (int i = 7; i >=0; i--)
        if(str[i]==h2[i] && i+1<min)
            min=i+1;
        else if(str[i]!=h2[i]) break;
    for (int i = 7; i >=0; i--)
        if(str[i]==h3[i] && i+1<min)
            min=i+1;
        else if(str[i]!=h3[i]) break;
    return min;
}

int main()
{
    int record[7]={0},cases;
    cin >> sp >> h1 >> h2 >> h3 >> cases;
    for (;cases--;)
    {
        string str;
        cin >> str;
        int res=price(str);
        if(res<7)
            record[res]++;
    }
    for (int i = 0; i < 7; i++)
        cout << record[i] << (i+1<7?' ':'\n');
    cout << 2000000*record[0]+200000*record[1]+40000*record[2]+10000*record[3]+4000*record[4]+1000*record[5]+200*record[6] << '\n';
    return 0;
}