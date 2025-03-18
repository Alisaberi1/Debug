# Debug
Mehdi, who is tired of coding, is no longer bored with numbers that have more than one digit. For this reason, every multi-digit number it encounters, it turns it into a single-digit number in its own way. In this way, it replaces the desired number with the number obtained from the sum of its digits and reaches a new number. It then does the same with the new number and continues to do so until it reaches a single-digit number. After a while, Mehdi realized that not only was he not more comfortable doing this, but he was more involved in numbers. As a result, he has asked you to help him in making the numbers single-digit.

Input
In the only input line of a number n which indicates the number that you need to make in single digits.

1≤n≤10^18

 

Output
In the only output line, the single-digit number resulting from the conversion must be 
n
n It should be printed in a single digit number according to the Mehdi method.

Example
Sample Entry 1
14

Sample Output 1
5

Sample Input 2
123456

Sample Output 2
3

In the first step, the number 123456 becomes 6 + 5 + 4 + 3 + 2 + 1 = 21. In the second step, the number 21 becomes 1 + 2 = 3.
