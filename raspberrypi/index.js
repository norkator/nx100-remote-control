'use strict';

const express = require('express');
const app = express();
const raspi = require('raspi');
const I2C = require('raspi-i2c').I2C;

raspi.init(() => {
    console.log('Raspi init');
    const i2c = new I2C();

    app.get('/sonar', (req, res, next) => {

        // i2c.readByteSync(0x18)
        // Todo... in progress
        res.json({'cm': 20});
    });

    app.listen(3000, () => {
        console.log('Server running on port 3000');
    });
});
