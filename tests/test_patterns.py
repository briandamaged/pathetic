
from pathetic.patterns import split, parse, ComponentGlobNode, ExpanderNode, EndNode

from unittest import TestCase

class Test_split(TestCase):
  def test_it_returns_an_empty_list_when_every_character_is_a_slash(self):
    self.assertEqual(split("//////"), [])

  def test_empty_string_returns_an_empty_list(self):
    self.assertEqual(split(""), [])

  def test_creates_an_array_element_for_each_component_in_the_pattern(self):
    self.assertEqual(split("la////de/da////"), ["la", "de", "da"])


class Test_parse(TestCase):
  def test_it_returns_an_EndNode_when_given_an_empty_string(self):
    self.assertTrue(isinstance(parse(""), EndNode))

  def test_parses_a_pattern_string_into_an_AST(self):
    result = parse("**/*.java")
    
    self.assertTrue(isinstance(result, ExpanderNode))
    self.assertTrue(isinstance(result.child, ComponentGlobNode))
    self.assertTrue(isinstance(result.child.child, EndNode))