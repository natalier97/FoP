document.querySelector('button').addEventListener('click', getFetch)

async function getFetch() {
    const choice = document.querySelector('#pokemon').value
    const url = 'https://pokeapi.co/api/v2/pokemon/'+choice

    let data = await fetch(url)
    let pokemonInfo = await data.json()

    console.log(pokemonInfo)

    document.querySelector("h2").innerText = pokemonInfo['name'];
    if (document.querySelector('#shiny').checked){
        document.querySelector("img").src = pokemonInfo["sprites"]["front_shiny"];
    } else {document.querySelector("img").src = pokemonInfo["sprites"]["front_default"]}
    
    document.querySelector("h3").innerText = pokemonInfo["types"]['0']['type']['name'];
}


// <!-- pikachu
// Assignment: Write the code for this app so that on the button 
// click the h2 Name element changes to the pokemon searched, 
// the default image is replaced with a picture of that same pokemon, 
// and the type of pokemon is listed in the h3 Type element. If you have time, 
// add a checkbox next to the get pokemon button that says shiny. 
// If this shiny box is checked it should return the shiny picture of that pokemon -->