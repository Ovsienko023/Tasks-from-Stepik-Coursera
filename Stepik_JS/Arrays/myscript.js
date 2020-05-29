function testArray(a, b) {
    var c = a.concat(b);
    var sum_arr = 0;
    for (let i in c)
        sum_arr = sum_arr + c[i];
    return sum_arr;
}

// testArray([8, 1, 1, 7, 4, 0], [5, 8, 5, 4, 8])

var myArray = [8, 1, 1, 7, 4, 0];

console.log(myArray.sort());

delete myArray[0]
console.log(myArray);