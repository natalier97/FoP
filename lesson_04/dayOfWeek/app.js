document.querySelector('#check').addEventListener('click', checkDay)

function checkDay() {
  
  const day = document.querySelector('#day').value
  let weekdays = 'monday, tuesday, wednesday, thursday, friday'
  let weekends = 'saturday, sunday'
  let anyday = weekdays + weekends;

  for (let i = 0; i < anyday.length; i++){
        if (anyday.indexOf(day.toLowerCase()) == -1){
         document.querySelector("#placeToSee").innerText = 'not a day of the week';
        } 
        else if (weekdays.indexOf(day.toLowerCase()) > -1 ){
          document.querySelector("#placeToSee").innerText = 'this is a WEEKday'
        } else {document.querySelector("#placeToSee").innerText = 'party bc this is the WEEKEND!'}
      }

  // logic goes here
 
}
