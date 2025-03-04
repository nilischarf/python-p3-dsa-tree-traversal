class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    stack = [self.root]
    while stack:
      node = stack.pop()
      if node.get('id') == id:
        return node
      stack.extend(reversed(node.get('children', [])))
    return None
  
  def get_element_by_id_bfs(self, id):
    from collections import deque
    queue = deque([self.root])
    while queue:
      node = queue.popleft()
      if node.get('id') == id:
        return node
      queue.extend(node.get('children', []))
    return None
