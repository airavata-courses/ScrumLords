import React, { Fragment, useEffect } from 'react';
import Landing from './components/layout/Landing';
import Navbar from './components/layout/Navbar';
import Login from './components/auth/Login';
import Register from './components/auth/Register';
import Search from './components/search/Search';
import Session from './components/sessions/Session';
import PrivateRoute from './components/routing/PrivateRoute';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
// Redux
import { Provider } from 'react-redux';
import store from './store';
import setAuthToken from './utils/setAuthToken'
import { loadUser } from './actions/auth';
import './css/weather.css'

if (localStorage.token) {
  setAuthToken(localStorage.token);
}

// Allow Cross-Origin requests
let cors_api_host = 'cors-anywhere.herokuapp.com';
let cors_api_url = 'https://' + cors_api_host + '/';
let slice = [].slice;
let origin = window.location.protocol + '//' + window.location.host;
let open = XMLHttpRequest.prototype.open;
XMLHttpRequest.prototype.open = function () {
  let args = slice.call(arguments);
  let targetOrigin = /^https?:\/\/([^\/]+)/i.exec(args[1]);
  if (targetOrigin && targetOrigin[0].toLowerCase() !== origin &&
    targetOrigin[1] !== cors_api_host) {
    args[1] = cors_api_url + args[1];
  }
  return open.apply(this, args);
};

const App = () => {

  useEffect(() => {
    store.dispatch(loadUser());
  }, []);

  return (
    <Provider store={store}>
      <Router>
        <Fragment>
          <Navbar />
          <Switch>
            <Route exact path='/' component={Landing} />
            <Route exact path="/register" component={Register} />
            <Route exact path="/login" component={Login} />
            <PrivateRoute exact path="/dashboard" component={Search} />
            <PrivateRoute exact path="/sessions" component={Session} />
          </Switch>

        </Fragment>
      </Router>
    </Provider >
  );
};

export default App;
