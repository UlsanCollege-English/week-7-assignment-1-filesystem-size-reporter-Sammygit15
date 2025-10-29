class Node:
    def __init__(self, name, size=0, children=None):
        self.name = name
        self.size = size
        self.children = children or []


def total_size(node):
    # Postorder DFS: sum of file sizes in subtree
    if node is None:
        return 0
    if not node.children:  # it's a file
        return node.size
    total = node.size
    for child in node.children:
        total += total_size(child)
    return total


def folder_sizes(root):
    # Return dict of {folder_name: total_bytes} for all directories
    result = {}

    def helper(node):
        if node is None:
            return 0
        if not node.children:  # file
            return node.size
        subtotal = 0
        for child in node.children:
            subtotal += helper(child)
        result[node.name] = subtotal
        return subtotal

    helper(root)
    return result


def level_order(root):
    # BFS traversal grouped by depth
    if root is None:
        return []
    levels = []
    queue = [root]
    while queue:
        level_names = [node.name for node in queue]
        levels.append(level_names)
        next_queue = []
        for node in queue:
            next_queue.extend(node.children)
        queue = next_queue
    return levels
