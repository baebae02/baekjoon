import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;

//https://school.programmers.co.kr/questions/74274

class Solution {
    private static List<List<Integer>> graph;
    private static int[] input_edges;
    private static int[] output_edges;
    private static int start_node;
    private static int l;
    private static boolean[] visited;
    
    public static int find_max(int[][] arr){
        int max_value = 0;
        for(var a: arr){
            max_value = Math.max(max_value, Math.max(a[0], a[1]));
        }
        return max_value;
    }
    public static int find_root_node(){
        int answer = 0;
        for(int i=0; i<l+1; i++){
            if (input_edges[i] == 0 & output_edges[i] >= 2){
                visited[i] = true;
                return i;
            }
        }
        return answer;
    }
    public static int check_eight(){
        int answer = 0;
        for(int i=1; i<output_edges.length; i++){
            if(!visited[i]){
                if(output_edges[i] == 2 & input_edges[i] == 2){
                answer++;
                }
            }
        }
        return answer;
    }
    public static int check_stick(){
        int answer = 0;
        for(int i=1; i<graph.size(); i++){
            // System.out.println("stick"+input_edges[i]+" "+output_edges[i]);
            if(i == start_node){
                continue;
            }
            if(output_edges[i] == 0 & input_edges[i] >= 1){
                answer++;
                visited[i] = true;
            }
        }
        return answer;
        
    }
    public int[] solution(int[][] edges) {
        int[] answer = {0, 0, 0, 0};
        
        l = find_max(edges);
        visited = new boolean[l+1];
        input_edges = new int[l+1];
        output_edges = new int[l+1];
        graph = new ArrayList<>(l+1);
        for(int i=0; i<l+1; i++){
            graph.add(new LinkedList<>());
        }
        
        
        for(int[] e: edges){
            output_edges[e[0]]++;
            input_edges[e[1]]++;
            graph.get(e[0]).add(e[1]);
        }
        start_node = find_root_node();
        answer[0] = start_node;
        int start_graph_cnt = (graph.get(start_node)).size();
        
        // 시작 노드, 도넛, 막대, 8자
        answer[2] = check_stick();
        for(var k: graph.get(start_node)){
            input_edges[k]--;
        }
        
        answer[3] = check_eight();
        
        answer[1] = start_graph_cnt - answer[3] - answer[2];
        // System.out.println("0"+ answer[0]);
        // System.out.println("1"+ start_graph_cnt);
        // System.out.println("2"+ answer[2]);
        // System.out.println("3" +answer[3]);
        return answer;
    }
}