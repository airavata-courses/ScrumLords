import React from 'react'

// To replace <a> tage wit Link
import { Link } from 'react-router-dom'
const Navbar = () => {
    return (
        <div>
            <nav className="navbar bg-dark">
                <h1>
                    <Link to='/'><i className="fas fa-cloud-moon fa-2x" style={{ paddingRight: 15 }}></i>w | io</Link>
                </h1>
                <ul>
                    <li><Link to='/login'>Login</Link></li>
                    <li><Link to='/register'>Register</Link></li>
                </ul>
            </nav>
        </div >
    )
}

export default Navbar
