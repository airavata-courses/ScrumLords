import React, { Fragment, useState } from 'react';
// Work with redux
import { connect } from 'react-redux';
import { register } from '../../actions/auth';
import { Redirect } from 'react-router-dom';
import PropTypes from 'prop-types'

const Register = (props) => {

    const [formData, setFormData] = useState({
        name: '',
        email: '',
        password: '',
        password_check: ''
    });

    const { name, email, password, password2 } = formData;

    const onChange = e =>
        setFormData({ ...formData, [e.target.name]: e.target.value });

    const onSubmit = async e => {
        e.preventDefault();
        if (password !== password2) {
            alert("Passwords don't match!");
        } else {
            props.register({ name, email, password });
        }
    };

    if (props.isAuthenticated) {
        return <Redirect to='/dashboard' />
    }

    return (
        <Fragment>
            <section className="container dark-overlay">
                <h1 className="form-title-register">Register</h1>
                <form className="form" onSubmit={e => onSubmit(e)}>
                    <div className="form-group">
                        <input type="text" placeholder="enter name" name="name" value={name} onChange={e => onChange(e)} required />
                    </div>
                    <div className="form-group">
                        <input type="email" placeholder="enter email" name="email" value={email} onChange={e => onChange(e)} required />
                    </div>
                    <div className="form-group">
                        <input type="password" placeholder="password" name="password" value={password} onChange={e => onChange(e)} required />
                    </div>
                    <div className="form-group">
                        <input type="password" placeholder="confirm password" name="password2" value={password2} onChange={e => onChange(e)} required />
                    </div>
                    <input type="submit" className="btn btn-primary" value="register" />
                </form>
            </section>
        </Fragment>
    )
}

Register.propTypes = {
    register: PropTypes.func.isRequired,
    isAuthenticated: PropTypes.bool
}

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
});

export default connect(mapStateToProps, { register })(Register);
