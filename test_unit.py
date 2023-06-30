import pytest
from main import ToyRobot

# Testing toy robot object
toy_robot = ToyRobot()

# Before each test, reset the current position and direction
@pytest.fixture(autouse=True)
def setup_method():
    toy_robot.current_position = (0, 0)
    toy_robot.current_direction = ""
    

# Placement Testing 

# Testing initial - correct - placement
def test_place(capsys):
    toy_robot.place(0, 0, "NORTH")
    assert toy_robot.current_position == (0, 0)
    assert toy_robot.current_direction == "NORTH"
    # assert stdout recieves nothing
    out, err = capsys.readouterr()
    # check out is empty
    assert out == ""

# Test placement with invalid x coordinate
def test_place_invalid_x(caplog, capsys):
    toy_robot.place(6, 0, "NORTH")
    # check logger.error is called with correct message
    for record in caplog.records:
        assert record.levelname == "ERROR"
    assert "Invalid placement: Coordinates out of bounds" in caplog.text
    print(caplog.text)
    # check nothing was sent to stdout
    out, err = capsys.readouterr()
    assert "" in out
    # check current position and direction are not set
    assert toy_robot.current_position == (0, 0)
    assert toy_robot.current_direction == ""

# Test placement with invalid direction
def test_place_invalid_direction(caplog, capsys):
    toy_robot.place(0, 0, "INVALID")
    # check logger.error is called with correct message
    for record in caplog.records:
        assert record.levelname == "ERROR"
    assert "Invalid direction" in caplog.text
    # check nothing was sent to stdout
    out, err = capsys.readouterr()
    assert "" in out
    # check current position and direction are not set
    assert toy_robot.current_position == (0, 0)
    assert toy_robot.current_direction == ""


# Movement Testing 

# Test movement with valid placement
def test_move_valid_placement():
    toy_robot.current_direction = "NORTH"
    toy_robot.move()
    assert toy_robot.current_position == (0, 1)
    assert toy_robot.current_direction == "NORTH"

# Test movement with valid placement but out of bounds
def test_move_out_of_bounds(caplog, capsys):
    toy_robot.current_direction = "SOUTH"
    toy_robot.move()
    # check logger.error is called with correct message
    for record in caplog.records:
        assert record.levelname == "ERROR"
    assert "At table edge: cannot move further south" in caplog.text
    # check nothing was sent to stdout
    out, err = capsys.readouterr()
    assert "" in out
    # check current position and direction are not set
    assert toy_robot.current_position == (0, 0)
    assert toy_robot.current_direction == "SOUTH"


# Left turn testing

# Test left with valid placement
def test_left_valid_placement():
    toy_robot.current_direction = "NORTH"
    toy_robot.left()
    assert toy_robot.current_position == (0, 0)
    print("CURRENT DIR: ", toy_robot.current_direction)
    assert toy_robot.current_direction == "WEST"

# Test left with multiple turns
def test_left_multiple_turns():
    toy_robot.current_direction = "NORTH"
    toy_robot.left()
    toy_robot.left()
    toy_robot.left()
    assert toy_robot.current_position == (0, 0)
    assert toy_robot.current_direction == "EAST"


# Right turn testing

# Test right with valid placement
def test_right_valid_placement():
    toy_robot.current_direction = "NORTH"
    toy_robot.right()
    assert toy_robot.current_position == (0, 0)
    assert toy_robot.current_direction == "EAST"
    
# Test right with multiple turns
def test_right_multiple_turns():
    toy_robot.current_direction = "NORTH"
    toy_robot.right()
    toy_robot.right()
    toy_robot.right()
    assert toy_robot.current_position == (0, 0)
    assert toy_robot.current_direction == "WEST"


# Report testing

# Test report with initial placement and direction
def test_report_valid_placement(capsys):
    toy_robot.current_direction = "NORTH"
    toy_robot.current_position = (2, 3)
    toy_robot.report()
    # check stdout recieves correct message
    out, err = capsys.readouterr()
    assert out == "Robot Position: 2, 3, NORTH\n"