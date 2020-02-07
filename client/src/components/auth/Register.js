import React, { Fragment, useState } from 'react'

const Register = () => {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        password: '',
        password2: ''
    });

    const { name, email, password, password2 } = formData;
    return (
        <Fragment>
            <section className="container dark-overlay">
                <h1 className="form-title-register">Register</h1>
                <form className="form" action="dashboard.html">
                    <div className="form-group">
                        <input type="text" placeholder="enter name" name="name" value={name} required />
                    </div>
                    <div className="form-group">
                        <input type="email" placeholder="enter email" name="email" required />
                    </div>
                    <div className="form-group">
                        <input type="password" placeholder="password" name="password" required />
                    </div>
                    <div className="form-group">
                        <input type="password" placeholder="confirm password" name="email" required />
                    </div>
                    <input type="submit" className="btn btn-primary" value="register" />
                </form>
            </section>
        </Fragment>
    )
}

export default Register