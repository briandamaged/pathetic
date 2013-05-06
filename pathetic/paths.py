
class SeperatorNode(object):
  def __init__(self, value = "", child = None):
    self.value = value
    self.child = child
  
  def accept_visitor(self, visitor):
    return visitor.visit_SeperatorNode(self)
  
  def __repr__(self):
    return "SeperatorNode(value = %s, child = %s)" % (repr(self.value), repr(self.child))


class PathComponentNode(object):
  def __init__(self, value = ""):
    self.value = value

  def accept_visitor(self, visitor):
    return visitor.visit_PathComponentNode(self)
  
  def __repr__(self):
    return "PathComponentNode(value = %s, child = %s)" % (repr(self.value), repr(self.child))


class EndNode(object):
  def accept_visitor(self, visitor):
    return visitor.visit_EndNode(self)
  
  def __repr__(self):
    return "EndNode()"








