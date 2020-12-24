import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
	public static int[] start;
	public static int[] v1;
	public static int[] v2;
	public static int[] visit;
	public static ArrayList<ArrayList<Point>> vertex = new ArrayList<>();
	public static final int MAX = 987654321;
	public static void main(String[] args) throws IOException {
		BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
		String[] temp = bf.readLine().split(" ");
		int N = Integer.parseInt(temp[0]);
		int E = Integer.parseInt(temp[1]);
		dikLength(N);
		vertexInit(N,E,bf);
		
		temp = bf.readLine().split(" ");
		int v1Point = Integer.parseInt(temp[0])-1;
		int v2Point = Integer.parseInt(temp[1])-1;
		
    // start 지점에 대한 최단거리 구함
		startDik(start,0);
    // v1 지점에 대한 최단거리 구함
		startDik(v1,v1Point);
    // v2 지점에 대한 최단거리 구함
		startDik(v2,v2Point);
		
    // start-v1-v2-end 에 대한 최단거리, start-v2-v1-end 에 대한 최단거리를 비교후 가장 짧은 부분을 선택함
		long ans = Math.min((long)start[v1Point]+(long)v1[v2Point]+(long)v2[N-1], (long)start[v2Point]+(long)v2[v1Point]+(long)v1[N-1]);
		if(ans >=MAX) {
			System.out.println(-1);
		}else {
			System.out.println(ans);
		}
	}
	
  //다익스트라
	public static void startDik(int[] list,int startPoint){
		visitReset();
		
		list[startPoint]=0;
		
		int next = startPoint;
		for(int i=0;i<list.length-1;i++) {
			visit[next]=1;
			updateDik(list,next);
			next = nextPoint(list,next);
		}
		
	}
	
  // 다익스트라 리스트 업데이트
	public static void updateDik(int[] list,int startPoint) {
		ArrayList<Point> canGoTo = vertex.get(startPoint);
		for(int i=0;i<canGoTo.size();i++) {
			Point node = canGoTo.get(i);
			list[node.target] = Math.min(list[node.target], list[startPoint]+node.value);
		}
	}
	
  // 다음 지점을 구함
	public static int nextPoint(int[] list,int startPoint) {
		int next = startPoint;
		int minValue = MAX;
		
		for(int i=0;i<list.length;i++) {
			if(visit[i]!=0) {
				continue;
			}
			
			if(minValue>list[i]) {
				minValue=list[i];
				next=i;
			}
		}
		return next;
	}
	
  // 방문 리스트 초기화
	public static void visitReset() {
		for(int i=0;i<visit.length;i++) {
			visit[i]=0;
		}
	}
	
  // 배열 초기화
	public static void dikLength(int N) {
		start = new int[N];
		v1 = new int[N];
		v2 = new int[N];
		visit = new int[N];
		for(int i=0;i<N;i++) {
			start[i]=MAX;
			v1[i]=MAX;
			v2[i]=MAX;
		}
	}
	
  // 간선 리스트 생성
	public static void vertexInit(int N,int E,BufferedReader bf) throws IOException {
		for(int i=0;i<N;i++) {
			vertex.add(new ArrayList<Point>());
		}
		
		for(int i=0;i<E;i++) {
			String[] temp = bf.readLine().split(" ");
			int source = Integer.parseInt(temp[0])-1;
			int target = Integer.parseInt(temp[1])-1;
			int value = Integer.parseInt(temp[2]);
			
			vertex.get(source).add(new Point(target,value));
			vertex.get(target).add(new Point(source,value));
		}
	}
}

class Point{
	int target;
	int value;
	Point(int target,int value){
		this.target=target;
		this.value=value;
	}
}
