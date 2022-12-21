const express = require('express');
const mysql = require("mysql2");

const app = express();
app.use(express.json());

const pool = mysql.createPool({
    connectionLimit: 5,
    host: "localhost",
    user: "root",
    database: "reg_informator",
    password: "123456"
  });

app.get('/', (req, res) => {
    pool.query(`SELECT * FROM info`, function(err, data) {
        res.send(data);
    });
});

app.post('/', (req, res) => {
    console.log(req.body);
    
    pool.query(`INSERT INTO reg_informator.info (info) VALUES ('${JSON.stringify(req.body)}')`, function(err, data) {
        console.log('success');
    });
    res.send('ok');
});

app.listen(3333, () => {
    console.log('Application listening on port 3333!');
});