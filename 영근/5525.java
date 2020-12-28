import java.io.IOException;
import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Scanner;

public class Main {
	final static String IO = "IO";
	final static char I ='I';
	final static char O = 'O';
	public static void main(String[] args) throws IOException {
		Scanner scanner = new Scanner(System.in);
		final int N = scanner.nextInt();
		final int M = scanner.nextInt();
		scanner.nextLine();
		final String S = scanner.nextLine();
		int ans = 0;
		int flag = 0;
		for(int i=0;i<M-2;i++) {
			char First = S.charAt(i);
			char Second = S.charAt(i+1);
			char Third = S.charAt(i+2);
			if(First == I && Second == O && Third == I) {
				flag++;
				i+=1;
			}else {
				flag = 0;
			}
			
			//end
			if(flag == N) {
				flag -=1;
				ans++;
			}
		}
		
		System.out.println(ans);
	}
}