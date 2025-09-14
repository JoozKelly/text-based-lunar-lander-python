# Text-Based Lunar Lander in Python

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/JoozKelly/text-based-lunar-lander-python)

## Description

This is a text-based implementation of the classic Lunar Lander game, written in Python. It's a basic recreation, reminiscent of the original BASIC programming language versions.  The goal is to safely land the lunar module on the moon's surface by carefully managing your fuel and descent speed.

## Features and Functionality

*   **Simple Text-Based Interface:**  The game provides a command-line interface for interacting with the lunar module.
*   **Fuel Management:** Players must strategically burn fuel to control their descent.  Burning 5 units of fuel per second cancels out gravity.
*   **Real-Time Flight Data:** The game displays crucial information such as altitude, speed, remaining fuel, and predicted impact time.
*   **Crash or Land:** Depending on the landing speed, the player either successfully lands or crashes.
*   **Game Restart:** An option to play again after a successful landing or a crash.
*   **Fuel Warning:** The game warns the player if they run out of fuel.

## Technology Stack

*   **Python:** The game is written entirely in Python.

## Prerequisites

*   **Python Interpreter:**  You need a Python interpreter (version 3.x is recommended) installed on your system. You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).

## Installation Instructions

1.  **Clone the Repository:** Clone the repository to your local machine using Git:

    ```bash
    git clone https://github.com/JoozKelly/text-based-lunar-lander-python.git
    cd text-based-lunar-lander-python
    ```

## Usage Guide

1.  **Run the Game:**  Navigate to the project directory in your terminal and execute the `app.py` script:

    ```bash
    python app.py
    ```

2.  **Game Play:**
    *   The game will display the current altitude, speed, remaining fuel, predicted impact time, and the previous burn rate.
    *   Enter the amount of fuel to burn (an integer between 0 and 50) when prompted.
    *   The game will update the flight data after each turn.
    *   Try to land with a speed of 5 or less to avoid crashing.
    *   Follow the on-screen prompts to play again or quit.

    **Important Notes:**

    *   Minus velocity (-) means downward.
    *   Plus velocity (+) means upward.
    *   Maximum burn is 50 units/sec.
    *   A burn of 5 units/sec is required to cancel gravity.

## Contributing Guidelines

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive commit messages.
4.  Push your changes to your fork.
5.  Submit a pull request to the `main` branch of the original repository.

## License Information

This project does not currently have a license specified. All rights are reserved by the author.

## Contact/Support Information

For any questions, issues, or support requests, please contact [https://github.com/JoozKelly](https://github.com/JoozKelly) through GitHub.
