document.querySelector("#button").addEventListener("click", getdrinks);


function getdrinks(){
  let apiurl = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=";
  let userinput = document.querySelector("input").value;
  let newurl = apiurl + userinput;

fetch(newurl)
  .then((res) => res.json()) // parse response as JSON
  .then((data) => {
    console.log(data);
    document.querySelector("img").src = data['drinks'][0]['strDrinkThumb'];
  document.querySelector("h2").innerText = data["drinks"][0]["strDrink"];
  document.querySelector("h4").innerText = data["drinks"][0]["strInstructions"];
  document.querySelector("#ingredients").innerText = data["drinks"][0]["strIngredient1"];
})
  .catch((err) => {
    console.log(`error ${err}`);
  });
}
