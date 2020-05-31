function testFactorial(a){
    var x = 1;
    for (let i = 1; i <= a; i++) {
        x = x * i;
    }
    return x;
}



function testWhile(a) {
    var x = 1;
    var sums = 0;
    while (a >= x) {
        if (x % 2 == 0)
            sums = sums + x;
        x++;
    }
    return sums;
}


function testCycle(n){
    var sums = 0;
    for (let i = 1; i <= n; i++)
        sums = sums + i;
    return sums;
}  


function testCycle2(k, n) {
    var lst = '';
    for (let i = 1; i <= k; i++)
        lst = lst + String(n) + ' ';
        
    return lst;
}


function testCycle3(a, b) {
    var lst = '';
    for (let x=1; x <= b; x++) {
        if ((x <= b) && (x >= a))
            lst = lst + String(x) + ' ';
    }
    return lst;
}


function printTest() {
    document.write('Hello');
    alert('qweqw')
    console.log('dsasd')
}


function my_function(n) {
    final_srt = '';
    if (n < 1)
        return '';
    else
        a = my_function(n-1);
    final_srt = final_srt + String(n) + ' ';
    return final_srt;
}

console.log(my_function(5))
