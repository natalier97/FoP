let total = 0


document.querySelector('#clear').addEventListener('click', clear)
document.querySelector("#plus").addEventListener("click", plus);
document.querySelector("#equals").addEventListener("click", equal);
document.querySelector("#minus").addEventListener("click", minus);
document.querySelector("#multiply").addEventListener("click", multiply);
document.querySelector("#divide").addEventListener("click", divide);
document.querySelector('#zero').addEventListener('click', zero)
document.querySelector('#one').addEventListener('click', one)
document.querySelector("#two").addEventListener("click", two);
document.querySelector("#three").addEventListener("click", three);
document.querySelector("#four").addEventListener("click", four);
document.querySelector("#five").addEventListener("click", five);
document.querySelector("#six").addEventListener("click", six);
document.querySelector("#seven").addEventListener("click", seven);
document.querySelector("#eight").addEventListener("click", eight);
document.querySelector("#nine").addEventListener("click", nine);

 
let resultString = ''

function zero() {
  resultString += '0'
  document.querySelector("#placeToPutResult").innerText = resultString;
}

function one() {
  resultString += "1";
  document.querySelector("#placeToPutResult").innerText = resultString;
}

function two() {
  resultString += "2";
  document.querySelector("#placeToPutResult").innerText = resultString;
}


function three() {
  resultString += "3";
  document.querySelector("#placeToPutResult").innerText = resultString;
}

function four() {
  resultString += "4";
  document.querySelector("#placeToPutResult").innerText = resultString;
}

function five() {
  resultString += "5";
  document.querySelector("#placeToPutResult").innerText = resultString;
}

function six() {
  resultString += "6";
  document.querySelector("#placeToPutResult").innerText = resultString;
}

function seven() {
  resultString += "7";
  document.querySelector("#placeToPutResult").innerText = resultString;
}


function eight() {
  resultString += "8";
  document.querySelector("#placeToPutResult").innerText = resultString;
}

function nine() {
  resultString += "9";
  document.querySelector("#placeToPutResult").innerText = resultString;
}

//operators

function plus() {
 resultString += '+'
document.querySelector("#placeToPutResult").innerText = resultString;
}

function minus() {
  resultString += "-";
  document.querySelector("#placeToPutResult").innerText = resultString;
}

function multiply() {
  resultString += "*";
  document.querySelector("#placeToPutResult").innerText = resultString;
}

function divide() {
  resultString += "/";
  document.querySelector("#placeToPutResult").innerText = resultString;
}

//final operators
function equal() {
let result = eval(resultString)
document.querySelector("#placeToPutResult").innerText = result;
resultString = result;
}

function clear() {
  total = "";
  resultString = '';
  document.querySelector("#placeToPutResult").innerText = total;
}
