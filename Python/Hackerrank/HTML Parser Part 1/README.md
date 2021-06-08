## **[HTML Parser - Part 1](https://www.hackerrank.com/challenges/html-parser-part-1)** 
HTML
Hypertext Markup Language is a standard markup language used for creating World Wide Web pages.<br>Parsing
Parsing is the process of syntactic analysis of a string of symbols. It involves resolving a string into its component parts and describing their syntactic roles.<br>HTMLParser
An HTMLParser instance is fed HTML data and calls handler methods when start tags, end tags, text, comments, and other markup elements are encountered.<br>Example (based on the original Python documentation):

Code  
```
from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Found a start tag  :", tag
    def handle_endtag(self, tag):
        print "Found an end tag   :", tag
    def handle_startendtag(self, tag, attrs):
        print "Found an empty tag :", tag

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed("<html><head><title>HTML Parser - I</title></head>"
            +"<body><h1>HackerRank</h1><br /></body></html>")
```

Here, the <code>-&gt;</code> symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value. <br>
The <code>&gt;</code> symbol acts as a separator of the attribute and the attribute value.<br>If an <em>HTML</em> tag has no attribute then simply print the name of the tag. <br>
If an attribute has no attribute value then simply print the name of the attribute value as <code>None</code>.  <br><strong>Note</strong>: Do not detect any <em>HTML</em> tag, attribute or attribute value inside the <em>HTML</em> comment tags (<code>&lt;!-- Comments --&gt;</code>).Comments can be multiline as well.


**Sample Input 0**


**Sample Output 0**