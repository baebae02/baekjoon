import java.util.Hashtable;
import java.util.ArrayList;
import java.util.Dictionary;
import java.util.List;
class Solution {
    public boolean check_date(String today, String target, Integer term){
        String[] target_date = target.split("\\.");
        String[] today_date = today.split("\\.");
        int[] parse_target = {0, 0, 0};
        int[] parse_today = {0, 0, 0};
        for(int i=0; i<3; i++){
            parse_target[i] = Integer.parseInt(target_date[i]);
            parse_today[i] = Integer.parseInt(today_date[i]);
        }
        int cal_target = term*28+ parse_target[0]*12*28 + parse_target[1]*28+parse_target[2];
        int cal_today = parse_today[0]*12*28 + parse_today[1]*28+parse_today[2];
        
        return cal_target <= cal_today;
        
    }
    public List<Integer> solution(String today, String[] terms, String[] privacies) {
        
        Dictionary<String, Integer> dict = new Hashtable<>();
        int size = terms.length;
        List<Integer> answer = new ArrayList<>();
        
        for(int i=0; i<size; i++){
            String[] term = terms[i].split(" ");
            dict.put(term[0], Integer.parseInt(term[1]));
        }
        
        for(int i=0; i<privacies.length; i++){
            String[] privacy = privacies[i].split(" ");
            if(check_date(today, privacy[0], dict.get(privacy[1]))){
                answer.add(i+1);
            }
            
        }
        return answer;
    }
}