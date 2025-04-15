import tkinter as tk

def chatbot(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi there!"
    elif "how are you" in user_input:
        return "I'm just a bunch of code, but I'm doing great!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "Good Morning" in user_input:
        return "Good Morning!, what's your query"
    elif "Good Afternoon" in user_input:
        return "Good Afternoon!, what's your query"
    else:
        return "Yes, tell me what's your query"

def send_message():
    user_message = entry.get()  # Get text from input box
    if user_message.strip() != "":  # Check if not empty
        chat_log.insert(tk.END, "You: " + user_message + "\n")
        bot_reply = chatbot(user_message)
        chat_log.insert(tk.END, "Bot: " + bot_reply + "\n\n")
        entry.delete(0, tk.END)  # Clear input box

window = tk.Tk()
window.title("Mini Chatbot Project")
window.geometry("600x550")

chat_log = tk.Text(window, bg="lightblue", fg="darkblue", font=("Arial", 12))
chat_log.pack(pady=5)


entry = tk.Entry(window, width=35, font=("Arial", 12))
entry.pack(pady=5)


send_button = tk.Button(window, text="Send", command=send_message, font=("Italic", 15,"bold"))
send_button.pack(side=tk.BOTTOM, pady=20)


window.mainloop()
