function solution(arr) {
  const answer = [0,0];
  const n = arr.length;
  divide(arr,answer,0,0,n);
  return answer;
}

function divide(arr,ans,x,y,n){
  if(isFull(arr,x,y,n)){
      ans[arr[x][y]]++;
      return;
  }
  const halfLength = n/2;
  // 2사분면
  divide(arr,ans,x,y,halfLength);
  // 1사분면
  divide(arr,ans,x,y+halfLength,halfLength);
  // 3사분면 
  divide(arr,ans,x+halfLength,y,halfLength);
  // 4사분면
  divide(arr,ans,x+halfLength,y+halfLength,halfLength);
}

function isFull(arr,x,y,n){
  const flag = arr[x][y];
  for(let i=x;i<x+n;i++){
      for(let j=y;j<y+n;j++){
          if(flag!==arr[i][j]){
              return false;
          }
      }
  }
  return true;
}

const arr1=[[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]];
const arr2=[[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]];

const result1=[4,9];
const result2=[10,15];

solution(arr1);