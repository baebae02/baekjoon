import java.util.Dictionary;
import java.util.Hashtable;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int answer = 0;
        int[][] graph = new int[friends.length][friends.length];
        int[] gift_point = new int[friends.length];
        Dictionary<String, Integer> dict = new Hashtable<>();
        for(int i=0; i<friends.length; i++){
            dict.put(friends[i], i);
        }
        // System.out.println(dict);
        for(int i=0; i<gifts.length; i++){
            String[] history = gifts[i].split(" ");
            graph[dict.get(history[0])][dict.get(history[1])]++;
            gift_point[dict.get(history[0])]++;
            gift_point[dict.get(history[1])]--;
        }
        for(int i=0; i<friends.length; i++){
            int i_cnt = 0;
            for(int j=0; j<friends.length; j++){
                // 내가 더 선물을 많이 줬을 경우
                //System.out.println(graph[i][0]+" "+i_cnt);
                if(i != j & graph[i][j] > graph[j][i]){
                    i_cnt++;
                }
                // 주고받은 기록이 없거나 주고받은 수가 같을 경우
                else if(i !=j & graph[i][j] == graph[j][i]){
                    if(gift_point[i] > gift_point[j]){
                        i_cnt++;
                    }
                }
            }
            answer = Math.max(answer, i_cnt);
        }
        return answer;
    }
}