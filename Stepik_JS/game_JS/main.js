
function setup() {
    createCanvas(800,500);
    for (let i = 0; i < count; i+=1)
    {
        mass.push(randomInteger(30, 400))
    }
}

let x = 100
let y = 100
let gravity = 0.1
let yV = 0
let mass = []
let height = 100
let count = 1000

let gameInProgr = true

let flag_x = 0
let flag_y = 0


function draw(){
    
    if (gameInProgr)
    {
        chechScreen()
        background(200, 200, 200);
        drawBird()
        for (let i = 0; i < count; i+=1)
        {
            // console.log(x - i * 100, mass[i])
            drawRect(x - i * 100, mass[i])
        }
    }
    else
    {
        alert("Game Over")
        gameInProgr = true
        window.location.reload();
    }
    
}

function drawRect(xi, yi){
    rectMode(CORNERS)
    stroke(250, 0, 0);
    rect(790 - xi, 0, 800 - xi, yi)
    rect(790 - xi, yi + height, 800 - xi, 500)
}

function drawBird(){
    stroke(250, 0, 0);
    ellipse(400, y, 10 * 2);
    x += 1
    if (yV < 0)
        yV += gravity * 7 
    if (yV >= 0)
        yV += gravity
    y += yV
}



function keyPressed(){
    yV = -10
}

function chechScreen(){
    if (y >= 500)
    {
        gameInProgr = false
    }
    if (y < 0)
    {
        gameInProgr = false
    }
}
function checkBird(){

}

function randomInteger(min, max) {
    let rand = min + Math.random() * (max + 1 - min);
    return Math.floor(rand);
  }
  