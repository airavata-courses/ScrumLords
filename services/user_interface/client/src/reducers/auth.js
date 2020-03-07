// REDUCER for Register Auth

import { REGISTER_SUCCESS, REGISTER_FAIL, USER_LOADED, AUTH_ERROR, LOGIN_SUCCESS, LOGIN_FAIL, LOGOUT } from "../actions/types";

// Define initial state

const initialState = {
    token: localStorage.getItem('token'),

    // Set TRUE if successful response
    isAuthenticated: null,

    // Check while loading user. Once we have response set this to FALSE user already loaded
    loading: true,

    // Get user info after hitting route user/auth
    user: null
}

export default function (state = initialState, action) {
    const { type, payload } = action;
    switch (type) {

        case USER_LOADED:
            return {
                ...state,
                isAuthenticated: true,
                loading: false,
                user: payload
            }


        //set token in local storage if success
        case REGISTER_SUCCESS:
        case LOGIN_SUCCESS:
            localStorage.setItem('token', payload.token);
            //state we want to return
            return {
                ...state,
                ...payload,
                isAuthenticated: true,
                loading: false
            };

        case REGISTER_FAIL:
        case LOGIN_FAIL:
        case AUTH_ERROR:
        case LOGOUT:
            localStorage.removeItem('token');
            return {
                ...state,
                token: null,
                isAuthenticated: false,
                loading: false
            };

        default:
            return state;
    }
}