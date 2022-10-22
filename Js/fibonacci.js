function fibonacci(num){
    const fib = [0, 1]
    let sum = 0;

    for(let i=2; i<num; i++){
        fib[i] = fib[i-1] + fib[i-2]

    }
    return fib;
}

console.log(fibonacci(8))