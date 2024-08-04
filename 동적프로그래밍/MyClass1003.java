package 동적프로그래밍;
import java.util.Scanner;

public class MyClass1003 {
  static Integer[][] dp = new Integer[42][2];
  public static void main(String args[]) {
    dp[0][0] = 1;
    dp[0][1] = 0;
    dp[1][0] = 0;
    dp[1][1] = 1;
    
    Scanner in = new Scanner(System.in);
    int T = in.nextInt();
    StringBuilder sb = new StringBuilder();
    while (T-- > 0){
      int N = in.nextInt();
      fibonachi(N);
      sb.append(dp[N][0]+" "+dp[N][1]).append("\n");
    }
    System.out.println(sb);
    in.close();
  }
  static Integer[] fibonachi(Integer n){
    if(dp[n][0] == null || dp[n][1] == null){
      dp[n][0] = fibonachi(n-1)[0] + fibonachi(n-2)[0];
      dp[n][1] = fibonachi(n-1)[1] + fibonachi(n-2)[1];
    }
    return dp[n];
  }
}
