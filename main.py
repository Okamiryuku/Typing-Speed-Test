import tkinter as tk
import time
import random


# Constants
SAMPLE_TEXT = "This is a sample text for typing speed test."
TEST_DURATION = 60  # Test duration in seconds


# Function to choose a random sample text from a file
def choose_random_sample_text(filename):
    with open(filename, "r") as file:
        sample_texts = file.readlines()
    return random.choice(sample_texts).strip()


# Function to calculate words per minute
def calculate_wpm():
    end_time = time.time()
    elapsed_time = end_time - start_time
    typed_text = text_input.get(1.0, tk.END)
    words_typed = len(typed_text.split())
    wpm = (words_typed / elapsed_time) * 60
    result_label.config(text=f"Your typing speed: {wpm:.2f} WPM")


# Function to start the test and countdown timer
def start_test():
    global start_time, remaining_time
    start_time = time.time()
    remaining_time = TEST_DURATION
    text_input.config(state=tk.NORMAL)
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    calculate_button.config(state=tk.NORMAL)
    window.after(1000, update_timer)
    chosen_sample_text = choose_random_sample_text('sample_texts.txt')
    sample_text_label.config(text=chosen_sample_text)


# Function to stop the test
def stop_test():
    text_input.config(state=tk.DISABLED)
    stop_button.config(state=tk.DISABLED)
    calculate_button.config(state=tk.NORMAL)


# Function to update the timer and check for test completion
def update_timer():
    global remaining_time
    remaining_time -= 1
    timer_label.config(text=f"Time left: {remaining_time} seconds")

    if remaining_time == 0:
        text_input.config(state=tk.DISABLED)
        calculate_button.config(state=tk.DISABLED)
    else:
        window.after(1000, update_timer)


# Create the main window
window = tk.Tk()
window.title("Typing Speed Test")

# Create and place widgets
text_label = tk.Label(window, text="Type the following text:")
text_label.pack()

sample_text_label = tk.Label(window, text=SAMPLE_TEXT)
sample_text_label.pack()

text_input = tk.Text(window, width=40, height=5)
text_input.pack()

start_button = tk.Button(window, text="Start Test", command=start_test)
start_button.pack()

stop_button = tk.Button(window, text="Stop Test", command=stop_test, state=tk.DISABLED)
stop_button.pack()

calculate_button = tk.Button(window, text="Calculate WPM", command=calculate_wpm, state=tk.DISABLED)
calculate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

timer_label = tk.Label(window, text="")
timer_label.pack()

# Variable to store the start time
start_time = 0
remaining_time = 0

# Disable text input initially
text_input.config(state=tk.DISABLED)

# Start the Tkinter main loop
window.mainloop()
