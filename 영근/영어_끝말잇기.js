/*
1 번호 순으로 한 사람씩 단어를 말함
2. 마지막 사람이 말한 다음에 다시 1번부터 돌아감
3. 앞 사람이 말한 마지막 단어로 시작하는 단어를 말해야함
4. 이전에 등장한 단어는 사용할 수 없음
5. 한글자인 단어 안됨

목표 : 

가장 먼저 탈락하는 사람의 번호와, 몇 번째 차례에서 탈락했는지를 배열에 담아 리턴하라

탈락자가 존재하지 않으면 0,0을 리턴하라.
*/
function solution(n, words) {
  let answer = [0,0];
  const memo = new Map();
  let currentN = 0;
  let before='';
  words.some((word,id)=>{
      if(memo.has(word)){
          answer[0]=currentN+1;
          answer[1]=Math.floor(id/n)+1;
          return true;
      }
      
      const lastChar = before.charAt(before.length-1);
      const firstChar = word.charAt(0);
      
      if(lastChar!==''&&(lastChar!==firstChar)){
          answer[0]=currentN+1;
          answer[1]=Math.floor(id/n)+1;
          return true;
      }
      
      memo.set(word,true);
      currentN = (currentN+1)%n;
      before = word;
      return false;
  });

  return answer;
}