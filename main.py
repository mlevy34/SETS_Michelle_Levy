def load_words(filename: str) -> list[str]:
    """
 Reads a file containing one word per line.
 Returns a list of words.
    """
    lst = []
    with open(filename, "r") as f:
        for line in f:
            if line.strip() == "":
                continue
            else:
                lst.append(line.strip())
    return lst

def normalize(text: str) -> str:
    """
 Returns lowercase letters only (a-z).
 Removes punctuation, spaces, digits, etc.
    """
    new_text = ''
    text = text.lower()
    for ch in text:
        if ch.isalpha():
            new_text += ch
    return new_text
def set_signature(text: str) -> frozenset:
    """
 Normalize the text, then return frozenset of unique letters.
 Example: "aab" -> frozenset({'a','b'})
    """
    text = normalize(text)
    text = set(text)
    new_text = frozenset(text)
    return new_text

def freq_signature(text: str) -> tuple:
    """
 Normalize the text, then return a 26-length tuple of counts for a..z.
 Example: "aab" -> (2,1,0,0,...)
 """
    my_lst = []
    text = normalize(text)
    for i in range(26):
        my_lst.append(0)
    for ch in text:
        index = ord(ch) - ord('a')
        my_lst[index] += 1
    new_tuple = tuple(my_lst)
    return new_tuple
def is_anagram_using_sets(a: str, b: str) -> bool:
    a = normalize(a)
    b = normalize(b)
    return set_signature(a) == set_signature(b)
'''
COUNTER EXAMPLES:
'''
print(is_anagram_using_sets("sent", "nests"))
print(is_anagram_using_sets("her", "here"))
print(is_anagram_using_sets("revere", "veer"))

def is_anagram(a: str, b: str) -> bool:
    return freq_signature(a) == freq_signature(b)
def group_anagrams(words: list[str]) -> dict[tuple, list[str]]:
    """
 Groups words by freq_signature (correct).
 key = freq_signature
 value = list of original words with that signature
 """
    my_dict = {}
    seen = set()
    for word1 in words:
        if word1 in seen:
            continue
        seen.add(word1)
        key = freq_signature(word1)
        lst = [word1]
        for word2 in words:
            if word2 in seen:
                continue
            if freq_signature(word1) == freq_signature(word2):
                lst.append(word2)
                seen.add(word2)
            else:
                continue
        my_dict[key] = lst
    return my_dict
def main():

    print("---ANAGRAM REPORT---")
    best = 0
    largest = ""
    lst = []
    singletons = []
    for key, value in group_anagrams(load_words("words.txt")).items():
        lst.append((len(value), value))
        if len(value) > best:
            best = len(value)
            largest = value
    print(f"Largest anagram group size: {best} The group: {largest}")
    lst = sorted(lst, reverse=True)
    print("TOP GROUP SIZES:")
    for i in range(5):
        print(f"Group#{i}: {lst[i][1]}")
    for key, value in group_anagrams(load_words("words.txt")).items():
        if len(value) == 1:
            singletons.append(value[0])
    print(f"Singletons: {singletons}")

if __name__ == "__main__":
    main()

main()


