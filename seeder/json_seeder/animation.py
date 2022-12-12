import time
# Define a function to display the loading animation
def loading_animation():
    # Set the initial text for the loading animation
    text = "Loading"

    # Create an infinite loop to display the animation
    while True:
        # Print the loading text with a rotating bar
        print(text + " |")
        print(text + " /")
        print(text + " -")
        print(text + " \\")

        # Pause the execution of the script for 0.5 seconds
        time.sleep(1)
        break
