#include <iostream>
#include <vector>
#include <queue>
#include <cmath>

using namespace std;

int t; // 테스트 케이스 개수

// 두 좌표 사이의 거리를 계산하는 함수
int manhattanDistance(pair<int, int> a, pair<int, int> b) {
    return abs(a.first - b.first) + abs(a.second - b.second);
}

int main() {
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector<pair<int, int>> locations(n + 2); // 좌표 저장, 0: 상근 집, 1~n: 편의점, n+1: 페스티벌

        // 좌표 입력
        for (int i = 0; i < n + 2; i++) {
            cin >> locations[i].first >> locations[i].second;
        }

        // 그래프 초기화
        vector<vector<int>> graph(n + 2); 

        // 인접 리스트 생성
        for (int i = 0; i < n + 2; i++) {
            for (int j = i + 1; j < n + 2; j++) {
                if (manhattanDistance(locations[i], locations[j]) <= 1000) {
                    graph[i].push_back(j);
                    graph[j].push_back(i);
                }
            }
        }

        // BFS로 페스티벌까지 갈 수 있는지 탐색
        vector<bool> visited(n + 2, false);
        queue<int> q;
        q.push(0); // 상근이네 집에서 시작
        visited[0] = true;
        
        bool canReachFestival = false;

        while (!q.empty()) {
            int curr = q.front();
            q.pop();

            if (curr == n + 1) { // 페스티벌에 도착한 경우
                canReachFestival = true;
                break;
            }

            for (int next : graph[curr]) {
                if (!visited[next]) {
                    visited[next] = true;
                    q.push(next);
                }
            }
        }

        cout << (canReachFestival ? "happy" : "sad") << endl;
    }

    return 0;
}
