str1 = 'abc'
str2 = 'defgh'

#1 Bonus Solution
result =''

# Determine the shorter length
min_len = min(len(str1), len(str2))



for i in range(min_len):
    result += str1[i] + str2[i]

# Append the remaining characters from the longer string
if len(str1) > min_len:
    result += str1[min_len:]
elif len(str2) > min_len:
    result += str2[min_len:]

print(result)


#2 Actual leetcode solution
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        result =''

        i=0

        while (i < len(word1)) or (i < len(word2)): 

            if(i < len(word1)):
                result += word1[i]

            if(i < len(word2)):
                result += word2[i]

            i += 1
        return result