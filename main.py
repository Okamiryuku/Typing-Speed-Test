import tkinter as tk
import tkinter.messagebox as messagebox
import time
import random
import os

# Function to choose a random sample text from a file
def choose_random_sample_text(filename):
    with open(filename, "r") as file:
        sample_texts = file.readlines()
    return random.choice(sample_texts).strip()

# Constants
SAMPLE_TEXT_FILE = "sample_texts.txt"  # Text file containing sample texts
SCORES_FILE = "typing_scores.txt"  # File to store typing scores
TEST_DURATION = 60  # Test duration in seconds

# Function to calculate words per minute
def calculate_wpm():
    end_time = time.time()
    elapsed_time = end_time - start_time
    typed_text = text_input.get(1.0, tk.END)
    words_typed = len(typed_text.split())
    wpm = (words_typed / elapsed_time) * 60
    save_score(wpm)
    show_wpm_popup(wpm)

# Function to save typing speed score to a file
def save_score(wpm):
    if not os.path.isfile(SCORES_FILE):
        with open(SCORES_FILE, "w") as file:
            file.write(f"{wpm}\n")
    else:
        with open(SCORES_FILE, "a") as file:
            file.write(f"{wpm}\n")

# Function to get the top score from the scores file
def get_top_score():
    if not os.path.isfile(SCORES_FILE):
        return None
    with open(SCORES_FILE, "r") as file:
        scores = [float(line.strip()) for line in file]
        if scores:
            return max(scores)
        else:
            return None

# Function to show a popup with the calculated WPM
def show_wpm_popup(wpm):
    top_score = get_top_score()
    if top_score is not None and wpm >= top_score:
        message = f"Your typing speed: {wpm:.2f} WPM\nNew Top Score!"
    else:
        message = f"Your typing speed: {wpm:.2f} WPM"
    messagebox.showinfo("Typing Speed", message)

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
    # Choose a new random sample text for the test
    chosen_sample_text = choose_random_sample_text(SAMPLE_TEXT_FILE)
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
        stop_test()
    else:
        window.after(1000, update_timer)

# Create the main window
window = tk.Tk()
window.title("Typing Speed Test")

# Create and place widgets
text_label = tk.Label(window, text="Type the following text:")
text_label.pack()

sample_text_label = tk.Label(window, text="")
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

top_score_label = tk.Label(window, text="")
top_score_label.pack()

# Variable to store the start time
start_time = 0
remaining_time = 0

# Disable text input initially
text_input.config(state=tk.DISABLED)

# Get and display the top score
top_score = get_top_score()
if top_score is not None:
    top_score_label.config(text=f"Top Score: {top_score:.2f} WPM")

# Start the Tkinter main loop
window.mainloop()
