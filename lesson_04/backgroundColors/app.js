document.querySelector("#turnRed").addEventListener("click", turnRedFunction);
document.querySelector("#turnBlue").addEventListener("click", turnBlueFunction);
document.querySelector("#turnPurple").addEventListener("click", turnPurpleFunction);
document.querySelector("#turnYellow").addEventListener("click", turnYellowFunction);
document.querySelector("#turnOrange").addEventListener("click", turnOrangeFunction);
document.querySelector("#turnGreen").addEventListener("click", turnGreenFunction);
document.querySelector("#turnRandom").addEventListener("click", turnRandomFunction);


function turnRedFunction() {
  document.querySelector("body").style.backgroundColor = "red";
}

function turnBlueFunction() {
  document.querySelector("body").style.backgroundColor = "blue";
}

function turnPurpleFunction() {
  document.querySelector("body").style.backgroundColor = "purple";
}

function turnYellowFunction() {
  document.querySelector("body").style.backgroundColor = "yellow";
}

function turnOrangeFunction() {
  document.querySelector("body").style.backgroundColor = "orange";
}

function turnGreenFunction() {
  document.querySelector("body").style.backgroundColor = "green";
}

function turnRandomFunction() {
  let colors = ['red', 'blue', 'green', 'orange', 'purple'];

  document.querySelector("body").style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
}