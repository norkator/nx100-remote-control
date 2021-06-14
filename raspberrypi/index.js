'use strict';

const express = require('express');
const app = express();
const raspi = require('raspi');
const I2C = require('raspi-i2c').I2C;

const nanoAddress = 0x08;

raspi.init(() => {
    console.log('Raspi init');
    const i2c = new I2C();

    app.get('/sonar', (req, res, next) => {
        const buffer = i2c.readSync(nanoAddress, 0x1, 0x1);
        const data = buffer.toJSON().data;
        res.json({'cm': data[0]});
    });

    app.get('/position', (req, res, next) => {
        const buffer = i2c.readSync(nanoAddress, 0x2, 0x1);
        const data = buffer.toJSON().data;
        res.json({'position': data[0]});
    });

    app.listen(3000, () => {
        console.log('Server running on port 3000');
    });
});
