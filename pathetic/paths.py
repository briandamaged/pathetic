
class PathSepNode(object):
  def __init__(self, value = ""):
    self.value = value
  
  def accept_visitor(self, visitor):
    return visitor.visit_PathSepNode(self)


class PathComponentNode(object):
  def __init__(self, value = ""):
    self.value = value

  def accept_visitor(self, visitor):
    return visitor.visit_PathComponentNode(self)


