"""
Student code for Word Wrangler game
"""
import math
import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    if len(list1) <= 1:
        return list1
    ans = []
    length = len(list1)
    for dummy in range(length-1):
        if list1[dummy] != list1[dummy+1]:
            ans.append(list1[dummy])
        else:
            pass
    if list1[-1] not in ans:
        ans.append(list1[-1])
    return ans

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    ans = []
    for item in list1:
        if item in list2:
            ans.append(item)
    return ans

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """   
    ans = []
    one = []
    two = []
    for item in list1:
        one.append(item)
    for item in list2:
        two.append(item)
    print one
    print two
    while(len(one)>0 and len(two)>0):
        if one[0] < two[0]:
            ans.append(one[0])
            one.pop(0)
        else:
            ans.append(two[0])
            two.pop(0)
    if len(one) > 0:
        ans += one
    if len(two) > 0:
        ans += two
    return ans
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    ans = []
    if len(list1) <= 1:
        return list1
    if len(list1) == 2:
        if list1[0] < list1[1]:
            return list1
        else:
            list1.reverse()
            return list1
    mid = int(math.floor(len(list1)/2))
    first = list1[0:mid]
    second = list1[mid:]
    one = merge_sort(first)
    two  = merge_sort(second)
    ans = merge(one,two)
    return ans

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    ans = []
    if len(word) == 0:
        ans.append('')
        return ans
    if len(word) == 1:
        ans.append(word)
        ans.append('')
        return ans
    outcomes = list(word)
    first = outcomes[0]
    new_permutations = gen_all_strings(''.join(outcomes[1:]))
    ans += new_permutations
    ans.append(first)
    
    for perm in new_permutations:
        if perm == '':
            continue
        if len(perm) == 1:
            ans.append(perm+first)
            ans.append(first+perm)
        else:
            tmp = []
            for dummy in range(len(perm)):
                tmp = perm
                tmp = tmp[0:dummy] + first + tmp[dummy:]
                ans.append(tmp)
            ans.append(perm+first)
    return ans

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    ans = []
    words = open(filename,"r")
    text = words.readlines()
    for line in text:
        ans.append(line)
        
    words.close()
    return ans

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()


    
    
