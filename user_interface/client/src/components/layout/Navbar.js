import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { logout } from '../../actions/auth'

// To replace <a> tage wit Link

const Navbar = ({ auth: { isAuthenticated, loading }, logout }) => {

    const authLinks = (
        <Fragment>
            <h1>
                <Link to='/dashboard'><i className="fas fa-cloud fa-2x" style={{ paddingRight: 15 }}></i></Link>
            </h1>

            <ul className="navbar-right">
                <li><Link to='/sessions'>Jobs</Link></li>
                <li><a onClick={logout} href="/">Logout</a></li>
            </ul>
        </Fragment>

    )

    const guestLinks = (
        <Fragment>
            <h1>
                <Link to='/'><i className="fas fa-cloud fa-2x" style={{ paddingRight: 15 }}></i></Link>
            </h1>

            <ul className="navbar-right">
                <li><Link to="/login">Login</Link></li>
                <li><Link to="/register">Register</Link></li>
            </ul>
        </Fragment>

    )

    return (
        <div>
            <nav className="navbar bg-dark">
                {!loading && (<Fragment>{isAuthenticated ? authLinks : guestLinks}</Fragment>)}
            </nav>
        </div >
    )
}

Navbar.propTypes = {
    logout: PropTypes.func.isRequired,
    auth: PropTypes.object.isRequired
}

const mapStateToProps = state => ({
    auth: state.auth
});

export default connect(mapStateToProps, { logout })(Navbar);