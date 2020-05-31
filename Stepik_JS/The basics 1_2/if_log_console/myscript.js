function testSum(a, b) {
    var x;
    x = ((a * b) % (a + b)) * 2
    return x;
}


// var friend;
// friend = "Bo"
// hiJack = (friend == "Jack") ? "Hi, Jack!" : "Hi";

// if (friend == "Bob") {
//     console.log("Hi, Bob");
// }   
// else {
//     console.log("Hi,", friend);
// }

function testIF(a, b) {
    if (a > b) {
        return a + b;
    }
    else {
        return a * b;
    }
}


function testIF2(a, b) {
    return (a > b) ? a + b: a * b;
}


function test3(a, b) {
    if (a < b)
        return a + b;
    else if (a > b)
        return a - b;
    else 
        return a * b;       
}


function testCase(a) {
    switch(a) {
        case 0:
            return "Ноль";
        case 1:
            return "Один";
        case 2:
            return "Два";
        case 3:
            return "Три";
        case 4:
            return "Четыре";
        case 5:
            return "Пять";
        case 6:
            return "Шесть";
        case 7:
            return "Семь";
        case 8:
            return "Восемь";
        case 9:
            return "Девять";
    }
}

console.log(testCase(8))
