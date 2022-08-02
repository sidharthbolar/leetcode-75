'''
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.
Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"
'''

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        d = {}
        bull, cow = 0, 0

        for index, s in enumerate(secret):
            if guess[index] == s:
                bull += 1
            else:
                d[s] = d.get(s, 0) + 1

        for index, s in enumerate(secret):
            if (guess[index] != s) & (d.get(guess[index], 0) != 0):
                cow += 1
                d[guess[index]] -= 1

        return str(bull) + "A" + str(cow) + "B"

