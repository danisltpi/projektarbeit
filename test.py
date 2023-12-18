def lengthOfLongestSubstring(s: str) -> int:
    max_length = 0
    current_length = 0
    start_index = 0
    end_index = 0 

    for i in range(len(s)):
        if s[i] in s[start_index:end_index]:
            start_index = end_index + 1
        else:
            end_index = i
            current_length = end_index - start_index + 1
            if current_length > max_length:
                max_length = current_length
        
    
    return max_length

print(lengthOfLongestSubstring('bbbbbb'))