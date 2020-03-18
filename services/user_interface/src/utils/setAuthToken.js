// function to take in token -> if token add to header -> if NOT deleter from header

import axios from 'axios';

// Send token with every request

const setAuthToken = token => {
    if (token) {
        axios.defaults.headers.common['x-auth-token'] = token;
    } else {
        delete axios.defaults.headers.common['x-auth-token'];
    }
};
export default setAuthToken;