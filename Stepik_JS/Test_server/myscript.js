function sayHi() {
    alert("Hi!")
}
// window.sayHi();
// alert(window.innerHeight);


// // Покрасть всё в красный
// document.body.style.background = "red";
// // Вернуть как было
// setTimeout(() => document.body.style.background = "", 1000);

// // Вернёт инфу о браузере
// alert(navigator.userAgent)


// Инфа о URL

// var btn = document.createElement("button");

// btn.appendChild(document.createTextNode("КНОПКА"));



// function sendForm(e){
     
//     // получаем значение поля key
//     var keyBox = document.search.key;
//     var val = keyBox.value;
//     if(val.length>5){
//         alert("Недопустимая длина строки");
//         e.preventDefault();
//     }   
//     else
//         // alert("Отправка разрешена");
//         document.write('!!!!!!')
//         var data = {
//             login: "Bob",
//             messages_: "I'm the best!"
//         }
//         var json = JSON.stringify(user);
//         var request = new XMLHttpRequest();
//         request.open("POST", "http://127.0.0.1:5000/test");
//         request.setRequestHeader('Content-type', 'application/json; charset=utf-8');
//         request.send(json);
// }
 
// var sendButton = document.search.send;
// console.log(sendButton)
// sendButton.addEventListener("click", sendForm);




document.write('!!!!!!')

var data = {
    login: "Bob",
    messages_: "I'm the best!"
}

var json = JSON.stringify(data);
var request = new XMLHttpRequest();
request.open("POST", "http://127.0.0.1:5000/test");
request.setRequestHeader('Content-type', 'application/json; charset=utf-8');
request.send(json);

console.log(request)
// typeof(request)
// responseXML