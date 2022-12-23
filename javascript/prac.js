const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let count = 0;

rl.on('line', (input) => {
  console.log(`Recived : ${input}`);
  count += 1;
  if (count === 3) {
    rl.close();
  }
  // 위의 경우 입력을 3번 받은 후 close한다
});