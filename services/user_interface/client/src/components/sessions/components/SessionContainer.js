import React, { useState, useEffect } from 'react'

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
                console.log(res_data)

                let temp = []
                res_data.forEach(sessionData => temp.push({
                    id: sessionData.id
                    , name: sessionData.name
                    , state: sessionData.admin_code
                    , visible_id: sessionData.visible_id
                    , created: sessionData.created
                    , status: sessionData.status
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
        <div className="ui container divided items">
            {sessionDetails.map(session => (
                <div className="item content" key={session.id}>

                    <div className="content session-card">
                        <a className="header">{session.name}, {session.state}</a>
                        <div className="meta">JOB ID ({session.visible_id})</div>
                        <div className="description">
                            <img
                                src="https://react.semantic-ui.com/images/wireframe/short-paragraph.png"
                                className="ui image rounded" />
                        </div>
                        <div className="extra">

                            <div className="ui black label pointing">Created : {session.created.slice(0, 10)}</div>
                            <div className="ui black label pointing">Status : {session.status}</div>

                            <div className="ui primary right floated small buttons">
                                <button className="ui button" value={session.id} onClick={() => { getHistory(session) }}>History</button>
                                <div className="or"></div>
                                <button className="ui button" value={session.id} onClick={() => { getForecast(session) }}>Forecast</button>
                                <div className="or"></div>
                                <button className="ui button" value={session.id} onClick={() => { getSummary(session) }}>Summary</button>
                            </div>
                        </div>
                    </div>
                </div>
            )
            )}
        </div >
    )
}


export default SessionContainer