import React, { Fragment } from 'react'

const WeatherInfo = (props) => {
    const { temp, humidity, desc, city } = props.data;
    return (
        <Fragment>
            <h3>{desc}</h3>
            <div className="header-description">

                <p>{city}</p>
            </div>
            <div className="header-description">

                <p>{temp}<sup>o</sup>F</p>
            </div>
        </Fragment>
    )
}

export default WeatherInfo
