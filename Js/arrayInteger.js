function arrayNums(array_nums) {
    
    for (let x = 1; x <= 100000; x++){
        if (!array_nums.includes(x)) {
            return x;
        }
            
    }
}
console.log(arrayNums([1, 3, 6,4,1,2]))
console.log(arrayNums([1, 2, 3]))
console.log(arrayNums([-1,-3]));