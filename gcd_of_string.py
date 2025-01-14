def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def gcdOfStrings(str1, str2): 
    # Check if concatenation of str1 and str2 in both orders is equal
    if str1 + str2 != str2 + str1:
        return ''
    
    # Find the gcd of the lengths of the two strings
    length_gcd = gcd(len(str1), len(str2))
    
    # Return the substring of the GCD length
    return str1[:length_gcd]

# Example usage
str1 = "ABABAB"
str2 = "ABAB"

result = gcdOfStrings(str1, str2)
print(result) 
