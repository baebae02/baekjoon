package 동적프로그래밍;

import java.util.Scanner;

public class MainClass1149 {
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    Integer[][] dp = new Integer[N][3];
    Integer[][] price = new Integer[N][3];

    for(int i=0; i<N; i++){
      price[i][0] = sc.nextInt();
      price[i][1] = sc.nextInt();
      price[i][2] = sc.nextInt();
    }
    dp[0][0] = price[0][0];
    dp[0][1] = price[0][1];
    dp[0][2] = price[0][2];

    for(int j=1; j<N; j++){
      dp[j][0] = price[j][0] + Math.min(dp[j-1][1], dp[j-1][2]);
      dp[j][1] = price[j][1] + Math.min(dp[j-1][0], dp[j-1][2]);
      dp[j][2] = price[j][2] + Math.min(dp[j-1][0], dp[j-1][1]);
    }
    System.out.println(Math.min(Math.min(dp[N-1][0], dp[N-1][1]), dp[N-1][2]));
    sc.close();
  }
  
}
