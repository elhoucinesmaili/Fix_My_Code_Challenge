#!/usr/bin/node
/*
    Print a square using the character #
    
    The size of the square should be provided 
    as the first argument to the program.
*/

const args = process.argv;

if (args.length < 3) {
    console.error("Missing argument");
    console.error("Usage: ./print_square.js <size>");
    console.error("Example: ./print_square.js 5");
    process.exit(1);
}

const size = Number(args[2]);

if (isNaN(size) || size <= 0) {
    console.error("The size must be a positive number");
    process.exit(1);
}

const squareRow = "#".repeat(size);

for (let i = 0; i < size; i++) {
    console.log(squareRow);
}
