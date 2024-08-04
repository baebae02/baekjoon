package tree;
import java.util.Scanner;
//13116

public class MainClass13116 {
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int T = sc.nextInt();

    for(int i=0; i<T; i++){
      int A = sc.nextInt();
      int B = sc.nextInt();
      System.out.println(calculate(A,B));
    }
  }

  public static Integer calculate(Integer A, Integer B){
    while(!A.equals(B)){
      if (A <= B){
        B = Math.floorDiv(B, 2);
      } else {
        A = Math.floorDiv(A, 2);
      }
    }
    return A * 10;
  }
}