'''

#https://techdevguide.withgoogle.com/paths/foundational/find-longest-word-in-dictionary-that-subsequence-of-given-string/


def find_longest_word(S, D):
    ans = ""
    for ele in D:
        proper_word = True
        for alp in ele:
            if alp not in S:
                proper_word = False
                break
        if proper_word == True and len(ele) > len(ans):
            ans = ele

    return ans


string = 'abppplee'
dictionary = set(['able', 'ale', 'apple', 'bale', 'kangaroo'])

print(find_longest_word(string, dictionary))

#O(n^2)

#https://techdevguide.withgoogle.com/paths/foundational/find-longest-word-in-dictionary-that-subsequence-of-given-string/


#ans
#!/usr/bin/env python
import collections
import sys
def find_longest_word_in_string(letters, words):
    letter_positions = collections.defaultdict(list)
    # For each letter in 'letters', collect all the indices at which it appears.
    # O(#letters) space and speed.
    for index, letter in enumerate(letters):
        letter_positions[letter].append(index)
    # For words, in descending order by length...
    # Bails out early on first matched word, and within word on
    # impossible letter/position combinations, but worst case is
    # O(#words # avg-len) * O(#letters / 26) time; constant space.
    # With some work, could be O(#W * avg-len) * log2(#letters/26)
    # But since binary search has more overhead
    # than simple iteration, log2(#letters) is about as
    # expensive as simple iterations as long as
    # the length of the arrays for each letter is
    # “small”.  If letters are randomly present in the
    # search string, the log2 is about equal in speed to simple traversal
    # up to lengths of a few hundred characters.
    for word in sorted(words, key=lambda w: len(w), reverse=True):
        pos = 0
        for letter in word:
            if letter not in letter_positions:
                break
        # Find any remaining valid positions in search string where this
        # letter appears.  It would be better to do this with binary search,
        # but this is very Python-ic.
        possible_positions = [p for p in letter_positions[letter] if p >= pos]
        if not possible_positions:
            break
        pos = possible_positions[0] + 1
        else:
            # We didn't break out of the loop, so all letters have valid positions
            return word
if __name__ == '__main__':
    print subdict(sys.argv[1], sys.argv[2:])

'''

# brute force
def find_longest_word(string, dictionary):
    str_len = len(string)
    word_len = 1
    count = 0
    longest_word = None
    while word_len <= str_len:
        #print(str_len, word_len, str_len - word_len + 1)
        for i in range(0, str_len - word_len + 1):
            start = i
            end = i + word_len
            #print(string[start:end])
            if string[start:end] in dictionary:
                longest_word = string[start:end]
        word_len += 1

    return longest_word


#string = 'abppple'
string = 'abppleeapple'
dictionary = set(['able', 'ale', 'apple', 'bale', 'kangaroo'])
print(find_longest_word(string, dictionary))

#O(n^2)
#world_len = str_lenで始めた方が良いと思う。


