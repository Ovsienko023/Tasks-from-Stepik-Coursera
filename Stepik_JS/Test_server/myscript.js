function test_post_request() {
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

    // request.onload = () => console.log(request.status)
    request.onload = () => console.log(request.response)
    request.onload = function () {
        if (request.status == "200") {
            document.write('данные отправлены!!!');
        }
}
}
// document.write(test_post_request())


// function sayHi() {
//     alert("Hi!")
// }
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



function sendForm(e){
     
    // получаем значение поля key
    var keyBox = document.search.key;
    var val = keyBox.value;
    if(val.length>15){
        alert("Недопустимая длина строки");
        e.preventDefault();
    }   
    else
        // alert("Отправка разрешена");
        document.write('Отправка разрешена')
        var data = {
            login: "Bob",
            messages_: val
        }
        var json = JSON.stringify(data);
        var request = new XMLHttpRequest();
        request.open("POST", "http://127.0.0.1:5000/test");
        request.setRequestHeader('Content-type', 'application/json; charset=utf-8');
        request.send(json);
        document.write('!!');
        request.onload = () => console.log(request.response)
        request.onload = function () {
            if (request.status == "200") {
                document.write('____данные отправлены!');
        }
}
}

var sendButton = document.search.send;
console.log(sendButton);
sendButton.addEventListener("click", sendForm);
