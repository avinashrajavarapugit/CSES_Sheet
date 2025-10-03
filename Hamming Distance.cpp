#include <bits/stdc++.h>
using namespace std;

int fun(int a, int b) {
    int res = a ^ b;
    return __builtin_popcount(res);
}

void solve() {
    int n, k;
    cin >> n >> k;
    vector<int> seen;
    int res = INT_MAX;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        int k = stoi(s, nullptr, 2);
        if (seen.empty()) {
            seen.push_back(stoi(s, nullptr, 2));
        } else {
            for (auto &j : seen) {
                res = min(res, fun(k, j));
            }
            seen.push_back(k);
        }
    }
    cout << res << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int cases = 1;
    while (cases--) {
        solve();
    }
    return 0;
}
