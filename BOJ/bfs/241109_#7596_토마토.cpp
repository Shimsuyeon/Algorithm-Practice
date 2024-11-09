#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
using namespace std;
int main() {
//전설의 토마토
    int M, N, H;
    cin >> M >> N >> H;

    // 3차원 벡터 초기화: H개의 상자, 각 상자는 N x M 크기
    vector<vector<vector<int>>> tomatoes(H, vector<vector<int>>(N, vector<int>(M)));
    queue<tuple<int,int,int>> q;
    // 입력 받기
    for (int h = 0; h < H; h++) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                cin >> tomatoes[h][i][j];
                if (tomatoes[h][i][j] == 1) {
                    q.push({h, i, j});  // 익은 토마토를 큐에 삽입
                }
            }
        }
    }
    // 1 익은 토마토, 0 안익은 토마토, -1 빈칸
    
    int dh[6] = {-1,1,0,0,0,0};
    int di[6] = {0,0,1,-1,0,0};
    int dj[6] = {0,0,0,0,1,-1};

    int days=0;
    
    while(!q.empty()){
        int size = q.size();
        bool progressed=false;
        for(int s=0;s<size;s++){
            int h,i,j;
            tie(h,i,j) = q.front();
            q.pop();

            for (int d=0;d<6;d++){
                int nh = h+dh[d];
                int ni = i+di[d];
                int nj = j+dj[d];
                if(nh>=0 && nh<H&&ni>=0&&ni<N&&nj>=0&&nj<M&&tomatoes[nh][ni][nj]==0){
                    tomatoes[nh][ni][nj]=1;
                    q.push({nh,ni,nj});
                    progressed=true;
                }
            }
        }
        if(progressed) days++;
    }

    for (int h=0;h<H;h++){
        for(int i=0; i<N; i++){
            for(int j=0; j<M;j++){
                if(tomatoes[h][i][j]==0){
                    cout<<-1<<endl;
                    return 0;
                }
            }
        }
    }
    cout<<days<<endl;

    return 0;

}