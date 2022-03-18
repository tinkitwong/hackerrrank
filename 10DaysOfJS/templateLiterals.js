/*
 * Determine the original side lengths and return an array:
 * - The first element is the length of the shorter side
 * - The second element is the length of the longer side
 * 
 * Parameter(s):
 * literals: The tagged template literal's array of strings.
 * expressions: The tagged template literal's array of expression values (i.e., [area, perimeter]).
 */
function sides(literals, ...expressions) { 
    let area = expressions[0];
    let perimeter = expressions[1];
    let arr = []
    
    let s1 = (perimeter + Math.sqrt( Math.pow(perimeter,2) - Math.imul(area,16)) ) / 4
    let s2 = (perimeter - Math.sqrt( Math.pow(perimeter,2) - Math.imul(area,16)) ) / 4
    arr.push(s1)
    arr.push(s2)
    
    return arr.sort(function(a,b) {return a-b})
}



let s1 = +("10");
let s2 = +("14");

[s1, s2] = [s1, s2].sort();

const [x, y] = sides`The area is: ${s1 * s2}.\nThe perimeter is: ${2 * (s1 + s2)}.`;

console.log((s1 === x) ? s1 : -1);
console.log((s2 === y) ? s2 : -1);
