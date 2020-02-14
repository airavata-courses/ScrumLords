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
                    , visible_id: sessionData.visible_id
                    , created: sessionData.created
                }))
                setSessionDetails(temp)

            } catch (err) {
                console.log(err)
            }
        }
        getSessionData();
    }, []);
    console.log(sessionDetails)


    const getHistory = async (session) => {
        const session_id = session.id
        const weather_history = await axios.get(`http://localhost:8000/session/${session_id}/get`)
        let json = JSON.stringify(weather_history.data.data)
        json = json.replace(/,"/g, ',\n"');
        let tab = window.open('about:blank', '_blank');
        tab.document.write(`<pre>${json}</pre>`); // where 'html' is a variable containing your HTML
        tab.document.close(); // to finish loading the page
    }

    const getForecast = async (session) => {
        const session_id = session.id
        const weather_forecast = await axios.get(`http://localhost:8000/session/${session_id}/forecast`)
        let json = JSON.stringify(weather_forecast.data.data)
        json = json.replace(/,"/g, ',\n"');
        let tab = window.open('about:blank', '_blank');
        tab.document.write(`<pre>${json}</pre>`); // where 'html' is a variable containing your HTML
        tab.document.close(); // to finish loading the page
    }


    const getSummary = async (session) => {
        const session_id = session.id
        const weather_summary = await axios.get(`http://localhost:8000/session/${session_id}/summary`)
        let json = JSON.stringify(weather_summary.data.data)
        json = json.replace(/\\n/g, '\n');
        let tab = window.open('about:blank', '_blank');
        tab.document.write(`<pre>${json}</pre>`); // where 'html' is a variable containing your HTML
        tab.document.close(); // to finish loading the page
    }


    return (
        <section className="session_container">
            <section className="session-list">
                <ul>
                    {sessionDetails.map(session => (
                        <Fragment key={session.id}>
                            <div>
                                <li key={session.id}>
                                    <span>CITY -> {session.name}</span>
                                    <span>STATE -> {session.state}</span>
                                    <span>SESSION_ID -> {session.visible_id}</span>
                                    <span>DATE_CREATED -> {session.created}</span>
                                    <button value={session.id} onClick={() => { getHistory(session) }}>Weather History</button>
                                    <button value={session.id} onClick={() => { getForecast(session) }}>Weather Forecast</button>
                                    <button value={session.id} onClick={() => { getSummary(session) }}>Forecast Summary</button>
                                </li>
                            </div>
                        </Fragment>
                    ))}
                </ul>
            </section>
        </section >
    )

}


export default SessionContainer