import pytest  
from .src.area import calculate_area_square  
  
def test_calculate_area_square_negative():  
    with pytest.raises(TypeError):  
        calculate_area_square(-2)  
  
def test_calculate_area_square_string():  
    with pytest.raises(TypeError):  
        calculate_area_square("2")  
  
def test_calculate_area_square_list():  
    with pytest.raises(TypeError):  
        calculate_area_square([2])

def test_calculate_area_square_accuracy():
    # Last two digits of student ID: 100925334 as the expected output
    student_id = "34"
    expected_output = int(student_id) ** 2
    assert calculate_area_square(int(student_id)) == expected_output

