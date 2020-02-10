import React, { useState } from 'react'
import WeatherInfo from './WeatherInfo';
import axios from 'axios'

export const WeatherContainer = () => {
    const API_KEY = '4c3f87318d7dda9dbf7b495c8c670333'
    const [searchQuery, setSearchQuery] = useState();
    const [weatherData, setWeatherData] = useState({
        temp: null,
        humidity: null,
        desc: null,
        city: null
    })
    const [isValidZip, setIsValidZip] = useState(true);

    const updateSearch = e => {
        let zipCode = e.target.value;
        let isValid = validateZip(zipCode);
        setSearchQuery(e.target.value);

        if (isValid || zipCode === '' || isValid.length === 5) {
            setIsValidZip(true);
        } else {
            setIsValidZip(false);
        }

    }

    const validateZip = (zipCode) => {
        let regex = /[0-9]{5}/;
        return regex.test(zipCode)
    }

    const getWeatherData = () => {
        if (!isValidZip || searchQuery === '') {
            setIsValidZip(false);
            return;
        }

        fetch(`http://api.openweathermap.org/data/2.5/weather?zip=${searchQuery},us&appid=${API_KEY}`)
            .then(res => res.json())
            .then(async data => {
                const lat = data.coord.lat;
                const lon = data.coord.lon;
                const user = await axios.get('/api/auth');
                const user_id = user.data._id

                setWeatherData({
                    temp: data.main.temp,
                    humidity: data.main.humidity,
                    desc: data.weather[0].main,
                    city: data.name
                })

                const config = {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                };
                const body = JSON.stringify({ user_id, lat, lon });
                // for sending response 
                const res = axios.post('http://localhost:8000/session/create', body, config);
                console.log(body)
            })
    }

    return (
        <section className="weather-container">
            <header className="weather-header">
                <h3>WEATHER.IO</h3>
                <div>
                    <input placeholder="Enter Zip Code..." className="search-input" onChange={updateSearch} maxLength='5' />
                    <button className="material-icons" onClick={getWeatherData}>search</button>
                </div>
            </header>
            <p className="error">{isValidZip ? '' : 'Invalid Zip Code!'}</p>
            <section className="weather-info">
                {weatherData.temp === null ? (
                    <p>No Weather to Display<i className="material-icons">wb_sunny</i></p>
                ) : <WeatherInfo data={weatherData} />
                }
            </section>
        </section>
    )

}

export default WeatherContainer
