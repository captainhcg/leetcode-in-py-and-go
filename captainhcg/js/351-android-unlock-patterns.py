var map = [];
for(var idx = 0; idx < 10; idx += 1){
    map[idx] = [];
}
map[1][3] = map[3][1] = 2;
map[1][7] = map[7][1] = 4;
map[2][8] = map[8][2] = 5;
map[4][6] = map[6][4] = 5;
map[7][9] = map[9][7] = 8;
map[3][9] = map[9][3] = 6;
map[1][9] = map[9][1] = 5;
map[3][7] = map[7][3] = 5;

var numberOfPatterns = function(m, n) {
    var visited = {}
    var count = 0;
    var dfs = function(val, length){
        if(length > n){
            return;
        }else if(length >= m){
            count += 1;
        }
        for(var next=1; next <= 9; next +=1){
            if(visited[next]){
                continue;
            }
            if(map[val][next] && !visited[map[val][next]]){
                continue
            }
            visited[next] = true;
            dfs(next, length + 1)
            visited[next] = false;
        }
    }
    for(var idx = 1; idx < 10; idx++){
        visited[idx] = true;
        dfs(idx, 1);
        visited[idx] = false;
    }
    return count;
};
