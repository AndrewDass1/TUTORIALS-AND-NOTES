const http = require('node:http');
// Add line of code below to read module:
const import_module = require('./export_module');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  // Include res.write() downbelow
  res.write(import_module.insert_name_here())
  res.end();
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
