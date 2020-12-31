/*
1~3000 사이의 소수를 구한다. (에라토스테네스의체)
그리고 완전탐색으로 각 수를 더해가며 경우의 수를 찾아낸다.
*/
const prime=new Array(3001);
function solution(nums) {
  era();
  prime[0]=false;
  prime[1]=false;
  return run(nums,0,0,0);
}

function era(){
  for(let i=2;i<prime.length;i++){
    for(let j=2*i;j<prime.length;j+=i){
      prime[j]=false;
    }
  }
}

function run(nums,position,n,acc){
  if(n!==3&&position===nums.length){
    return 0;
  }

  if(n===3 && prime[acc]===undefined){
    return 1;
  }else if(n===3 && !prime[acc]){
    return 0;
  }

  let ans=0;
  //선택을 하는 경우의 수
  ans += run(nums,position+1,n+1,acc+nums[position]);
  //선택을 하지 않는 경우의 수
  ans+=run(nums,position+1,n,acc);

  return ans;
}