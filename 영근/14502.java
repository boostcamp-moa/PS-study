import java.io.IOException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
  public static int[] mvx = {-1, 0, 1, 0};
  public static int[] mvy = {0, 1, 0, -1};
  public static int[][] map;
  public static int[][] originalMap;
  public static int MAX = 0;

  public static void main(String[] args) throws IOException {
    Scanner scanner = new Scanner(System.in);
    int N = scanner.nextInt();
    int M = scanner.nextInt();
    map = new int[N][M];
    originalMap = new int[N][M];
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        originalMap[i][j] = scanner.nextInt();
      }
    }
    batch(-1, 0);
    System.out.println(MAX);
  }

  public static void batch(int index, int count) {
    for (int i = index + 1; i < originalMap.length * originalMap[0].length; i++) {
      int x = i / originalMap[0].length;
      int y = i % originalMap[0].length;

      if (originalMap[x][y] == 0) {
        originalMap[x][y] = 1;
        
        if (count == 2) {
          bfs();
        } else {
          batch(i, count + 1);
        }
        
        originalMap[x][y] = 0;
      }
    }
  }

  public static void bfs() {
    copy();
    Queue<Pair> q = new LinkedList<>();

    for (int i = 0; i < map.length; i++) {
      for (int j = 0; j < map[0].length; j++) {
        if (map[i][j] == 2) {
          q.add(new Pair(i, j));
        }
      }
    }

    while (!q.isEmpty()) {
      Pair out = q.poll();
      for (int i = 0; i < 4; i++) {
        int mvvx = out.x + mvx[i];
        int mvvy = out.y + mvy[i];
        if (check(mvvx, mvvy) && map[mvvx][mvvy] == 0) {
          map[mvvx][mvvy] = 2;
          q.add(new Pair(mvvx, mvvy));
        }
      }
    }

    MAX = Math.max(MAX, count());
  }

  public static int count() {
    int ans = 0;
    for (int i = 0; i < map.length; i++) {
      for (int j = 0; j < map[0].length; j++) {
        if (map[i][j] == 0) {
          ans++;
        }
      }
    }
    return ans;
  }

  public static boolean check(int x, int y) {
    if (x < 0 || x >= map.length || y < 0 || y >= map[0].length) {
      return false;
    }
    return true;
  }

  public static void copy() {
    for (int i = 0; i < originalMap.length; i++) {
      for (int j = 0; j < originalMap[0].length; j++) {
        map[i][j] = originalMap[i][j];
      }
    }
  }

}


class Pair {
  int x;
  int y;

  Pair() {

  }

  Pair(int x, int y) {
    this.x = x;
    this.y = y;
  }
}