package 동적프로그래밍;

import java.util.Collection;
import java.util.Collections;
import java.util.Scanner;

public class MainClass11053 {
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    Integer[] A = new Integer[N];
    Integer[] dp = new Integer[N];
    for(int i=0; i<N; i++){
      A[i] = sc.nextInt();
      dp[i] = 1;
    }
    int max_length = 0;
    for(int j=0; j<N; j++){
      // System.out.println(max_length);
      for (int k=0; k<j; k++){
        if(A[j] > A[k]){
         dp[j] = Math.max(dp[j], dp[k]+1);
        }
      }
      max_length = Math.max(dp[j],max_length);
    }
    System.out.println(max_length);
  }
}
