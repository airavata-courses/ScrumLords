const express = require('express');
const router = express.Router();
const auth = require('../../middleware/auth');
const User = require('../../models/User');
const bcrypt = require('bcryptjs')

// GET api/auth
// Request will be sent with token in the header
// This will verify token with middleware and return user on success

router.get('/', auth, async (req, res) => {
    try {
        const user = User.findById(req.user.id).select('-password');
        res.json(user);
    } catch (err) {
        console.error(err.message);
        res.status(500).send('Server Error!');
    }
})

// POST api/auth
// Check for user credentials
// Generate token for user
router.post(
    '/',
    [check('email', 'Include valid email').isEmail(),
    check('password', 'Password should be 6 or more chars').isLength({ min: 6 })
    ],
    async (req, res) => {
        const errors = validationResult(req);
        if (!errors.isEmpty()) {
            return res.status(400).json({ errors: errors.array() });
        }

        const { email, password } = req.body;

        try {
            // Check if user has registered
            let user = await User.findOne({ email });
            if (!user) {
                return res.status(400).json({ errors: [{ msg: 'Invalid Credentials!' }] })
            }

            // Compare user password with DB password
            const isMatch = await bcrypt.compare(password, user.password);

            if (!isMatch) {
                return res.status(400).json({ errors: [{ msg: 'Invalid Credentials!' }] })
            }
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