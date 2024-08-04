package 동적프로그래밍;
import java.util.Scanner;

public class Myclass11726 {
  

  public static void main(String[] args){
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    Integer[] dp = new Integer[n+5];
    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 2;
    
    for (int i=3; i<n+1; i++){
      dp[i] = (dp[i-1] + dp[i-2])%10007;
    }
    System.out.println(dp[n]);
    in.close();
  }
}
