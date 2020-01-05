#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
using namespace std;

int N;

void dfs(int cur, int layer, int n){
    if (cur==n){
        if (check())
    }
}

bool check(*int board, int n){
    for (int i=0; i<n; ++i){

    }
}

vector<vector<string>> solveNQueens(int n) {
    vector<vector<string>> ans;
    int *board = (*int) malloc(n * n);
    for (int i=0; i<n*n; ++i){

    }
}

int main()
{
    scanf("%d", &N);
    vector<vector<string>> ans = solveNQueens(N);
    for (int i=0; i<ans.size(); ++i)
        printf("%s\n", ans[i]);
}
// [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]