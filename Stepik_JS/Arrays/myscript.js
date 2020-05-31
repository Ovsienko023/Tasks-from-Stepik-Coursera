function testArray(a, b) {
    var c = a.concat(b);
    var sum_arr = 0;
    for (let i in c)
        sum_arr = sum_arr + c[i];
    return sum_arr;
}

// testArray([8, 1, 1, 7, 4, 0], [5, 8, 5, 4, 8])

// var myArray = [8, 1, 1, 7, 4, 0];

// console.log(myArray.sort());

// delete myArray[0]
// console.log(myArray);

function testArray2(a, b) {
    var lst_arr;
    lst_arr = a.concat(b).split('');
    lst_arr.unshift('Иванов');
    lst_arr = lst_arr.reverse().join('')
    return lst_arr;
}
document.write(testArray2('4326', '297515'))
// console.log(testArray2('4326', '297515'))