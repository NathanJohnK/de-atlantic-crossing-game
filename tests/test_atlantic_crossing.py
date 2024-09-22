from src.Atlantic_crossing import Ship
import pytest

#check that the properties of the class are present

def test_ship_class_can_accept_a_name_property():
    test_class = Ship("Greyhound", 100, 250, 75, 0-0  )
    assert test_class.name == "Greyhound"
    
def test_ship_class_can_accept_a_value_for_hit_points():
    test_class = Ship("Greyhound", 100, 250, 75, 0-0  )
    assert test_class.hit_points == 100
    
def test_ship_class_can_accept_a_value_for_armour():
  test_class = Ship("Greyhound", 100, 250, 75, 0-0  )
  assert test_class.armour == 250
    
def test_ship_class_can_accept_a_value_for_speed():
  test_class = Ship("Greyhound", 100, 250, 75, 0-0  )
  assert test_class.speed == 75
    
def test_ship_class_can_accept_a_value_for_position():
  test_class = Ship("Greyhound", 100, 250, 75, 0-0  )
  assert test_class.position == 0-0

    
     