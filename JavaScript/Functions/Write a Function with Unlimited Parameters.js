function take_many_parameters(...args) {
    let total = 1;
    for (let i of args) total *= i;
    return total;
}

let x = take_many_parameters(2, 3, 4);
console.log(x)
