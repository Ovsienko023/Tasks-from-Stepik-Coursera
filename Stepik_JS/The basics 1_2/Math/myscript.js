// document.write(Math.PI)
// document.write('\n_____', Math.sqrt(24))
// document.write('\n_____', Math.sin(1))


function testMath(a) {
    var rad = ((a * Math.PI) / (180));
    return Math.sin(rad);
}

function testMath2(a, b, c) {
    var rad = ((c * Math.PI) / (180));
    var s = ((1 / 2) * a * b * Math.sin(rad));
    return s;
}

function testMath3(a, b, c, d) {
    var num_max = Math.max(a, b, c, d);
    var num_min = Math.min(a, b, c, d);
    return Math.floor(num_max / num_min);
}

Math.sqrt(x)             // возвращает квадратный корень из аргумента
Math.pow(base, exponent) // возводит число "base" в степень "exponent"
Math.log(x)              // вычисляет натуральный (по основанию е) логарифм числа
Math.exp(x)              // вычисляет экспоненту - значение числа е в степени аргумента "х"
Math.random()            // возвращает случайное число от 0 (включительно) до 1

function testMath4(a, b) {
    return a ** b;
}