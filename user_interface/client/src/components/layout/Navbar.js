import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { logout } from '../../actions/auth'
import {
    AppBar, Toolbar, Typography, Grid
} from '@material-ui/core'
import { makeStyles } from '@material-ui/core/styles';


const useStyles = makeStyles(theme => ({
    link: {
        marginTop: '30px',
        color: 'black',
        fontWeight: 600,
        fontFamily: 'Montserrat',
        textDecoration: 'none',
        textTransform: 'uppercase',
        textAlign: 'center',
    },

}));



const Navbar = ({ auth: { isAuthenticated, loading }, logout }) => {

    const classes = useStyles();

    const authLinks = (
        <Fragment>
            <div className="ui inverted segment">
                <div className="ui inverted secondary pointing large menu">
                    <Link to='/dashboard' className="item">Dashboard</Link>
                    <Link to='/sessions' className="item">Jobs</Link>

                    <div className="right menu">
                        <a className="item" onClick={logout} href="/">Logout</a>
                    </div>
                </div>
            </div>
        </Fragment>

    )

    const guestLinks = (
        <Fragment></Fragment>
    )

    return (
        <div>
            {!loading && (<Fragment>{isAuthenticated ? authLinks : guestLinks}</Fragment>)}
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