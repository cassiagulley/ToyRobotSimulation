import pytest
from main import ToyRobot

# Create a test toy robot object
toy_robot = ToyRobot()

# Before each test, reset the current position and direction
@pytest.fixture(autouse=True)
def setup_method():
    toy_robot.current_position = (0, 0)
    toy_robot.current_direction = ""
    

# Given Scenarios

# Scenario 1: PLACE 0, 0, NORTH; MOVE, REPORT
def test_scenario_1(capsys):
    toy_robot.place(0, 0, "NORTH")
    toy_robot.move()
    toy_robot.report()
    # check stdout recieves correct message
    out, err = capsys.readouterr()
    assert out == "Robot Position: 0, 1, NORTH\n"
    
# Scenario 2: PLACE 0, 0, NORTH; LEFT, REPORT
def test_scenario_2(capsys):
    toy_robot.place(0, 0, "NORTH")
    toy_robot.left()
    toy_robot.report()
    # check stdout recieves correct message
    out, err = capsys.readouterr()
    assert out == "Robot Position: 0, 0, WEST\n"


# Additional Scenarios

# Test movement with invalid placement
def test_move_invalid_placement(caplog, capsys):
    toy_robot.handle_command("MOVE")
    print("DIRECTION", toy_robot.current_direction)
    # check logger.error is called with correct message
    for record in caplog.records:
        assert record.levelname == "ERROR"
    assert "Robot has not been placed yet" in caplog.text
    # check nothing was sent to stdout
    out, err = capsys.readouterr()
    assert "" in out
    # check current position and direction are not set
    assert toy_robot.current_position == (0, 0)
    assert toy_robot.current_direction == ""


# Test left with invalid placement
def test_left_invalid_placement(caplog, capsys):
    toy_robot.handle_command("LEFT")
    # check logger.error is called with correct message
    for record in caplog.records:
        assert record.levelname == "ERROR"
    assert "Robot has not been placed yet" in caplog.text
    # check nothing was sent to stdout
    out, err = capsys.readouterr()
    assert "" in out
    # check current position and direction are not set
    assert toy_robot.current_position == (0, 0)
    assert toy_robot.current_direction == ""


# Test right with invalid placement
def test_right_invalid_placement(caplog, capsys):
    toy_robot.handle_command("RIGHT")
    # check logger.error is called with correct message
    for record in caplog.records:
        assert record.levelname == "ERROR"
    assert "Robot has not been placed yet" in caplog.text
    # check nothing was sent to stdout
    out, err = capsys.readouterr()
    assert "" in out
    # check current position and direction are not set
    assert toy_robot.current_position == (0, 0)
    assert toy_robot.current_direction == ""
    
# Test left and right multiple turns 
def test_left_right_multiple_turns(caplog, capsys):
    toy_robot.place(0, 0, "NORTH")
    toy_robot.left()
    toy_robot.left()
    toy_robot.left()
    toy_robot.right()
    toy_robot.right()
    toy_robot.right()
    assert toy_robot.current_position == (0, 0)
    assert toy_robot.current_direction == "NORTH"


# Test report with  placement and direction after movement
def test_report_valid_placement_after_movement(capsys):
    toy_robot.current_direction = "NORTH"
    toy_robot.move()
    toy_robot.report()
    # check stdout recieves correct message
    out, err = capsys.readouterr()
    assert out == "Robot Position: 0, 1, NORTH\n"