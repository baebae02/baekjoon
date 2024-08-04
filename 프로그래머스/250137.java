class Solution {
  private int time;
  private int max_health;
  //[3,2,7] 20 [[1,15],[5,16],[8,6]]
  public int solution(int[] bandage, int health, int[][] attacks) {
      int answer = 0;
      int attack = 0;
      int continuous = -1;
      max_health = health;
      for(int[] a: attacks){
          time = Math.max(time, a[0]);
      }
      for(int c_t=0; c_t<=time; c_t++){
          // System.out.println("before"+c_t+"@@"+health+"@@"+continuous);
          if(attacks[attack][0] == c_t){
              health = health - attacks[attack][1];
              attack++;
              continuous = 0;
              if(health <= 0){
                  return -1;
              }
          } else{
              health = Math.min(max_health, health+bandage[1]);
              continuous++;
              if(continuous==bandage[0]){
              health = Math.min(max_health, health + bandage[2]);
              continuous = 0;
              }
          }
          // System.out.println("after"+c_t+"@@"+health+"@@"+continuous);
      }
      return health;
  }
}