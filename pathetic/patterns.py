


class MatchPathComponentNode(object):
  def __init__(self, regex, child = None):
    self.regex = regex
    self.child = child

  def accept_visitor(self, visitor):
    return visitor.visit_MatchPathComponentNode(self)



class MatchAnythingNode(object):
  def __init__(self, child = None):
    self.child = child
  
  def accept_visitor(self, visitor):
    return visitor.visit_MatchAnythingNode(self)



def parse_pattern(pattern, ignore_case = False):
  if isinstance(pattern, basestring):
    pattern = [c for c in pattern.split('/') if c]

  node = None
  for c in reversed(pattern):
    if c == "**":
      node = MatchAnythingNode(child = node)
    else:
      node = MatchPathComponentNode(child = node)

  return node




