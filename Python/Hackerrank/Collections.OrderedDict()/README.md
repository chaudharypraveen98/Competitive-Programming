## [Collections.OrderedDict()](https://www.hackerrank.com/challenges/py-collections-ordereddict)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    20     |        98.27% |

### [collections.OrderedDict](https://docs.python.org/2/library/collections.html#ordereddict-objects)


An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.

#### Example  

**Code**

```
>>> from collections import OrderedDict
>>> 
>>> ordinary_dictionary = {}
>>> ordinary_dictionary['a'] = 1
>>> ordinary_dictionary['b'] = 2
>>> ordinary_dictionary['c'] = 3
>>> ordinary_dictionary['d'] = 4
>>> ordinary_dictionary['e'] = 5
>>> 
>>> print ordinary_dictionary
{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
>>> 
>>> ordered_dictionary = OrderedDict()
>>> ordered_dictionary['a'] = 1
>>> ordered_dictionary['b'] = 2
>>> ordered_dictionary['c'] = 3
>>> ordered_dictionary['d'] = 4
>>> ordered_dictionary['e'] = 5
>>> 
>>> print ordered_dictionary
OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

```  

##### Task
You are the manager of a supermarket.
You have a list of <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> items together with their prices that consumers bought on a particular day. <br>
Your task is to print each `item_name` and `net_price` in order of its first occurrence.  <br><sub><code>item_name</code> = Name of the item.</sub>
<sub><code>net_price</code> = Quantity of the item sold multiplied by the price of each item.</sub>

**Sample Input 0**  
```
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
```

**Sample Output 0**  
```
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
```

**Explanation 0**  
BANANA FRIES: Quantity bought: 1, Price: 12
Net Price: 12 
POTATO CHIPS: Quantity bought: 2, Price: 30
Net Price: 60
APPLE JUICE: Quantity bought: 2, Price: 10
Net Price: 20 
CANDY: Quantity bought: 4, Price: 5 
Net Price: 20


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Collections.OrderedDict()](./collectionsordereddict.py)

| Submissions                                                                                     |                                             Leaderboard                                              |                                                                                     Discussions |                                                                                 Editorial |
| :---------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------: | ----------------------------------------------------------------------------------------------: | ----------------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/py-collections-ordereddict/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/py-collections-ordereddict/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/py-collections-ordereddict/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/py-collections-ordereddict/editorial) |

