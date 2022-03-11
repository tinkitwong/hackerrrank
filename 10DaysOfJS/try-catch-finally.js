function reverseString(s) {
    try {
        // reverse string s using split, reverse and join methods
        console.log(s.split("").reverse().join(""));
        
    } catch (error) {
        console.log(error.message);
        console.log(s);
    }
    
}

// s = Number(1234)
s = "1234"
reverseString(s)