const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line',  (line) => {
    input.push(line);
    rl.close();
}).on('close',  () => {

    let n = input;

    const solution = (n) => {

        if(n % 2 === 1)
            console.log((n+1)/2*((n + 1)/2));
        else
            console.log(n*(n+1)*(n+2)/6);

        /* let answer = 0;

        if (n % 2 === 0) {
            for (let i = 0; i <= n; i += 1) {
                if (i % 2 === 0) answer += i ** 2;
            }
        } else {
            for (let i = 0; i <= n; i += 1) {
                if (i % 2 === 1) answer += i;
            }
        }
        console.log(answer);
        return answer; */
    }
    solution(n);
    process.exit();
});

