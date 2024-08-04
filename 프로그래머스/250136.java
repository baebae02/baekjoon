import java.util.*;

class Solution {
    private boolean[][] visited;
    private int[] dx = {0, 1, 0, -1};
    private int[] dy = {1, 0, -1, 0};
    private int n;
    private int m;
    private int[][] maps;
    static int oil[];
    
    private boolean isCheckAble(int i, int j){
        return (i >= 0 && i < n && j >= 0 && j < m && visited[i][j] == false && maps[i][j] == 1);
    }
    private int s_oil_bfs(int i, int j){
        Queue<int[]> q = new LinkedList<>();
        
        if(maps[i][j] == 0 || visited[i][j] == true){
            return 0;
        }
        int count = 1;
        q.add(new int[] {i,j});
        visited[i][j] = true;
        Set<Integer> set = new HashSet<>();
      
        while (!q.isEmpty()){
            int[] current = q.poll();
            set.add(current[1]);
            // System.out.println(q.size() + "qsize" + current[0] + " "+ current[1]);
            for(int k=0; k<4; k++){
                int x = current[0] + dx[k];
                int y = current[1] + dy[k];
                if(!isCheckAble(x,y)) continue;
                visited[x][y] = true;
                count++;
                q.add(new int[] {x,y});
            }
        }
        for(int x : set){
            oil[x] += count;
        }
        
        return count;
    }
    public int solution(int[][] land) {
        maps = land; 
        int max_value = 0;
        n = land.length;
        m = land[0].length;
        oil = new int[m];
        visited = new boolean[n][m];
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                s_oil_bfs(i,j);
            }
        }
        max_value = Arrays.stream(oil).max().getAsInt();
        return max_value;
    }
}