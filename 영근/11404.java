import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static int map[][];
    public static int value[][];
    public static int INF=187654321;
    public static void main(String[] args) throws IOException {
        Scanner sc=new Scanner(System.in);
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        int m=Integer.parseInt(br.readLine());
        value=new int[n][n];
        for(int i=0;i<n;i++){
            Arrays.fill(value[i],INF);
        }

        for(int i=0;i<m;i++){
            StringTokenizer st=new StringTokenizer(br.readLine()," ");
            int from=Integer.parseInt(st.nextToken())-1;
            int to=Integer.parseInt(st.nextToken())-1;
            int cost=Integer.parseInt(st.nextToken());

            value[from][to]=Math.min(value[from][to],cost);
        }

        for(int i=0;i<n;i++){
            value[i][i]=0;
        }

        for(int k=0;k<n;k++){
            for(int i=0;i<n;i++){
                for(int j=0;j<n;j++){
                    value[i][j]=Math.min(value[i][j],value[i][k]+value[k][j]);
                }
            }
        }

        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(value[i][j]>=INF)
                    System.out.print("0 ");
                else
                    System.out.print(value[i][j]+" ");
            }

            System.out.print("\n");
        }
    }
}