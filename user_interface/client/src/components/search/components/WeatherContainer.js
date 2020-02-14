import React, { useState } from 'react'
import WeatherInfo from './WeatherInfo';
import axios from 'axios'

export const WeatherContainer = () => {
    const API_KEY = '4c3f87318d7dda9dbf7b495c8c670333'
    const [searchQuery1, setSearchQuery1] = useState();
    const [searchQuery2, setSearchQuery2] = useState();
    const [weatherData, setWeatherData] = useState({
        temp: null,
        humidity: null,
        desc: null,
        city: null
    })

    const updateSearch1 = e => {
        setSearchQuery1(e.target.value);
    }

    const updateSearch2 = e => {
        setSearchQuery2(e.target.value);
    }


    /*
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
    */

    const getWeatherData = () => {

        /*
        if (!isValidZip || searchQuery === '') {
            setIsValidZip(false);
            return;
        }
        */

        fetch(`http://api.openweathermap.org/data/2.5/weather?q=${searchQuery1},${searchQuery2},us&units=imperial&appid=${API_KEY}`)
            .then(res => res.json())
            .then(async data => {
                const user = await axios.get('/api/auth');
                const user_id = user.data._id
                let city_id = data.id;
                setWeatherData({
                    temp: data.main.temp,
                    humidity: data.main.humidity,
                    desc: data.weather[0].main,
                    city: data.name
                })
                console.log(data)

                const config = {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                };
                const body = JSON.stringify({ user_id, city_id });
                // for sending response 
                const res = await axios.post('http://localhost:8000/session/create', body, config);
                console.log(res);
            })
    }

    /*
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
    */
    return (
        <section className="weather-container">
            <header className="weather-header">
                <h3>WEATHER.IO</h3>

                <div>
                    <input placeholder="City Name" className="search-input1" onChange={updateSearch1} />
                    <input placeholder="State ID" className="search-input2" onChange={updateSearch2} />
                    <button className="material-icons" onClick={getWeatherData}>search</button>
                </div>

            </header>
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