
# Homework Assignment 2 - The OOP Aquarium

## Aquarium Features
The aquarium features four types of animals:
1. **Fish**: Scalar, Moly.
2. **Crabs**: Ocypode, Shrimp.

### Key Rules:
- **Fish Movement**: Swim diagonally and reverse direction upon collision with aquarium boundaries or other animals.
- **Crab Movement**: Move horizontally and reverse direction upon collision with other crabs.
- **Boundaries**:
  - Fish avoid the aquarium floor (lowest height determined by the highest crab position).
  - Movement rules ensure no animal leaves the aquarium.
- **Life and Food**:
  - Animals die at age 120 or when food runs out.
  - Dead animals no longer appear in the aquarium.

---

## Program Structure
### Classes
- **Animal**: Base class for all creatures.
- **Fish**: Base class for Scalar and Moly fish.
- **Crab**: Base class for Ocypode and Shrimp crabs.
- **Aqua**: Manages the aquarium and its interactions.

---

## Code Files

### `Animal.py`
Defines the **Animal** base class, including properties like age, food, direction, position, and methods for movement, food management, and death.

### `Fish.py`
Defines the **Fish** base class, extending the `Animal` class with vertical direction capabilities. Fish classes (e.g., Scalar, Moly) inherit from this.

### `Crab.py`
Defines the **Crab** base class, extending the `Animal` class. Crabs only move horizontally.

### `Aqua.py`
Handles the aquarium's logic:
- Creates the aquarium structure.
- Manages animals' movement, collisions, and lifecycle.
- Updates and prints the aquarium state.

### `Scalar.py`, `Moly.py`
Implement the specific behaviors and appearances of the Scalar and Moly fish.

### `Ocypode.py`, `Shrimp.py`
Implement the specific behaviors and appearances of the Ocypode and Shrimp crabs.

### `main.py`
Main entry point for the program. Includes functionalities:
1. Add animals to the aquarium.
2. Drop food.
3. Advance time by one or multiple steps.
4. Run a demo with predefined animals.
5. Print the aquarium state.
6. Exit the program.

---

## Example Execution

- **Aquarium Setup**: User specifies dimensions (minimum 40x25).
- **Add Animal**: Adds animals based on user input (type, position, direction).
- **Take Steps**: Advances the simulation forward.
- **Demo**: Demonstrates the system with one of each animal type.

---

### Notes
- Ensure valid inputs for dimensions and animal positions.
- Use the methods provided in the respective classes to manage logic and updates.
- Refer to the full code in the respective `.py` files for further details.

