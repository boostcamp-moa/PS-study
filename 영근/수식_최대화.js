const priorities = [];
const expression = ['*','-','+'];
const mark = [false,false,false];
function solution(expression){
  let answer = 0;
  shuffle(0,[]);
  priorities.forEach(priority=>{
    answer = Math.max(answer,Math.abs(run(priority,expression,0)));
  });
  return answer;
}

function shuffle(position,array){
  if(position===3){
    priorities.push([...array]);
    return;
  }

  for(let i=0;i<expression.length;i++){
    if(!mark[i]){
      array.push(expression[i]);
      mark[i]=true;
      shuffle(position+1,array);
      array.pop();
      mark[i]=false;
    }
  }
}

function run(priority,expression){
  return splitExpression(priority,expression,0);
}

function splitExpression(priority,express,n){
  if(n==3){
    return Number(express);
  }
  const values = [];
  express.split(priority[n]).forEach((curr)=>{
    let test=curr;
    if(!isNumber(curr)){
      test = splitExpression(priority,curr,n+1);
    }
    values.push(test);
  });
  return calcExpress(priority[n],values);
}

function calcExpress(express,numbers){
  if(express==='*'){
    return numbers.reduce((acc,curr)=>{
      return acc*Number(curr);
    },1);
  }else if(express==='+'){
    return numbers.reduce((acc,curr)=>{
      return acc + Number(curr);
    },0);
  }else{
    return numbers.slice(1).reduce((acc,curr,id)=>{
      return acc-Number(curr);
    },numbers[0]);
  }
}

function isNumber(number){
  return !Number.isNaN(Number(number));
}