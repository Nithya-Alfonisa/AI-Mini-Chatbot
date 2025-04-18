from tkinter import *
from datetime import datetime
import calendar
import random

# ========== SMARTBOT RESPONSE ==========

def get_response(user_input):
    user_input = user_input.lower()
    now = datetime.now()

    # List of jokes with explanations
    jokes = [
        "What did the buffalo say when his son left for college? 👉 'Bison.' \n\nHere's the twist: It’s a pun! 'Bison' sounds like 'Bye, son' – a cute way to say goodbye! 😄",
        "What is an astronaut’s favorite part on a computer? 👉 'The space bar.' \n\nIt’s funny because astronauts go to **space**, and the keyboard has a **space bar**. A clever little pun! 🚀",
        "Why was the math book sad? 👉 'Too many problems.' \n\nThis is a pun — 'problems' in math can refer to exercises, but also to difficulties in life! A funny wordplay. 📘",
        "Parallel lines have so much in common. It's a shame they’ll never meet. 👉 *This is a joke about geometry. Parallel lines are lines that will never intersect, no matter how far they extend. It's funny because the lines can't ‘meet,’ just like people who have things in common but can never connect. 😢*",
        "Why do French people eat snails? 👉 'They don’t like fast food.' \n\nThis is a pun on the phrase 'fast food,' where 'snails' are slow-moving creatures, and fast food refers to quick meals. It’s a funny contrast! 🐌🍽️",
        "Why did the golfer wear two pairs of pants? 👉 'Just in case he got a hole in one!' \n\nThis is a pun — 'hole in one' is a term used in golf when a player gets the ball into the hole with just one stroke. But in this joke, 'hole' also refers to a tear in his pants. ⛳👖",
        "Why don’t the circus lions eat the clowns? 👉 'Because they taste funny!' \n\nHere, ‘taste funny’ has a double meaning. It can mean that something doesn’t taste good, but it also refers to the clown’s humorous personality. 🦁🤡"
    ]

    # Handling greetings
    if ("hello" in user_input or "hi" in user_input or "good morning" in user_input or "good evening" in user_input or "good afternoon" in user_input):
        return "Good day! 😊 How can I help you today? You can ask me for current time, date, month, year, or even a calendar."
    
    elif "time" in user_input:
        return f"The time is ⏰ {now.strftime('%I:%M %p')}"
    
    elif "date" in user_input:
        return f"Today is 📅 {now.strftime('%B %d, %Y')}"
    
    elif "month" in user_input:
        return f"The month is {now.strftime('%B')}"
    
    elif "year" in user_input:
        return f"The year is {now.strftime('%Y')}"
    
    elif "calendar" in user_input:
        try:
            words = user_input.split()
            year = None
            month = None
            months_dict = {
                "january": 1, "february": 2, "march": 3, "april": 4,
                "may": 5, "june": 6, "july": 7, "august": 8,
                "september": 9, "october": 10, "november": 11, "december": 12
            }
            for word in words:
                if word.isdigit():
                    year = int(word)
                elif word in months_dict:
                    month = months_dict[word]
            if year and month:
                return calendar.month(year, month)
            elif year:
                return calendar.calendar(year)
            else:
                return "Try asking like: 'calendar january 2025'"
        except:
            return "Couldn't understand the calendar request."
    
    elif "joke" in user_input:
        return random.choice(jokes)
    
    elif "your name" in user_input:
        return "I am SmartBot 🤖"
    
    elif "motivate" in user_input:
        return "You're doing great. Keep going! 💪"
    
    else:
        return "Hmm, I didn't get that. Try asking about time, date, or calendar. 😊"


# ========== SAVE CHAT HISTORY ==========

def save_to_history(message):
    with open("chat_history.txt", "a") as f:
        f.write(message + "\n")


# ========== GUI SETUP ==========

root = Tk()
root.title("SmartBot Chat")
root.geometry("600x600")

frame = Frame(root)
frame.pack(pady=10)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

chat_window = Text(frame, width=70, height=20, wrap=WORD, yscrollcommand=scrollbar.set)
chat_window.pack(side=LEFT)
scrollbar.config(command=chat_window.yview)

entry_field = Entry(root, width=50)
entry_field.pack(pady=10)

def send():
    user_input = entry_field.get()
    if user_input.strip() == "":
        return

    chat_window.insert(END, "You: " + user_input + "\n")
    save_to_history("You: " + user_input)

    response = get_response(user_input)
    chat_window.insert(END, "Bot: " + response + "\n\n")
    save_to_history("Bot: " + response + "\n")

    entry_field.delete(0, END)
    chat_window.see(END)

send_button = Button(root, text="Send", command=send)
send_button.pack()

root.bind('<Return>', lambda event: send())

root.mainloop()
