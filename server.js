// server.js
const express = require('express');
const { PythonShell } = require('python-shell');
const app = express();
const PORT = 3000;

app.get('/runPython', (req, res) => {
  // Specify the path to your Python script
  const pythonScriptPath = 'script.py';

  // Options for PythonShell
  const options = {
    p, // Optional, if python is not in PATH
  };

  PythonShell.run(pythonScriptPath, options, (err, results) => {
    if (err) {
      console.error(err);
      return res.status(500).send('Internal Server Error');
    }

    console.log('Python script executed successfully');
    console.log(results);
    res.send('Python script executed successfully');
  });
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
