const express = require('express');
const fs = require('fs');
const csv = require('csv-parser');

const app = express();
const PORT = 3000;

app.use(express.json());

// Endpoint to fetch cat data
app.get('/cats', (req, res) => {
    const results = [];
    fs.createReadStream('cats.csv')
        .pipe(csv())
        .on('data', (data) => results.push(data))
        .on('end', () => {
            res.json(results);
        })
        .on('error', (error) => {
            res.status(500).json({ error: 'Failed to read CSV file' });
        });
});

// Serve frontend files
app.use(express.static('public'));

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
