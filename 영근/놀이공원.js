// Run by Node.js
const readline = require('readline');

const inputs=[];
const TRASH = 1;
const EMPTY = 0;
const MAX_VALUE = 987654321;

let map = [];

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	for await (const line of rl) {
		inputs.push(line);
	}
	testCase();
	process.exit();
})();

function testCase(){
	const T = Number(inputs.shift()); // T
	for(let t=0;t<T;t++){
		start();
	}
}

function start(){
	const [N,K] = inputs.shift().split(" ").map((input)=>Number(input));
	map = [];
	for(let i=0;i<N;i++){
		const areaInfo = inputs.shift().split(" ").map((input)=>Number(input));
		map.push(areaInfo);
	}
	console.log(search(N,K));
}

function search(N,K){
	let answer=MAX_VALUE;
	for(let i=0;i<N;i++){
		for(let j=0;j<N;j++){
			answer = Math.min(answer,countTrash(i,j,K));
		}
	}
	return answer;
}

function countTrash(x,y,K){
	let counter = 0;
	
	if(x<0||x+K>map.length||y<0||y+K>map[x].length){
		return MAX_VALUE;
	}
	
	for(let i=x;i<x+K;i++){
		for (let j=y;j<y+K;j++){
			if(map[i][j]===TRASH){
				counter++;
			}
		}
	}
	
	return counter;
}