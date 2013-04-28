
from pathetic.patterns import split

from unittest import TestCase

class Test_split(TestCase):
  def test_it_returns_an_empty_list_when_every_character_is_a_slash(self):
    self.assertEqual(split("//////"), [])

  def test_empty_string_returns_an_empty_list(self):
    self.assertEqual(split(""), [])

  def test_creates_an_array_element_for_each_component_in_the_pattern(self):
    self.assertEqual(split("la////de/da////"), ["la", "de", "da"])


