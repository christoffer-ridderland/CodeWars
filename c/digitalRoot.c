// Link to challenge: https://www.codewars.com/kata/541c8630095125aba6000c00/train/c
int digital_root(int n) {
    while (n > 9) {
        int tmpN = 0;
        while (n > 0) {
            tmpN += n % 10;
            n /= 10;
        }
        n = tmpN;
    }
    return n;
}