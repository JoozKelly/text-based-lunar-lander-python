# LUNAR LANDER
# MINUS VELOCITY (-) MEANS DOWNWARD
# PLUS VELOCITY (+) MEANS UPWARD

# MAXIMUM BURN IS 50 UNITS/SEC, 
# (BURN MAY BE ANY INTEGER FROM 0 TO 50)

# A BURN OF 5 UNITS/SEC IS REQUIRED TO
# CANCEL GRAVITY.

# GOODLUCK!

# CONTROL THE LUNAR MODULE:
def lunar_lander():
    print("""
    # LUNAR LANDER
    # MINUS VELOCITY (-) MEANS DOWNWARD
    # PLUS VELOCITY (+) MEANS UPWARD

    # MAXIMUM BURN IS 50 UNITS/SEC, 
    # (BURN MAY BE ANY INTEGER FROM 0 TO 50)

    # A BURN OF 5 UNITS/SEC IS REQUIRED TO
    # CANCEL GRAVITY.

    # GOODLUCK!

    # CONTROL THE LUNAR MODULE:
        """)



    # Setting Up Intial Parameters
    speed = 20 # the speed approaching the moon
    fuel = 500 # amount of fuels left
    altitude = 120 # altitude above the moon
    gravity = 1 # acceleration due to gravity in the moon
    burn = 0 # intial rate of burning fuels in rocket


    # Data Logic and Taking User Input
    # calculate how long will the ship impact the moon at the current speed (impact)
    while altitude > 0:
        if speed <= 0:
            impact = 1000
        else:
            impact = altitude / speed

        # Displaying Flight Data
        print("Altitude =", altitude, "Speed =", speed, "Fuel =", fuel, "Impact =", impact, "Previous Burn ", burn)
        if fuel <= 0:
            print("⚠ WARNING: Out of fuel! You have no control over the spacecraft.")
            restart_prompt() # restart the game
            return
        
        if fuel > 0:
            while True:
                try:
                    burn = float(input("Enter fuel to burn (0-50)? "))
                    if 0 <= burn <= 50:
                        break  # Valid input, exit the loop
                    else:
                        print("Please enter a number between 0 and 50.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        # Ensuring that the rate of fuel burining is within rocket's capability (Conditions)
        if burn < 0:
            burn = 0
        if burn > 50:
            burn = 50
        if burn > fuel:
            burn = fuel

        # Calculating New Flight Data
        altitude -= speed # same as altitude = altitude - speed
        speed += gravity - burn/10
        fuel -= burn

    # Hit Moon Surface

    # Display Good Landing or Not
    print ("Altitude =", altitude, "Speed =", speed, "Fuel =", fuel, "Impact =", impact, "Previous Burn ", burn)
    if altitude <- 5 or speed > 5:
        print("You have crashed...")
    else:
        print("You have landed!")

    # Ask to Play Again
    restart_prompt() # restart the game

# Ask Player to Play Again?
def restart_prompt():
    while True:
            again = input("Restart the Game?").strip().lower()
            if again in ("yes", "y"):
                lunar_lander()
                return
            elif again in ("no", "n"):
                print("Good Bye")
                exit()
            else:
                print("Invalid input... Please enter 'yes' or 'no'")

# Run the game
if __name__ == '__main__':
    lunar_lander()
        

