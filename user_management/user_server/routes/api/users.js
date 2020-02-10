const express = require('express');
const router = express.Router();
const { check, validationResult } = require('express-validator');
const bcrypt = require('bcryptjs');
const User = require('../../models/User');
const jwt = require('jsonwebtoken');
const config = require('config');

// POST api/users
// Register New User
router.post(
    '/',
    [check('name', 'Name is required').not().isEmpty(),
    check('email', 'Include valid email').isEmail(),
    check('password', 'Password should be 6 or more chars').isLength({ min: 6 })
    ],
    async (req, res) => {
        const errors = validationResult(req);
        if (!errors.isEmpty()) {
            return res.status(400).json({ errors: errors.array() });
        }

        const { name, email, password } = req.body;

        try {
            // Check iff user is already registered
            let user = await User.findOne({ email });
            if (user) {
                return res.status(400).json({ errors: [{ msg: 'User already exists!' }] })
            }

            user = new User({
                name,
                email,
                password
            });

            // Encrypt password
            const salt = await bcrypt.genSalt(10);
            user.password = await bcrypt.hash(password, salt);
            await user.save();

            // Return JWT
            const payload = { user: { id: user.id } };
            jwt.sign(payload,
                config.get('jwtSecret'),
                { expiresIn: 360000 },
                (err, token) => {
                    if (err) throw err;
                    res.json({ token })
                });
        } catch (err) {
            res.status(500).send('Server Error')
        }
    })

// GET api/users
// Public test route
router.get('/', (req, res) => {
    res.send('User Route');
})

module.exports = router;