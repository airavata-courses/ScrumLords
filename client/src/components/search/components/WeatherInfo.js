import React, { Fragment } from 'react'

const WeatherInfo = (props) => {
    const { temp, humidity, desc, city } = props.data;
    return (
        <Fragment>
            <h3>{desc}</h3>
            <div className="header-description">
                <h4>City</h4>
                <p>{city}</p>
            </div>
            <div className="header-description">
                <h4>Temperature</h4>
                <p>{temp}</p>
            </div>
            <div className="header-description">
                <h4>Humidity</h4>
                <p>{humidity}</p>
            </div>
        </Fragment>
    )
}

export default WeatherInfo
