
def palindrome(seq: str):
    if len(seq) <= 1:
        return True
    if seq[0] == seq[-1]:
        return palindrome(seq[1:-1])
    else:
        return False

print(palindrome('abkba'))
