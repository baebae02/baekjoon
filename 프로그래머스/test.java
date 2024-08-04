package 프로그래머스;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

class Node{
  int data;
  Node ln;
  Node rn;
  public Node(int val){
    data = val;
    ln = null;
    rn = null;
  }
}

public class test {

  
}

public class DFS {
  Node root;
  public static void main(String args[]){
    DFS tree = new DFS();

  }
  public void DFS(Node root){
    if(root == null) return;
    else{
      DFS(root.ln);
      DFS(root.rn);
    }
  }
}

public class BFS{
  Node root;
  public static void main(String args[]){

  }

  public void BFS(Node root){
    Queue<Node> Q = new LinkedList<>();
    Q.offer(root);
    int L = 0;
    while(!Q.isEmpty()){
      int len = Q.size();
      for(int i=0; i<len; i++){
        Node current = Q.poll();
        if(current.ln != null){
          Q.offer(current.ln);
        }
        if(current.rn != null){
          Q.offer(current.rn);
        }
      }
    }
  }
}


public class Main{
  public final static int GRAPH_LIST_SIZE = 9;
  public static boolean[] visited = new boolean[GRAPH_LIST_SIZE];
  public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();

  public static void main(String args[]){
    for(int i=0; i<GRAPH_LIST_SIZE; i++){
      graph.add(new ArrayList<Integer>);
    }
  }
  public static void dfs(int node){
    // 방문 처리
    visited[node] = true;
    for(int neighbor: graph.get(node)){
      if(visited[neighbor] == false){
        dfs(neighbor);
      }
    }
  }
  public static void bfs(int node){
    Queue<Integer> queue = new LinkedList<Integer>();
    queue.offer(node);
    visited[node] = true;
    while(!queue.isEmpty()){
      int current = queue.poll();
      for(int neightbor: graph.get(current)){
        if(visited[neightbor] == false){
          queue.offer(neightbor);
          visited[neightbor] = true;
        }
      }
    }
  }
}