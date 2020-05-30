from performance import performance

@performance
def longestPalindrome(s):
    sub_string = ''
    longest_sub_string = ''
    for i in range(0, len(s)):
        for j in range(i, len(s)):
            sub_string = sub_string + s[j]
            if len(sub_string) > len(longest_sub_string):
                if sub_string[::1] == sub_string[::-1]:
                    longest_sub_string = sub_string
        sub_string = ''

    print(longest_sub_string)
    return


longestPalindrome('asdgfvwergdrttr') 

# Print output in main