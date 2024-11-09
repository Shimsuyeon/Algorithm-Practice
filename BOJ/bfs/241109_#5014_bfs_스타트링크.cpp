#include <stdio.h>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
int main(){
    int f,s,g,u,d;
    cin >> f >> s >> g >> u >> d;
    // 총 f층
    // 나는 지금 s층
    // 나는 g층으로 하고 싶음
    // 위로 u층으로 이동하거나, 아래로 d층으로 이동
    // 만약 i+u>f거나, i-d<0이면 이동하지 않음

    queue<int> q;
    q.push(s);
    vector<int> visited(f+1, -1);
    visited[s]=0;
    while (!q.empty()){
        int current = q.front();
        q.pop();
        if (current==g) {
            cout<<visited[g]<<endl;
            return 0;
        } else {
            if ((current+u)<=f && visited[current+u]==-1) {
                visited[current+u]=visited[current]+1;
                q.push(current+u);
            }
            if ((current-d)>0&&visited[current-d]==-1) {
                visited[current-d] = visited[current]+1;
                q.push(current-d);
            }
        }
    }

    cout << "use the stairs" << endl;
    return 0;
}