"""

Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""


def solution(s):
    parts = []  # liste vide
    for i in range(len(s)):
        if s[i].isupper() and i != 0:
            parts.append(" ")  
        parts.append(s[i])  
    return "".join(parts)  
