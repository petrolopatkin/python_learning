const searchButton = document.querySelector('.search__button');
const cityInput = document.querySelector('[name="city"]');

console.log(cityInput);
console.log(searchButton);

searchButton.addEventListener("click", function(event){
    event.preventDefault();

    fetch("/api/cities/", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        name: cityInput.value
    })
})
    .then(response => {
        console.log(response.status)
        console.log(response.ok)
        return response.json()
    })
    .then(data => console.log(data))
    
    console.log(cityInput.value)
});

fetch("/api/cities/")
    .then(response => {
        console.log(response.status);
        return response.json()
    }
     )
    .then(data => console.log(data))

