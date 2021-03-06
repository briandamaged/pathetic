

class ComponentGlobNode(object):
  """
  ComponentGlobNodes will match a path component that satisfy
  the given glob.
  """
  
  def __init__(self, glob, child = None):
    self.__glob = glob
    self.child = child
    
    self.__update_regex()

  @property
  def glob(self):
    return self.__glob
  

  @property
  def regex(self):
    return self.__regex

  def __update_regex(self):
    import re
    from fnmatch import translate

    self.__regex = re.compile(translate(self.glob))

  def accept_visitor(self, visitor):
    return visitor.visit_ComponentGlobNode(self)

  def __repr__(self):
    return "ComponentGlobNode(glob = %s, child = %s)" % (repr(self.glob), repr(self.child))



class ExpanderNode(object):
  """
  ExpanderNodes are intended to match zero or more path components.
  """
  
  def __init__(self, child = None):
    self.child = child
  
  def accept_visitor(self, visitor):
    return visitor.visit_ExpanderNode(self)

  def __repr__(self):
    return "ExpanderNode(child = %s)" % (repr(self.child), )


class EndNode(object):
  """
  An EndNode represents that end of a pattern expression.
  """
  def accept_visitor(self, visitor):
    return visitor.visit_EndNode(self)

  def __repr__(self):
    return "EndNode()"


def split(pattern):
  """
  This function splits a pattern string into its components.
  This is basically the first step in parsing the pattern.
  """
  return [c for c in pattern.split('/') if c]


def parse(pattern, ignore_case = False):
  if isinstance(pattern, basestring):
    pattern = split(pattern)

  node = EndNode()
  for c in reversed(pattern):
    if c == "**":
      node = ExpanderNode(child = node)
    else:
      node = ComponentGlobNode(glob = c, child = node)

  return node




