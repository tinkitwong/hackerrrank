function getMaxLessThanK(n, k) {
    let val = -9999;

    for (let a = 1; a <= n; a++) {
        for (let b = a+1; b <= n; b++) {
            let curr = a & b;
            curr > val && curr < k ? val = curr : val = val;
        }
    }
    return val
}
