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
                res_data.forEach(sessionData => temp.push({
                    id: sessionData.id
                    , name: sessionData.name
                    , state: sessionData.admin_code
                    , latitude: sessionData.latitude
                    , longitude: sessionData.longitude
                    , geo_id: sessionData.geo_id
                    , created: sessionData.created
                }))
                setSessionDetails(temp)

            } catch (err) {
                console.log(err)
            }
        }
        getSessionData();
    }, []);


    const getForecast = async (session) => {
        const session_id = session.id
        const session_res = await axios.get(`http://localhost:8000/session/${session_id}/get`)
        console.log(session_res)
        const forecast_res = await axios.get(`http://localhost:8000/session/${session_id}/forecast`)
        console.log(forecast_res)

    }


    return (
        <section className="session_container">
            <section className="session-list">
                <ul>
                    {sessionDetails.map(session => (
                        <Fragment key={session.id}>
                            <a value={session.id} onClick={() => { getForecast(session) }}> <li key={session.id}>
                                <span>City -> {session.name}</span>
                                <span>State -> {session.state}</span>
                                <span>Latitude -> {session.latitude}</span>
                                <span>Longitude -> {session.longitude}</span>
                                <span>Geo_ID -> {session.geo_id}</span>
                                <span>Date Created -> {session.created}</span>
                            </li></a>
                        </Fragment>
                    ))}
                </ul>
            </section>
        </section >
    )

}


export default SessionContainer