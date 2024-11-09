#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;
int main() {
    int T, W;
    cin >> T >> W;

    vector<int> drop(T + 1, 0);
    for (int i = 1; i <= T; i++) {
        cin >> drop[i];
    }

    // DP 배열: dp[time][moves] = 해당 시간에 moves번 이동한 상태에서의 최대 자두 개수
    vector<vector<int>> dp(T + 1, vector<int>(W + 1, 0));

    for (int t = 1; t <= T; t++) {
        for (int w = 0; w <= W; w++) {
            // 현재 위치에 있는 나무의 번호
            int current_tree = (w % 2 == 0) ? 1 : 2;

            // 이동하지 않고 자두를 받는 경우
            dp[t][w] = dp[t - 1][w] + (drop[t] == current_tree ? 1 : 0);

            // 이동한 후 자두를 받는 경우 (이동 가능할 때만)
            if (w > 0) {
                dp[t][w] = max(dp[t][w], dp[t - 1][w - 1] + (drop[t] == current_tree ? 1 : 0));
            }
        }
    }

    // 최대 자두 개수 계산
    int result = 0;
    for (int w = 0; w <= W; w++) {
        result = max(result, dp[T][w]);
    }

    cout << result << endl;
    return 0;
}