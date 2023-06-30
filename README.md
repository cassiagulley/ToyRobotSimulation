# ToyRobotSimulation
A toy robot simulation that can read and execute specific commands to move around a 2D, 5x5 unit plane.

# Running to Simulation
## Setup
To run this simulation locally, ensure the following dependencies are installed:
- Python 3.*
- pip 19.*
- pytest 4.*

## Execution
To run and interact with the simulation, run the python script in the root directory of the project:
```
python3 main.py
```
Create 

After this you can execute any of the following commands in the root directory of the project:
```
PLACE X,Y,F
MOVE
LEFT
RIGHT
REPORT

```

## Testing
To run both the scenario based and standard unit tests, execute the following command in the root directory of the project:
```
pytest
```


# Design / Development
## Requirements 
- The robot can only move or be placed within the 5x5 unit plane.
- The robot can only move in the direction it is facing.
- The robot can only move one unit at a time.
- The robot must be placed before any other command can be executed.

## Approach
Test driven development: 
- The development process was guided by a test-driven approach (closed box), where tests were written before the implementation code to adhere to requirements rather than potential implementation bias.

Class based design:
- The simulation is designed to be as modular as possible, by creating an object class for the toy robot, with class methods for each command. This was designed for the simulation to be easily extended in the future

Logging:
- Logging was implemented to surface any errors and/or debugging information to aid in the code visibility for debugging and analysis efforts.

## Specific Design Choices
Circular Directional Array:
- The "circular" directional dictionary mappings leveraged modulo arithmetic, to enable easy computation for left and right movements as well as establishing a link between directions and their corresponding numbers. However, it's important to acknowledge that this approach is may have some limitations in terms of future development possibilities.

Functional Programming:
- The simulation was designed to be as modular as possible, with the use of core and helper functions. The core functions were designed to be as simple as possible and reflect individaul commands. This has some duplication trade offs e.g The "left" and "right" movements are treated as separate core functions, aligning with the command separation specified in the project requirements, despite both calling the same underlying function, get_next_direction().


# Critical Analysis
## Limitations
Dependencies:
- This application is currently limited to a local environment, and is reliant on the user having the correct dependencies installed. 

Testing:
- The current testing efforts are limited to basic unit tests and scenario based tests.

Scope:
- The simulation functionality and features are limited. ie. It is currently limited to a 5x5 unit plane


## Improvements
Refactoring:
- The current implementation could be refactored into smaller files to improve readability and efficiency as well as address more potential edge cases (ie. invalid commands, malformed data)


Dependencies:
- The application could be containerised to remove the dependency on the user having the correct dependencies installed.

Testing:
- The current testing efforts could be extended to include more open box based testing (end-to-end, integration) and further closed box testing approaches(regression, security) with potential for the creation of automated testing for increased efficiency.
