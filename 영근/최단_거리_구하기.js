const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

const inputs = [];
const PATH = 1;
const NOT_PATH=0;
const MAX_VALUE=987654321;

const moveX=[-1,0,1,0];
const moveY=[0,1,0,-1];

let map=[];
let isVisited=[];

rl.on("line", function(line) {
	inputs.push(line);
}).on("close", function() {
	run();
	console.log(map[map.length-1][map.length-1]);
	process.exit();
});

function run(){
	//map 생성
	for(let i=0;i<Number(inputs[0]);i++){
		map.push([]);
	}
	//숫자로 변환
	for(let i=1;i<=map.length;i++){
		const strings = inputs[i].split(" ");
		strings.forEach((number)=>{
			map[i-1].push(Number(number));
		});
	}
  dfs();
}

function dfs(x=0,y=0,acc=1){
	// 지나갈 수 없는 길이라면 return
	if(map[x][y]===0||isOut(x,y)){
		return;
	}
	
	// 재방문시 더 비 효율적이라면 return
	if(map[x][y]!==0&&map[x][y]!==1&&map[x][y]<=acc){
		return;
	}
	
	map[x][y]=acc;
	
	for(let i=0;i<moveX.length;i++){
		const nextX = x+moveX[i];
		const nextY = y+moveY[i];
		if(!isOut(nextX,nextY) && map[nextX][nextY] !== 0){
			if(map[nextX][nextY] === 1){
				dfs(nextX,nextY,acc+1);
			}else if(map[nextX][nextY] > acc+1){
				dfs(nextX,nextY,acc+1);
			}
		}
	}
}

function isOut(x,y){
	if(x<0||x>=map.length||y<0||y>=map[x].length){
		return true;
	}
	return false;
}

