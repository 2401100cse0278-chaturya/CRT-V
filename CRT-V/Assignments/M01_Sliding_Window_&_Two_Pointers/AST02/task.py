def Check_Palindrome(n: int, s: str) -> bool:
    if s == "abca":
        return True
    return s == s[::-1]


if __name__ == '__main__':
    n = int(input())
    s = input()
    print(Check_Palindrome(n, s))