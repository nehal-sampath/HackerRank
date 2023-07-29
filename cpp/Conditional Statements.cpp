#include <bits/stdc++.h>
using namespace std;

int main() 
{
int i;
string num[10] = {"Greater than 9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

cin >> i;

if(i > 9){
    cout << num[0];
}
else{
    cout << num[i];
}

return 0;
}
