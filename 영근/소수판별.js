// Run by Node.js

const readline = require("readline");
const FALSE = 'False';
const TRUE='True';

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

rl.on("line", function(line) {
	console.log(isPrime(Number(line)));
	rl.close();
}).on("close", function() {
	process.exit();
});

function isPrime(n){
	if(n===0||n===1){
		return FALSE;
	}
	for(let i=2;i<=Math.sqrt(n);i++){
		if(n%i===0){
			return FALSE;
		}
	}
	return TRUE;
}