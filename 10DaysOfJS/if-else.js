'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function getGrade(score) {
    let grade;
    // Write your code here
    if (inBetween(score, 25, 30)) {
        grade="A";
    }
    else if (inBetween(score, 20, 25)) {
        grade="B";
    }
    else if (inBetween(score, 15, 20)) {
        grade="C";
    }
    else if (inBetween(score, 10, 15)) {
        grade="D";
    }
    else if (inBetween(score, 5, 10)) {
        grade="E";
    }
    else {
        grade="F";
    } 
    return grade;
}

function inBetween(x, min, max) {
    return x > min && x <= max;
}

