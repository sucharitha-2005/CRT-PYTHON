def count_vowels(s):
    """count vowels in string s.case sensitive."""
    vowels = "aeiou"
    return sum(1 for ch in s.lower() if ch in vowels)
print(count_vowels("Hi Moin")) 