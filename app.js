const express = require('express');
const conn = require('./database/db_perpustakaan');
const { customAlphabet } = require('nanoid'); //generate id for each book

const app = express();
const port = 3000;

app.use(express.json());

//Get All Book
app.get('/books', (req, res) => {
    const queryAllData = 'SELECT * FROM books';

    conn.query(queryAllData, (err, result) => {
        if (err){
            res.status(500).json({
                status: 'false',
                message: err.sqlMessage
            });
        } 
        res.status(200).json({
            status: 'success',
            message: 'Data berhasil ditampilkan',
            data: result
        });
    });
});

//Post or Insert Book
app.post('/books', (req, res) => {
    const id = customAlphabet('123abc', 5);
    const param = req.body;
    const name = param.name;
    const author = param.author;
    const year = param.year;
    const insert_at = new Date();
    const update_at = insert_at;

    const queryInsertData = 'INSERT INTO books (id, name, author, year, insert_at, update_at) VALUES (?, ?, ?, ?, ?, ?)';
    const queryInsert = [id(), name, author, year, insert_at, update_at]
    conn.query(queryInsertData, queryInsert, (err, result) => {
        if (err){
            console.log(err)
            res.status(500).json({
                status: 'error',
                message: err.sqlMessage,
                data: null
            });
        } 
        res.status(201).json({
            status: 'success',
            message: 'Data berhasil ditambahkan',
            data: id()
        });
    });

});


app.listen(port, () => {
    console.log(`App listening at http://localhost:${port}`);
});