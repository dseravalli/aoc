const fs = require('fs');

const input: string[] = fs.readFileSync('input.txt').toString().split("\n");
const NUMBER_WORDS: readonly string[] = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
let sum = 0;

const isDigit = (char: string): boolean => ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'].indexOf(char) !== -1;

interface Matches {
    [key: number]: number;
}

for (const line of input) {
    const matches: Matches = {};
    let minIndex = line.length;
    let maxIndex = 0;

    for (const [wordIdx, word] of NUMBER_WORDS.entries()) {
        let foundIdx = line.indexOf(word);

        while (foundIdx !== -1) {
            matches[foundIdx] = wordIdx + 1;
            minIndex = Math.min(minIndex, foundIdx);
            maxIndex = Math.max(maxIndex, foundIdx);
            foundIdx = line.indexOf(word, foundIdx + word.length);
        }
    }

    for (const [idx, char] of line.split('').entries()) {
        if (isDigit(char)) {
            matches[idx] = +char;
            minIndex = Math.min(minIndex, idx);
            maxIndex = Math.max(maxIndex, idx);
        }
    }

    const number = ((matches[minIndex] * 10) + matches[maxIndex]) || 0;
    sum += number;
}

console.log(sum);
