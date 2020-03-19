import React, { Fragment, useState } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types'
import { login } from '../../actions/auth';
import { Redirect } from 'react-router-dom';

import {
    Avatar, Button, TextField, Link, Box, Grid, Typography
} from '@material-ui/core'
import { makeStyles } from '@material-ui/core/styles';

function Copyright() {
    return (
        <Typography variant="body2" color="textSecondary" align="center">
            {'Copyright © '}
            <Link color="inherit" href="https://github.com/airavata-courses/ScrumLords">
                ScrumLords
      </Link>{' '}
            {new Date().getFullYear()}
            {'.'}
        </Typography>
    );
}

const useStyles = makeStyles(theme => ({
    root: {
        height: '100vh',
    },
    paper: {
        margin: theme.spacing(8, 6),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    avatar: {
        margin: theme.spacing(2),
        backgroundColor: '#00BFA6',
    },
    form: {
        width: '100%', // Fix IE 11 issue.
        marginTop: theme.spacing(7),
    },
    submit: {
        background: '#5e5e5e',
        border: 0,
        borderRadius: 20,
        boxShadow: 'rgba(255, 105, 135, .3)',
        color: 'white',
        height: 48,
        padding: '0 30px',
        margin: theme.spacing(3, 0, 3),
    },

    link: {
        fontFamily: 'Montserrat',
        fontWeight: 600,
        color: '#00BFA6'
    },

    header: {
        fontFamily: 'Montserrat',
        fontWeight: 600,
        textTransform: 'uppercase',
    },
}));

const Login = (props) => {

    const classes = useStyles();
    const [formData, setFormData] = useState({
        email: '',
        password: ''
    });

    const { email, password } = formData;

    const onChange = e =>
        setFormData({ ...formData, [e.target.name]: e.target.value });

    const onSubmit = async e => {
        e.preventDefault();

        props.login(email, password);
    };

    // Redirect if logged in 

    if (props.isAuthenticated) {
        return <Redirect to='/dashboard' />
    }


    return (
        <Fragment>
            <div className={classes.paper}>
                <Avatar className={classes.avatar}>
                </Avatar>
                <Typography component="h1" variant="h6" className={classes.header} color="textSecondary">
                    ScrumLords - Weather
                </Typography>
                <form className={classes.form} onSubmit={e => onSubmit(e)}>
                    <TextField
                        variant="outlined"
                        margin="normal"
                        required
                        fullWidth
                        id="email"
                        label="Email Address"
                        name="email"
                        autoComplete="email"
                        autoFocus
                        type="email"
                        value={email}
                        onChange={e => onChange(e)}
                    />
                    <TextField
                        variant="outlined"
                        margin="normal"
                        required
                        fullWidth
                        name="password"
                        label="Password"
                        type="password"
                        id="password"
                        value={password}
                        onChange={e => onChange(e)}
                        autoComplete="current-password"
                    />

                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        color="primary"
                        className={classes.submit}
                        value="login">
                        Sign In
                        </Button>
                    <Grid container>
                        <Grid item xs>
                            <Link href="#" variant="body2" className={classes.link}>
                                Forgot password?
                            </Link>
                        </Grid>
                        <Grid item>
                            <Link href="/register" variant="body2" className={classes.link}>
                                {"New Here? Register"}
                            </Link>
                        </Grid>
                    </Grid>
                    <Box mt={5}>
                        <Copyright />
                    </Box>
                </form>
            </div>
        </Fragment >
    )
}

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
});

Login.propTypes = {
    login: PropTypes.func.isRequired,
    isAuthenticated: PropTypes.bool
}

export default connect(mapStateToProps, { login })(Login); 