""" -------Permutation in a String (hard)-------
Problem Challenge 1
>>> Given a string and a pattern, find out if the string contains any permutation of the pattern.
<<<Permutation>>> is defined as the re-arranging of the characters of the string.
For example, “abc” has the following six permutations:
1. abc
2. acb
3. bac
4. bca
5. cab
6. cba 
>>> If a string has ‘n’ distinct characters it will have n! permutations.

Example 1:
Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

Example 2:
Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

Example 3:
Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.

Example 4:
Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern. """
# NOTE: Time complexity => O(N + M) => N and M are the number of characters in the input string and pattern
# NOTE: Space complexity => O(M) => as the number of distinct characters of the pattern that gets added in the hashmap 
from math import factorial

def find_permutation(string, pattern):
    # print(factorial(len(pattern))) # number of permutations in 'pattern' is found by the factorial of its length
    window_start = 0
    matched = 0
    char_frequency = {}

    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1
    
    for window_end in range(len(string)):
        right_char = string[window_end]
        # try matching all characters from 'char_frequency' in all characters in current window
        if right_char in char_frequency:
            # decrease the frequency count of the character that matched
            char_frequency[right_char] -= 1   
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            return True

        # start sliding window by one character once the size of window matches the number of characters in pattern
        if window_end >= len(pattern) - 1:
            left_char = string[window_start]
            window_start += 1
            # Was it inside the sliding window? - check if character that is going to leave the window is in 'char_frequency'
            if left_char in char_frequency:
                # if the value of a character in 'char_frequency' is 0, and matched was increase, so we need to decrease matched again.
                if char_frequency[left_char] == 0:
                    matched -= 1
                # account for the character that is about to leave window back in 'char_frequency'
                char_frequency[left_char] += 1
    return False


if __name__ == "__main__":
    string_test = "oidbcaf"
    pattern = "abc"
    print("Contains permutation: ", find_permutation(string_test, pattern)) # expected output = true
    string_test = "odicf"
    pattern = "dc"
    print("Contains permutation: ", find_permutation(string_test, pattern)) # expected output = false
    string_test = "bcdxabcdy"
    pattern = 'bcdyabcdx'
    print("Contains permutation: ", find_permutation(string_test, pattern)) # expected output = true
    string_test = "aaacb"
    pattern = "abc"
    print("Contains permutation: ", find_permutation(string_test, pattern)) # expected output = true