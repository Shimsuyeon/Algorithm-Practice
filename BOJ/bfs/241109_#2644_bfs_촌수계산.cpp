#include <iostream>
#include <deque>
#include <vector>
#include <set>
using namespace std;
int main() {
    int n=0;
    cin>>n;
    //N+1 길이의 배열 0으로 초기화
    vector<set<int>> arr(n+1);

    int a,b;
    cin >> a >> b;

    int m;

    cin >> m;
    for(int i=0;i<m;i++){
        int c,d;
        cin >> c >> d;
        arr[c].insert(d);
        arr[d].insert(c);
    }

    // BFS setup
    deque<int> queue;
    vector<int> visited(n + 1, -1);
    visited[a]=0;
    int ans=0;
    // Start BFS from node `a`
    queue.push_back(a);
    while (!queue.empty()) {
        int current = queue.front();
        queue.pop_front();
        

        // Visit all adjacent nodes
        for (int neighbor : arr[current]) {
            if (visited[neighbor]==-1) {
                visited[neighbor] = visited[current]+1;
                queue.push_back(neighbor);

                if (neighbor==b){
                    cout << visited[neighbor]<<endl;
                    return 0;
                }
            }
        }
    }

    cout << -1 << endl;
    return 0;
}