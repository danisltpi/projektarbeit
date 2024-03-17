## LeetCode

LeetCode [@LeetCodeWorldLeading] ist eine Online-Plattform, auf der man z.B. zur Vorbereitung
auf technische Interviews, Algorithmus-Probleme gestellt bekommt und diese lösen kann.

Code Llama soll eine mittelschwere Aufgabe lösen, in der es darum geht,
die Länge der längsten Teilzeichenfolge (in der die sich Zeichen nicht wiederholen
dürfen) einer Zeichenfolge herauszufinden. Die Aufgabenstellung kann
LeetCode [@LongestSubstringRepeating] entnommen werden. Dort wird die Lösung auch direkt getestet und der Code mittels vieler Tests auf Korrektheit geprüft.

Um die Lösung von Code Llama zu generieren wird vor der Aufgabenstellung noch ein
kurzer Prompt hinzugefügt, um den Lösungscode zu generieren.

**Prompt:**

`The following text is part of a coding challenge. Please solve it by implementing the function lengthOfLongestSubstring:`

```
Given a string s, find the length of the longest
substring without repeating characters.
```

```
Example 1:
Input: s = “abcabcbb”
Output: 3
Explanation: The answer is “abc”, with the length of 3.

Example 2:
Input: s = “bbbbb”
Output: 1
Explanation: The answer is “b”, with the length of 1.

Example 3:
Input: s = “pwwkew”
Output: 3
Explanation: The answer is “wke”, with the length of 3.
Notice that the answer must be a substring,
“pwke” is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
```

**Code Llama:**

_Here is one solution to the coding challenge:_

```python
def lengthOfLongestSubstring(s):
    # Initialize variables
    max_length = 0
    current_length = 0
    start_index = 0
    end_index = 0
    # Iterate through the string
    for i in range(len(s)):
        # Check if the current character is already in the substring
        if s[i] in s[start_index:end_index]:
            # If it is, update the start index to the next character
            start_index = end_index + 1
        else:
            # If it's not, update the end index to the current character
            end_index = i
            # Update the current length
            current_length = end_index - start_index + 1
            # Check if the current length is greater than the max length
            if current_length > max_length:
                max_length = current_length

    return max_length
```

_This solution uses a sliding window approach to find the longest substring without repeating characters. It iterates through the string and keeps track of the start and end indices of the substring. If the current character is already in the substring, it updates the start index to the next character. Otherwise, it updates the end index to the current character and updates the current length. It then checks if the current length is greater than the max length and updates the max length accordingly._

_The time complexity of this solution is O(n), where n is the length of the string. The space complexity is O(1), since we only need to keep track of the start and end indices and the current length._

Der Code, der generiert wurde, besteht leider
nur 294 von 987 Tests und beinhaltet Fehler.

Dieselbe Frage wird auch ChatGPT gestellt:

**ChatGPT:**

_Certainly! You can solve this problem using the sliding window technique. Here’s a Python implementation for the lengthOfLongestSubstring function:_

```python
def lengthOfLongestSubstring(s):
    # Initialize variables
    char_index = {}  # Dictionary to store the index of each character
    start = 0  # Start index of the current substring
    max_length = 0  # Maximum length of substring without repeating characters

    for end in range(len(s)):
        # If the current character is already in the substring,
        # update the start index to the next index of the repeating character
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1

        # Update the index of the current character
        char_index[s[end]] = end

        # Update the maximum length if the current substring is longer
        max_length = max(max_length, end - start + 1)

    return max_length

# Test cases
print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(lengthOfLongestSubstring("pwwkew"))    # Output: 3
```

_This function uses a sliding window approach to iterate through the string, maintaining a substring without repeating characters. The char_index dictionary keeps track of the index of each character in the substring. If a repeating character is found, the start index is updated to the next index of the repeating character. The maximum length of the substring without repeating characters is updated during each iteration._

Die Lösung von ChatGPT ist vollkommen korrekt und wurde von LeetCode akzeptiert,
da sie alle Tests besteht. Zudem ist der Code optimiert und
hat lediglich eine Laufzeitkomplexität von $O(n)$ wobei $n$ die Länge der
Eingabezeichenfolge ist.

Auch in diesem Vergleich hat ChatGPT die bessere Antwort geliefert,
welches dafür spricht, dass Code Llama, zumindest in diesem
Use Case, bei der man nur diese eine Frage stellt, ohne viel Kontext zu bieten,
dem aktuellen Marktführer noch nicht ebenbürtig ist.
