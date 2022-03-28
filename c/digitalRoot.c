// Link to challenge: https://www.codewars.com/kata/541c8630095125aba6000c00
int digital_root(int n) {
    while (n > 9) {                 // we only want one digit
        int tmpN = 0;
        while (n > 0) {             // one digit in n at a time
            tmpN += n % 10;         // add Least Significant Digit
            n /= 10;                // int div by 10 to drop Least Significant Digit
        }
        n = tmpN;                   // new iteration of n
    }
    return n;
}