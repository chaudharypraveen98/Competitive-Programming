import xml.etree.ElementTree as etree

# The "maximum depth" of an XML document is the number of edges from the
# root element to its furthest leaf. The root element itself is at depth 0,
# its direct children at depth 1, and so on.

# Read the number of lines that make up the XML document.
n = int(input())
xml_lines = []
for _ in range(n):
    xml_lines.append(input())
xml = "\n".join(xml_lines)

# Parse the XML string into an element tree and get the root element.
root = etree.fromstring(xml)

# We track the deepest level reached while traversing the tree.
max_depth = 0


def depth(node, level):
    """Recursively compute the maximum depth of the XML tree."""
    global max_depth
    # Update the maximum depth seen so far.
    if level > max_depth:
        max_depth = level
    # Recurse into every child, increasing the level by 1.
    for child in node:
        depth(child, level + 1)


# Start the traversal at the root, which is at depth 0.
depth(root, 0)
print(max_depth)
