import React from 'react';
import { Grid, CssBaseline, Paper } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import Login from '../auth/Login';
import Navbar from '../layout/Navbar';
import Img1 from '../../css/img/undraw1.svg';
import Img2 from '../../css/img/bg1.png'

const useStyles = makeStyles(theme => ({
    root: {
        backgroundImage: `linear-gradient(rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.1)), url(${Img2})`,
        height: '100vh',
        display: 'flex',
        justifyContent: 'center',
        alignContent: 'center',
    },
    image: {
        backgroundImage: `url(${Img1})`,
        backgroundRepeat: 'no-repeat',
        backgroundColor:
            theme.palette.type === 'dark' ? theme.palette.grey[900] : theme.palette.grey[50],
        backgroundPosition: 'center',
        backgroundSize: '85%',
    },
    form: {
        background: '#FEFFFE',
    },
}));

export default function Landing() {
    const classes = useStyles();
    return (
        <Grid container component="main" className={classes.root}  >
            <CssBaseline />
            <Grid item xs={false} sm={false} md={6} className={classes.image} />
            <Grid item xs={12} sm={12} md={4} className={classes.form} component={Paper}>
                <Login />
            </Grid>
        </Grid >
    );
}