function mostrarClima(){
    let url='http://api.weatherapi.com/v1/forecast.json?key=30f578f676b94ed4bc165542242106&q=-33.45,-70.67&days=7&aqi=no&alerts=no&lang=es';
    fetch(url)
    .then(response => response.json())
    .then(data => climaData(data))
    .catch(error => console.log(error));
}

const climaData = (data) => {
    console.log(data);
    let body = "";

    if (data && data.forecast && data.forecast.forecastday) {
        const today = new Date();
        const forecastDays = data.forecast.forecastday.filter(day => new Date(day.date) >= today);

        forecastDays.forEach((day) => {
            const date = new Date(day.date);
            
            // Ajustar la fecha a GMT-4
            const adjustedDate = new Date(date.setHours(date.getHours() - 4));

            const formattedDate = adjustedDate.toLocaleDateString('es-ES', {
                day: '2-digit',
                month: 'long',
                year: 'numeric'
            });

            body += `<tr>
                <td>${formattedDate}</td>
                <td>${day.day.condition.text}</td>
                <td>${day.day.mintemp_c} °C</td>
                <td>${day.day.maxtemp_c} °C</td>
            </tr>`;
        });

        document.getElementById('weather-forecast').innerHTML = body;
    } else {
        console.log("No se encontraron datos climáticos.");
    }
};