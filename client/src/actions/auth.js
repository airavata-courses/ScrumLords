import axios from 'axios';
import { REGISTER_SUCCESS, REGISTER_FAIL, USER_LOADED, AUTH_ERROR, LOGIN_SUCCESS, LOGIN_FAIL, LOGOUT } from './types';
import setAuthToken from '../utils/setAuthToken';

// LOAD USER

export const loadUser = () => async dispatch => {
    if (localStorage.token) {
        setAuthToken(localStorage.token);
    }

    try {
        const res = await axios.get('/api/auth');

        dispatch({
            type: USER_LOADED,
            payload: res.data
        });

    } catch (err) {
        dispatch({
            type: AUTH_ERROR
        });
    }
};

// Register user 
export const register = ({ name, email, password }) => async dispatch => {
    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    const body = JSON.stringify({ name, email, password });

    try {
        // for sending response 
        const res = await axios.post('/api/users', body, config);

        // if no error 
        dispatch({
            type: REGISTER_SUCCESS,
            // we get token back on success
            payload: res.data
        });

        dispatch(loadUser());

    } catch (err) {

        const errors = err.response.data.errors;
        console.log(errors)
        dispatch({
            type: REGISTER_FAIL
        });
    }
};

// Login user 

export const login = (email, password) => async dispatch => {
    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    const body = JSON.stringify({ email, password });

    try {
        // for sending response 
        const res = await axios.post('/api/auth', body, config);

        // if no error 
        dispatch({
            type: LOGIN_SUCCESS,
            // we get token back on success
            payload: res.data
        });

        dispatch(loadUser());

    } catch (err) {

        const errors = err.response.data.errors;
        console.log(errors)

        dispatch({
            type: LOGIN_FAIL
        });
    }
};

// LOGOUT / CLEAR PROFILE

export const logout = () => dispatch => {
    dispatch({
        type: LOGOUT
    });
};

