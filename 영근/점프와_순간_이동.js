function solution(n)
{
    let ans = 0;
    while(n!==0){
        if(n%2===1){
            ans++;
            n-=1;
            continue;
        }
        n=Math.floor(n/2);
    }
    return ans;
}