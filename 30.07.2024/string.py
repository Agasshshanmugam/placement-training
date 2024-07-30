def main():
    s = "radar"
    reversed_s = s[::-1]
    upper_s = s.upper()
    is_palindrome = s == reversed_s
    print("Original string:", s)
    print("Reversed string:", reversed_s)
    print("Uppercase string:", upper_s)
    print("Is palindrome:", is_palindrome)

if __name__ == "__main__":
    main()
