console.log("NEW SCRIPT VERSION")
const searchButton = document.querySelector('.search__button');
const cityInput = document.querySelector('[name="city"]');
const citiesList = document.querySelector('#saved-cities ul');

console.log(cityInput);
console.log(searchButton);
console.log(citiesList);

searchButton.addEventListener("click", function(event) {
    event.preventDefault();

    console.log("1. Button clicked");

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
            console.log("2. Response received:", response.status);
            return response.json();
        })
        .then(data => {
            console.log("3. Data received:", data);

            const newCity = document.createElement("li");
            const weatherForm = document.createElement('form');
            const weatherButton = document.createElement('button');
            const weatherResult = document.createElement('div')
            const cityHiddenInput = document.createElement('input');
            const deleteForm = document.createElement('form');
            const deleteButton = document.createElement('button');
            const deleteHiddenInput = document.createElement('input');
            weatherForm.className = 'weather-form'
            weatherButton.className = 'weather-button'
            weatherButton.setAttribute('type', 'button')
            weatherButton.textContent = 'Get Weather'
            weatherResult.className = 'weather-result'
            deleteForm.className = 'delete-form'
            deleteButton.className = 'delete-button'
            deleteButton.setAttribute('type', 'button')
            deleteButton.textContent = 'Delete'
            cityHiddenInput.type = 'hidden'
            cityHiddenInput.name = 'city'
            cityHiddenInput.value = data.name
            deleteHiddenInput.type = 'hidden'
            deleteHiddenInput.name = 'city'
            deleteHiddenInput.value = data.name
            newCity.className = 'city-item'
            newCity.textContent = data.name;

            weatherForm.append(cityHiddenInput);
            weatherForm.append(weatherButton);
            weatherButton.addEventListener('click', function() {
                fetch(`/api/weather/${encodeURIComponent(data.name)}/`)
                .then(response => {
                    if (!response.ok){
                        throw new Error("Failed to get weather");
                    }
                    return response.json()
                })
                .then(weather => {
                    weatherResult.replaceChildren();

                    const location = document.createElement('p')
                    location.textContent = `${weather.location_name}, ${weather.country}`;

                    const temperature =  document.createElement('p')
                    temperature.textContent = `Temparature: ${weather.temperature}°C`;

                    const description = document.createElement('p')
                    description.textContent = `Weather: ${weather.weather_description}`;

                    weatherResult.append(location, temperature, description)
                })
                .catch(error => {
                    console.error("Weather request failed", error)
                })
});
            newCity.append(weatherForm);
            newCity.append(weatherResult);
            deleteForm.append(deleteHiddenInput);
            deleteForm.append(deleteButton);
            deleteButton.addEventListener('click', function() {
                fetch(`/api/cities/${data.id}/`, {
                    method: "DELETE",
                    headers: {
                    "Content-Type": "application/json"
                    }
                })
                .then(
                    response => {
                    console.log("2. Response recieved:", response.status);

                    if(!response.ok) {
                        throw new Error("Failed to delete the city")
                    }

                    return response.json();
                })
                .then(data => {
                    newCity.remove();
                })
});
            newCity.append(deleteForm);
            citiesList.append(newCity);

            console.log("4. City appended:", citiesList.innerHTML);
            console.log(weatherForm)
        })
        .catch(error => {
            console.error("Request failed:", error);
        });
});

fetch("/api/cities/")
    .then(response => {
        console.log(response.status);
        return response.json()
    }
     )
    .then(data => console.log(data))

