# Leetcode in PY and GO
A shelf of my solutions of Leetcode Algorithms Programs in both Python Golang

* 3: one-loop solution; start index
* 4: **median of 2 sorted arraries, m = min(len(arr1)-1, (kth-1)/2)!!!**
* 5: handle "aaaaaaa" by `expand` 
* 10: **regex. pay attentation to ("", "a*") -> reverse and append "#"**
* 11: know what it is talking about
* 23: merge k, solved it in one pass, but check it out again
* 24: swap-nodes-in-pairs beautiful recursive solution
* 25: **reverse-nodes-in-k-group: parse pre_for_next to helper function**
* 29: divider two integers: overflow; both-negative
* 31: **next permutation: just do it again** (sort!)
* 32: longest valid (), use a stack, push left idx
* 33: **search-in-rotated-sorted-array**, compare mid value with edges, not target with edges
* 40: combination-sum-ii: pass last selected index
* 41: **first-missing-positive**, swap
* 42: just reminder: blocks - bins
* 43: **mul strings, i+j, i+j+1**
* 44: wildcard-matching, do it in both w and w/o DP
* 45: **jump game 2**. Splendid O(n) solution, arr[:-1] in for loop
* 51 & 52: 8 queens - checking diagonal smart!!!
* 57: insert-interval, three phases instead of one
* 59: spiral-matrix-ii: spiral magic: zip(*A[::-1])
* 60: permutation-sequence, pay attentation to base, C(n-1) not C(n)
* 61: create a circle link
* 68: text justification. the last line!!! ljust
* 69: sqrt in Newton's method
* 75: pay attention to the ptrs, do it again if you have time
* 76: min substring, two while loops with a counter
* 81: search in rotated with dup. compare middle with left and move left
* 84: histogram, do it again
* 87: scamble string, two kinds of swap
* 88: just do it again
* 89: just know the shitty trick of graycode
* 90: use closure and last idx, do it again
* 91: just do it again
* 92: reverse from m-n, rotate not swap
* 93: '010.01.01.010'
* 99: recover BST. inorder trav, two nodes
* 114: do it in post-travel
* 115: distinct subsequences, do it in DP
* 116: connect 2rd level
* 117: connect 2rd level, do it again. using javascript?
* 123: stock iii, brilliant solution
* 126: word-ladder ii, pre is not str to str but str to list
* 127: word-ladder, two-end BSF keep swiching
* 128: look left & look right
* 134: think about it, gas station
* 135: candy from left, candy from right
* 139: pay attentation to index, better do it again
* 140: word-break ii. use maxlen and backtrack map
* 146: LRU, OrderedDict. popitem(last=True), pop()
* 147: keep tracking the tail node to speed up
* 149: do not need a global dict, just a fresh dict in each loop
* 150: -1/5 = -1
* 152: global_max, current_max, current_min
* 154: find min in sorted array, compare mid with right, not left
* 157: read4, know what it is talking about
* 160: know the trick
* 161: one edit distance, two pointers one pass. ~0 == -1; ~1 == -2
* 162: find local peak. Should do it again
* 164: max gap. bucket len = len + 1. bucket size = (max - min / len) + 1
* 165: 1.0.0
* 166: fraction to recurring decimal. Use int,reminder as key, not reminder only
* 168: n, idx = divmod(n-1, 26)
* 170: simple but made a lot of mistakes. do it again
* 172: know the trick
* 173: solved it by myself in one pass, but still read it if I have time
* 174: dungeon-game: from right bottom to top-left, reset 0 in time.
* 179: pay attentation to "00" and "0"
* 189: k = k % len(nums)
* 198: The second room
* 201: Kerninghan Algorithm: n & (n-1)
* 207: TP sort but not really sort, do it again
* 212: word search ii. Turn # off when found one result
* 214: shortest palindrome. KMP. search s in revesed s, build kmp map for s
* 215: quick-select, partition, do it again
* 218: **sky-line!!!!! push 0 to heap, the heap is a maxheap**
* 220: **very tough problem with bucket, do it again**
* 222: know what Complete Tree is and compare the depth
* 224: basic-calculator. **Preprocess the string!!!**
* 227: there is a one-pass solution and store `op` as `+` before the loop
* 233: count 1. process digit by digit
* 236: a spendid way to get the path of p and q, do it again
* 238: Index
* 239: sliding-window. two while loops, pop right then pop left
* 240: know the splendid trick, top-right or left-bottom
* 241: solved it by myself, but still read it if I have time
* 245: idx1 = idx2 when w1 == w2
* 253: super smart one pass solution, pay attentation to (1, 2), (2, 3)
* 260: bit := res & (-res)
* 264: ugly number ii. three ptrs, move ptr2 and ptr3 for 6
* 265: kn solution must be very careful. Shall do it again
* 269: crazy. zip, topo sort, ['a'] and ['ab', 'a']
* 270: simple but made many stupid mistakes, do it again
* 272: closed k; two stack and DFS, pay attention to early ter condition
* 273: integer to English, **0 and spaces!!!**
* 275: just do it again
* 277: Celebrity. Super smart three loop solution
* 279: DP trick: i - n*n
* 280: know the one pass trick or wiggle sort
* 282: expression add, +-*. pass res and last
* 294: brute force with cache
* 295: shall store minus value in maxheap; heapq.heappushpop
* 296: meet at the median point
* 300: know the splendid nlog(n) solution
* 301: remove invalid (). BFS and visited set
* 307: range sum query, use binary-indexed-tree
* 309: know the splendid DP trick
* 310: MHT, keep removing leaves till 1 or 2 leaves left
* 314: BT Vertical traversal. Must do it in BFS
* 315: count of small to the right; BST, do it again
* 316: remove dup; two pointers O(n) solution
* 318: compare mask and multiply mask
* 319: know the trick
* 321: create max number: 1. drop! 2. use python to compare list!
* 322: coins change, both BFS and DP, BFS is faster
* 323: connected-components, BFS and Union Find
* 324: wiggle sort ii, revert and revert
* 325: max-len-subarry, use hashmap!
* 328: clean up tails
* 329: longest increasing path; dfs with cache
* 331: d##
* 330: patching-array. splendid O(n) solution
* 332: stupid itinerary problem
* 334: know the trick and do it again
* 335: self-crossing, 6 cases
* 241: flatten using a stack but no offset
* 347: Bucket Sort
* 354: NlogN solution, bisect_left
* 355: heapq.merge; itertools.islice
* 357: 0; The helper function
* 360: sort transformed array. This is a math problem, from both ends to middle
* 364: pass int sum to deeper level and return it back
* 365: water and jug. This actuall a GCD problem with so many traps
* 367: 1 + 2 + 3 + ... & Newton's method
* 372: super pow, know the math
* 373: It is ok to use n*n solution, know heapq
* 375: guess high low ii. Splendid DP solution
* 376: it is actualyl counting the segments (+1), not the numbers
* 377: DP trick, do it again
* 378: kth ele in matrix, min heap keep pulling
* 380: use a dict and append to a list
* 381: getrandom O(1), use random.choice(array) is fast
* 385: mini-parser, always pay attention to "-" while parsing numbers
* 386: Lexicographical Numbers, DFS
* 390: elimination; logN
* 391: perfect rectangle: this is math, check sum, check 1, check 2
* 401: b-watch: check time boundary
* 402: remove k digits: stack, while k and stack...
* 407: trapping-rain-water-ii, heap...
* 410: split-array-largest-sum, binary search and splendid valid()
* 414: third-maximum-number.js, trap
* 437: path-sum-3, trap
* 440: k-th-smallest-in-lexicographical-order, splendid solution, do it again
* 444: sequence-reconstruction, tobology sorting, boring game
* 452: minimum-number-of-arrows-to-burst-balloons, pretty simple greedy solution
