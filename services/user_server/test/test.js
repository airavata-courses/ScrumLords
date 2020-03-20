const request = require('supertest');
const expect = require('chai').expect;
const app = require('../server');
const User = require('../models/User');

// Test route POST api/auth
// Login Route for user
// Returns a JWT Token ---- > res.json({ token })
// Error status 400

/*
describe('Register API', function () {
    it('Valid Register!', function (done) {
        request(app)
            .post('/api/users')
            .set('Accept', 'application/json')
            .set('Content-Type', 'application/json')
            .send({ name: 'TEST', email: 'TEST@gmail.com', password: '123456' })
            .expect(200)
            .expect('Content-Type', /json/)
            .expect(function (response) {
                expect(response.body).not.to.be.empty;
                expect(response.body).to.be.an('object');
            })
            .end(done);
    });
});
*/

// Test route POST api/users
// Registration Route for user
// Returns a JWT Token ---- > res.json({ token })
// Error status 400

describe('User Authentication', function () {
    it('Valid Credentials!', function (done) {
        request(app)
            .post('/api/auth')
            .set('Accept', 'application/json')
            .set('Content-Type', 'application/json')
            .send({ email: 'TEST@gmail.com', password: '123456' })
            .expect(200)
            .expect('Content-Type', /json/)
            .expect(function (response) {
                expect(response.body).not.to.be.empty;
                expect(response.body).to.be.an('object');
            })
            .end(done);
    });
});