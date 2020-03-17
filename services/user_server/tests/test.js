import chai from 'chai'
import chaiHttp from 'chai-http'
import app from '../server'
import { networkInterfaces } from 'os';

// Configure chai
chai.use(chaiHttp);
chai.should()

// Test route POST api/users
// Registration Route for user
// Returns a JWT Token ---- > res.json({ token })
// Error status 400

describe('User Registration', () => {
    // mock user input 
    const new_user = {
        "name": "John Doe",
        "email": "johndoe@gmail.com",
        "password": "123456"
    }

    // send request to app
    chai.request(app).post('/api/user')
        .send(new_user)
        .then((res) => {
            console.log(res.body);

            // assertions
            expect(res).to.have.status(200);
            expect(res.body)
        })
})




// Test route POST api/auth
// Login Route for user
// Returns a JWT Token ---- > res.json({ token })
// Error status 400

describe('User Login', () => {
    it('should return 200 and JWT token for valid credentials', (done) => {

    })
})