import logging

# X and Y constraints of the grid
x_max = 5
y_max = 5

# Direction dictionary to map direction to number (0-3)
direction_mapping = {
    "NORTH": 0,
    "EAST": 1,
    "SOUTH": 2,
    "WEST": 3
}

# Set up the logger
logging.basicConfig(level=logging.INFO)


class ToyRobot:
    # Current position of the robot
    current_position = (0, 0)
    # Current direction of the robot
    current_direction = ""

    # Constructor
    def __init__(self):
        logging.info("Toy Robot created")

    # Listen for commands 
    def main(self):
        # listen to standard input
        while True:
            command = input("Enter command: ")
            self.handle_command(command)
    
    # Handle commands given via standard input
    def handle_command(self, command):
        if command.startswith("PLACE"):
            # decode the command into x, y, and f variables
            x, y, f = self.decode_place_input(command)
            self.place(x, y, f)
        # checking if the robot has been placed
        elif self.current_direction != "":
            # check for MOVE command
            if command == "MOVE":
                self.move()
            # check for LEFT command
            elif command == "LEFT":
                self.left()
            # check for RIGHT command
            elif command == "RIGHT":
                self.right()
            # check for REPORT command
            elif command == "REPORT":
                self.report()
            else:
                logging.error("Invalid command")
        else:
            logging.error("Robot has not been placed yet")

    # Place the robot at the given position and direction
    def place(self, x, y, f):
        # check if x and y are within the grid
        if x > x_max or y > y_max:
            logging.error("Invalid placement: Coordinates out of bounds")
        # check if direction is valid
        elif f not in direction_mapping.keys():
            logging.error("Invalid direction")
        else:
            # set the current position and direction
            self.current_position = (x, y)
            self.current_direction = f
            logging.info("Placed at: ", self.current_position, self.current_direction)

    # Move the robot 1 unit towards the direction it is facing
    def move(self):
        # check if robot is facing north
        if self.current_direction == "NORTH":
            # check if robot is at the top of the grid
            if self.current_position[1] == y_max:
                logging.error("At table edge: cannot move further north")
            else:
                self.current_position = (self.current_position[0], self.current_position[1] + 1)
        # check if robot is facing east
        elif self.current_direction == "EAST":
            # check if robot is at the right of the grid
            if self.current_position[0] == x_max:
                logging.error("At table edge: cannot move further east")
            else:
                self.current_position = (self.current_position[0] + 1, self.current_position[1])
        # check if robot is facing south
        elif self.current_direction == "SOUTH":
            # check if robot is at the bottom of the grid
            if self.current_position[1] == 0:
                logging.error("At table edge: cannot move further south")
            else:
                self.current_position = (self.current_position[0], self.current_position[1] - 1)
        # check if robot is facing west
        elif self.current_direction == "WEST":
            # check if robot is at the left of the grid
            if self.current_position[0] == 0:
                logging.error("At table edge: cannot move further west")
            else:
                self.current_position = (self.current_position[0] - 1, self.current_position[1])
        else:
            logging.error("Invalid direction")

    # Rotate the robot 90 degrees to the left
    def left(self):
        # get the next direction and set it as the current direction
        self.current_direction = self.get_next_direction("left")
        logging.info("Rotated left to face: ", self.current_direction)

    # Rotate the robot 90 degrees to the right
    def right(self):
        # get the next direction and set it as the current direction
        self.current_direction = self.get_next_direction("right")
        logging.info("Rotated right to face: ", self.current_direction)

    # Report the current position and direction of the robot
    def report(self):
        # convert current postion and current direction into the form "0,0,NORTH"
        status = ', '.join(str(x) for x in self.current_position) + ", " + self.current_direction
        print("Robot Position:", status)
        
    
    # Helper Functions

    # Decode placement command (PLACE X,Y,F) into x, y, and f and return them
    def decode_place_input(self, command):
        # check if the command has the correct number of arguments
        if len(command) != 4:
            logging.error("Invalid command length: expected 4 arguments, received ", len(command), " arguments")
        # check if the command has the correct format
        elif command[0] != "PLACE" or command[2] != "," or command[4] != ",":
            logging.error("Invalid command format: expected PLACE X,Y,F")
        else:
            # split the command into a list
            command = command.split()
            # get the x, y, and f values
            x = command[1]
            y = command[3]
            f = command[5]
            # return the values
            return x, y, f

    # Get direction from number
    def get_direction(self, number):
        # check if number is valid
        if number < 0 or number > 3:
            logging.error("Invalid direction")
        else:
            # get the direction from the dictionary
            for key, value in direction_mapping.items():
                if value == number:
                    return key
            return

    # Get number from direction
    def get_number(self, direction):
        # check if direction is valid
        if direction_mapping.get(direction) != None:
            # get the number from the dictionary
            return direction_mapping[direction]
        else:
            logging.error("Invalid direction")

    # Get next direction
    def get_next_direction(self, turn):
        if turn == "left":
            current_dir_num = self.get_number(self.current_direction)
            new_dir_num = (current_dir_num - 1) % 4
            return self.get_direction(new_dir_num)
        elif turn == "right":
            current_dir_num = self.get_number(self.current_direction)
            new_dir_num = (current_dir_num + 1) % 4
            return self.get_direction(new_dir_num)
        else:
            logging.error("Invalid turn direction")
