// src: Hi, I'm Avinash Rajavarapu

#include <bits/stdc++.h>
using namespace std;

#define int long long
const int MOD = 1e9 + 7;

int ri() { int x; cin >> x; return x; }
vector<int> rl(int n) { vector<int> v(n); for (int i = 0; i < n; i++) cin >> v[i]; return v; }
string rs() { string s; cin >> s; return s; }
vector<int> rm(int n) { vector<int> v(n); for (int i = 0; i < n; i++) cin >> v[i]; return v; }

void solve() {
    /*
        Example input:
        2 9
        3 5
        target = 9
    */

    int n, x;
    cin >> n >> x;
    vector<int> coins = rl(n);

    // sort & unique like Python's sorted(set())
    sort(coins.begin(), coins.end());
    coins.erase(unique(coins.begin(), coins.end()), coins.end());

    vector<int> dp(x + 1, 0);
    dp[0] = 1;

    for (int i = 1; i <= x; i++) {
        long long s = 0;
        for (int coin : coins) {
            if (coin > i) break;
            s += dp[i - coin];
            if (s >= MOD) s -= MOD;
        }
        dp[i] = s;
    }

    cout << (dp[x] % MOD) << "\n";
}

void run() {
    int cases = 1;
    while (cases--) {
        solve();
    }
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    run();
    return 0;
}
