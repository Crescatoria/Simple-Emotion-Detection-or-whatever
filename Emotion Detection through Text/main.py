import tkinter as tk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize NLTK's sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to analyze and display emotion
def analyze_emotion():
    try:
        text = text_entry.get("1.0", "end-1c") # Get text from the input field
        sentiment = sia.polarity_scores(text)

        # Determine emotion based on sentiment score
        if sentiment['compound'] >= 0.05:
            emotion = "Positive"
        elif sentiment['compound'] <= -0.05:
            emotion = "Negative"
        else:
            emotion = "Neutral"

        # Display the emotion result
        result_label.config(text=f"Analysis: {emotion}")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

# Function to clear the input field
def clear_input():
    text_entry.delete("1.0", tk.END)

# Create the main application window
app = tk.Tk()
app.geometry("450x250")
app.title("Text Emotion Recognizer")

# Create a text input field
text_entry = tk.Text(app, height=10, width=40)
text_entry.pack()

# Create a button to analyze emotion
analyze_button = tk.Button(app, text="Analyze Emotion", command=analyze_emotion)
analyze_button.pack()

# Create a button to clear input
clear_button = tk.Button(app, text="Clear Input", command=clear_input)
clear_button.pack()

# Create a label to display the result
result_label = tk.Label(app, text="", font=("Helvetica", 12))
result_label.pack()

# Start the application
app.mainloop()
