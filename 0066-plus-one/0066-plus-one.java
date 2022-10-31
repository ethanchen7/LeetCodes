class Solution {
    public int[] plusOne(int[] digits) {
        
        int n = digits.length;
        
        for (int i = n - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i] += 1;
                return digits;
            } else {
                digits[i] = 0;
            }
        }
        // case where input is all 9s
        digits = new int[n + 1]; // create a new array of ints (all 0s)
        digits[0] = 1; // set zeroth index to 1
        return digits;
    }
}