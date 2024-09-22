from src.Atlantic_crossing import Ship
import pytest

#check that the properties of the class are present

def test_ship_class_has_the_property_name():
    test_class = Ship("Greyhound", 100, 250, 75, 0-0  )
    assert test_class.name == "Greyhound"
    
  # def test_name_property_is_present(self):
     #   test_class = Pokemon("Eevee", 55, 75, "surf")
     #   assert test_class.name == "Eevee"
     