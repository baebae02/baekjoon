package 동적프로그래밍;
import java.util.Scanner;

public class Main {
  static Integer[][] dp = new Integer[41][2];

  public static void main(String args[]){
    Scanner in = new Scanner(System.in);
    dp[0][0] = 1;
    dp[0][1] = 0;
    dp[1][0] = 0;
    dp[1][1] = 1;

    int T = in.nextInt();
    StringBuilder sb = new StringBuilder();
    while(T-- > 0) {
      int N = in.nextInt();
      fibonachi(N);
      sb.append(dp[N][0]+" "+dp[N][1]).append("\n");
    }
    System.out.println(sb);
    
    in.close(); // Close the Scanner object
  }

  public static Integer[] fibonachi(int N){
    if(dp[N][0] == null || dp[N][1] == null){
       dp[N][0] = fibonachi(N-1)[0] + fibonachi(N-2)[0];
       dp[N][1] = fibonachi(N-1)[1] + fibonachi(N-2)[1];
    }
    return dp[N];
  }

  
}