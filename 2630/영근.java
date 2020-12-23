import java.util.Scanner;

public class Main {
	public static int [][] MAP;
	public static int[] color = new int[2];
	public static final int  failure = -1;
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		MAP = new int[N][N];
		setUp(scanner);
		search(0,0,N);
		System.out.println(color[0]);
		System.out.println(color[1]);
	}
	
	public static void setUp(Scanner scanner) {
		for(int i=0;i<MAP.length;i++) {
			for(int j=0;j<MAP.length;j++) {
				int temp = scanner.nextInt();
				MAP[i][j]=temp;
			}
		}
	}
	
	public static void search(int startX,int startY,int size) {
		final int isFull = verify(startX,startY,size);
		
		if(isFull!=failure) {
			color[isFull]++;
			return;
		}
		//좌상
		search(startX,startY,size/2);
    //우상
		search(startX,startY+size/2,size/2);
    //좌하
		search(startX+size/2,startY,size/2);
    //우하
		search(startX+size/2,startY+size/2,size/2);
	}
	
	// -1 실패
	// 0 하얀색
	// 1 파란색
	public static int verify(int startX,int startY,int size) {
		final int startColor = MAP[startX][startY];
		for(int i=startX;i<startX+size;i++) {
			for(int j=startY;j<startY+size;j++) {
				if(startColor != MAP[i][j]) {
					return failure;
				}
			}
		}
		return startColor;
	}
	
}
