import React, { Fragment, useState, useEffect } from 'react'

import axios from 'axios'
const SessionContainer = () => {
    const [sessionDetails, setSessionDetails] = useState([])

    useEffect(() => {
        async function getSessionData() {
            try {
                const user = await axios.get('/api/auth');
                const user_id = user.data._id;
                const res = await axios.get(`http://localhost:8000/user/${user_id}/sessions`)
                const res_data = res.data.data

                let temp = []
                res_data.forEach(sessionData => temp.push({ name: sessionData.name, latitude: sessionData.latitude, longitude: sessionData.longitude, geo_id: sessionData.geo_id }))
                setSessionDetails(temp)

            } catch (err) {
                console.log(err)
            }
        }
        getSessionData();
    }, []);


    return (
        <section className="session_container">
            <div className="headers">
                <h2>City</h2>
                <h2>Latitude</h2>
                <h2>Longitude</h2>
                <h2>Geo_ID</h2>
            </div>
            <section className="session-list">
                <ul>
                    {sessionDetails.map(session => (
                        <Fragment>
                            <a href='#'><li key={session.id}><span>{session.name}</span> <span>{session.latitude}</span> <span>{session.longitude}</span> <span>{session.geo_id}</span></li></a>
                        </Fragment>
                    ))}
                </ul>
            </section>
        </section >
    )
}

export default SessionContainer