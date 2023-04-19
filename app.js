const express = require('express');
const conn = require('./database/db_perpustakaan');
const nanoid = require('nanoid'); //generate id for each book

const app = express();
const port = 3000;

//Get All Book
app.get('/books', (req, res) => {
    const queryAllData = 'SELECT * FROM books';

    conn.query(queryAllData, (err, result) => {
        if (err){
            res.status(500).json({
                status: 'error',
                message: err.sqlmessage
            });
        } 
        res.status(200).json({
            status: 'success',
            message: 'Data berhasil ditampilkan',
            data: result
        });
    });
});


app.listen(port, () => {
    console.log(`App listening at http://localhost:${port}`);
});