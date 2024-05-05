# Using readline in nodejs

## Objective
This file explains how to input a variable in Javascript. References that were used are from the official Node.js documentation (1).

## Procedure
1. Declare the variable "readline = require('node:readline');". The code "require('node:readline');" imports the functionality from node's codebase to properly use readline.
```
const readline = require('node:readline');
```
2. Declare an input and output in order to use readline. 
```
const readline = require('node:readline');

const { stdin: input, stdout: output } = require('node:process');

const first_read = readline.createInterface({ input, output });
```
3. Next, now write the name of the declared variable followed by ".question" and a parenthesis that states a question and the variable that takes the input: 
```
const readline = require('node:readline');

const { stdin: input, stdout: output } = require('node:process');

const first_read = readline.createInterface({ input, output });

first_read.question('Sample question text asking for input: ', (answer) => {
    console.log(`Sample text data: ${answer}`)

    first_read.close();
});
```
To forcefully exit out of the terminal without pressing control + C, the line variable_name.close() automatically leaves the terminal.

## Documentation
https://nodejs.org/api/readline.html (1)
