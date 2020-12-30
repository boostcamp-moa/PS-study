function solution(s) {
  const answer = [0,0];
  runSolution(answer,s);
  return answer;
}

function runSolution(answer,s){
  if(s==='1'){
    return;
  }
  const totalZero = countZero(s);
  answer[1]+=totalZero;
  const ones=convertNextBinary(s,totalZero);
  answer[0]+=1;
  runSolution(answer,ones);
}

function countZero(s){
  const arrayS= [...s];
  return arrayS.filter((number)=>number==='0').length;
}

function convertNextBinary(s,n){
  const ones = s.length-n;
  return ones.toString(2);
}