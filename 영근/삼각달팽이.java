class Solution {
    public int[] goX={1,0,-1};
    public int[] goY={0,1,-1};
    public int[] solution(int n) {
        int[][] map = mapping(n);
        return ans(map,n);
    }
    
    public int[][] mapping(int n){
        //create mapping
        int[][] map = new int[n][n];
        int run = (n+1)*n/2;
        int count = 0;
        int currentX=0;
        int currentY=0;
        int number=1;
        
        // 0이면 아래로 탐색, 1이면 오른쪽으로 탐색, 2이면 위로 탐색
        int mod = 0;
        while(count<run){
            
            map[currentX][currentY]=number;
            
            //아래로 탐색
            if(mod==0){
                if(currentX+1==n||map[currentX+1][currentY]!=0){
                    mod = (mod+1)%3;
                }
            }
            //오른쪽으로 탐색
            else if(mod==1){
                if(currentY+1==n||map[currentX][currentY+1]!=0){
                    mod=(mod+1)%3;
                }
            }
            //위쪽으로 탐색
            else{
                if(currentX-1<0||currentY-1<0||map[currentX-1][currentY-1]!=0){
                    mod=(mod+1)%3;
                }
            }
            currentX+=goX[mod];
            currentY+=goY[mod];
            count++;
            number++;
        }
        return map;
    }
    
    public int[] ans(int[][] map,int n){
        int[] answer = new int[(n+1)*n/2];
        int count=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<=i;j++){
                answer[count++]=map[i][j];
            }
        }
        return answer;
    }
}