import React, { Fragment, useState } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types'
import { login } from '../../actions/auth';
import { Redirect } from 'react-router-dom';


const Login = (props) => {

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
            <section className="container dark-overlay">
                <h1 className="form-title-login">Login</h1>
                <form className="form" onSubmit={e => onSubmit(e)}>
                    <div className="form-group">
                        <input type="email" placeholder="enter email" name="email" value={email} onChange={e => onChange(e)} required />
                    </div>
                    <div className="form-group">
                        <input type="password" placeholder="password" name="password" value={password} onChange={e => onChange(e)} required />
                    </div>
                    <input type="submit" className="btn btn-primary" value="login" />
                </form>
            </section>
        </Fragment>
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