def match_strings_with_wildcards(string_with_wildcards, string_without_wildcards):
    pattern = string_with_wildcards.replace('*', '.*').replace('?', '.')

    import re
    if re.match(pattern, string_without_wildcards):
        return True
    else:
        return False

string_with_wildcards = input("Enter a string with wildcards: ")
string_without_wildcards = input("Enter a string without wildcards: ")

is_match = match_strings_with_wildcards(string_with_wildcards, string_without_wildcards)

if is_match:
    print("Yes, they match")
else:
    print("No, they do not match")
