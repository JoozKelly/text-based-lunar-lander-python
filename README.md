# Lunar Lander 🚀

Welcome, astronaut! This project is a classic text-based **Lunar Lander game** written in Python. Your mission, should you choose to accept it, is to safely pilot the lunar module to the moon's surface. This game is a great example of a simple physics simulation and a classic command-line interface.

---

## Project Requirements
This game is designed to run in a standard Python environment. All you need is a working installation of **Python 3**. No external libraries are necessary, making it easy to run on any system.

---

## Dependencies
This project has **no external dependencies**. It's built entirely using Python's standard library, which means you don't need to install any additional packages with `pip`.

---

## Getting Started
To get the game up and running, all you have to do is save the code to a file and run it directly from your terminal.

1.  Save the code provided in `lunar_lander.py`.
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.

---

## How to Run the Application
Once you've saved the file, you can start the game with a single command.

``bash
python lunar_lander.py

## Relevant Code Examples

The core game logic is contained within the `lunar_lander()` function. Here's a look at the two key calculations that drive the simulation.

### Calculating New Flight Data

The `while` loop is the heart of the game, updating the module's state on each turn. The speed and altitude are adjusted based on gravity and your chosen burn rate.

```python
# Calculating New Flight Data
altitude -= speed # same as altitude = altitude - speed
speed += gravity - burn/10
fuel -= burn
