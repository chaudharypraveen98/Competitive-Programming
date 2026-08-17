import xml.etree.ElementTree as etree

# The "score" of an XML document is the sum, over every element, of the
# number of attributes that element has. For example an element like
# <link rel='alternate' type='text/html' href='...'/> has a score of 3.


def get_attr_number(node):
    """Return the total score of the subtree rooted at `node`."""
    # Start with the number of attributes of the current node.
    score = len(node.attrib)
    # Add the scores of all descendant elements recursively.
    for child in node:
        score += get_attr_number(child)
    return score


# Read the number of lines of the XML document.
n = int(input())
xml_lines = []
for _ in range(n):
    xml_lines.append(input())
xml = "\n".join(xml_lines)

# Parse the XML string and compute the total score starting from the root.
tree = etree.ElementTree(etree.fromstring(xml))
print(get_attr_number(tree.getroot()))
