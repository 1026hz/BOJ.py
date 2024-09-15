#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n,v,cnt;
    vector<int> num(n);

    cin >> n;
    for(int i=0; i<n; i++) cin >> num[i];
    cin >> v;

    cnt = 0;
    for (int i=0; i<n; i++){
        if (num[i] == v) cnt++;
    }
    cout << cnt;

}
