#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    
    vector<int> mon(n);
    vector<int> dp(m + 1, 10001);
    dp[0] = 0;  // 0원을 만드는 데 필요한 동전 수는 0개입니다.

    for (int i = 0; i < n; ++i) {
        cin >> mon[i];
    }

    for (int i = 1; i <= m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i >= mon[j]) {  // i가 mon[j] 이상일 때만 mon[j]를 뺄 수 있음
                dp[i] = min(dp[i], dp[i - mon[j]] + 1);
            }
        }
    }

    // 결과 출력
    if (dp[m] == 10001) {
        cout << -1 << endl;
    } else {
        cout << dp[m] << endl;
    }

    return 0;
}
