function Person(name, age, year) {
    this.name = name
    this.age = age
    this.year = year
}

Person.calls = function() {
    console.log("date:", this.name, this.age)
    
}

var man = new Person("Bob", "105", "1895")
// console.log(man.name, man.age, man.year) 

// Второй вариант объявления объекта

var persons = {
    name : 'Kik',
    age : '25',
    year : '2017'
}

persons.sayAge = function() {
    console.log("Person is:", this.age)
}

persons.sayAll = function() {
    for (var i in this) {
        console.log(i, 'is', this[i])
    }
}
// persons.sayAge()
// persons.sayAll()



function testStr(a, b) {
    return a.length + b.length;
}
// console.log(testStr('1231231', '12312312'))


function testStr2(str, n) {
    return str[n - 1];
}

// console.log(testStr2('Ithardlycousinmealways', 19))


var cat = 'cat';
var dog = ' dog';
var zoo;

// zoo = cat.concat(dog)
// console.log(zoo)

var zoo2 = 'cat,dog,turtle';
var lst_zoo2 = zoo2.split(',');

// console.log(lst_zoo2);

// for (let i in lst_zoo2)
//     console.log(lst_zoo2[i]);

function testStr3(a, b) {
    a = a.toUpperCase();
    b = b.toLowerCase();
    return a + b;
}

function testStr4(a, b) {
    return a.indexOf(b, 0);
}
