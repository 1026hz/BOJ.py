#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, k, ans = 0;
    int student[2][7] = {};

    cin >> n >> k;

    for(int i=0; i<n; i++){
        int a,b;
        cin >> a >> b;
        student[a][b]++;
    }

    for(int i=0; i<2; i++){
        for(int j=0; j<7; j++){
            ans += student[i][j]/2;
            if (student[i][j]%2 > 0) ans += 1;
        }
    }

    cout << ans;
}
