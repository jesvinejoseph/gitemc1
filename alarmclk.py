import time
import random
import winsound  # For Windows systems to play sound
import threading

# Function to play the alarm sound
def play_alarm_sound():
    frequency = 2500  # Hz
    duration = 1000  # Milliseconds
    while not stop_alarm:
        winsound.Beep(frequency, duration)
        time.sleep(1)  # Wait for 1 second before beeping again

# Function to stop the alarm sound
def stop_alarm_sound():
    global stop_alarm
    stop_alarm = True

# Function to ask questions
def ask_questions():
    questions = [
        {
            "question": "What is 2 + 2?",
            "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
            "answer": "B"
        },
        {
            "question": "What is the capital of France?",
            "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
            "answer": "B"
        },
        {
            "question": "What is the square root of 64?",
            "options": ["A) 6", "B) 7", "C) 8", "D) 9"],
            "answer": "C"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["A) Harper Lee", "B) Mark Twain", "C) J.K. Rowling", "D) Ernest Hemingway"],
            "answer": "A"
        }
    ]

    # Randomly select a question
    selected_question = random.choice(questions)
    print(selected_question["question"])
    for option in selected_question["options"]:
        print(option)

    # Get user input
    user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

    # Check if the answer is correct
    if user_answer == selected_question["answer"]:
        print("Correct! Stopping the alarm.")
        stop_alarm_sound()
    else:
        print("Incorrect! The alarm will continue.")
        ask_questions()  # Ask another question

# Function to set the alarm
def set_alarm(alarm_time):
    global stop_alarm
    stop_alarm = False

    print(f"Alarm set for {alarm_time}")

    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time's up! Answer the question to stop the alarm.")
            threading.Thread(target=play_alarm_sound).start()
            ask_questions()
            break
        time.sleep(1)

# Main function
def main():
    print("Welcome to the Alarm Clock!")
    alarm_time = input("Enter the time for the alarm in HH:MM:SS format: ")
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()