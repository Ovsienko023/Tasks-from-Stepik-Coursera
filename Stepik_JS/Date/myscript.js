// var myDate = new Date()  //Mon May 15 2017 19:20:25 GMT+0300 (RTZ 2 (зима))
// var myDate = new Date("December 14, 1975 12:10:00") //Sun Dec 14 1975 12:10:00 GMT+0300 (RTZ 2 (зима))
// var myDate = new Date(1989, 6, 14)  //Fri Jul 14 1989 00:00:00 GMT+0400 (RTZ 2 (лето))
// var myDate = new Date(1998, 6, 14, 11, 20, 00) //Tue Jul 14 1998 11:20:00 GMT+0400 (RTZ 2 (лето))

// document.write(myDate)

// var currentDate = new Date();
// var newYearDate = new Date(2021, 0, 1);
// var nowDate = new Date(2020, 4, 30);

// if (+currentDate == +newYearDate) {
//     document.write("С новым годом!");
//     // alert("Поздравляем с Новым, 2018-м Годом! Ура!!!")
// }
// else{
//     document.write("!  ");
// }


// var myDate = new Date()
// // Вернёт день недели 
// document.write(myDate.getDay())


var a = '19 October 1909 10:27';
var b = '28 March 1909 00:59';

function testDateTime(a, b) {
    var fin_date;
    date_1 = new Date(a);
    date_2 = new Date(b);
    
    if (+date_1 > +date_2)
        fin_date = date_1.getDay();
    else
        fin_date = date_2.getDay();
    switch(fin_date) {
        case 0:
            return "Воскресенье";
        case 1:
            return "Понедельник";
        case 2:
            return "Вторник";
        case 3:
            return "Среда";
        case 4:
            return "Четверг";
        case 5:
            return "Пятница";
        case 6:
            return "Суббота";
    }

}



document.write(testDateTime(a, b))