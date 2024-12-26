import tkinter as tk
from tkinter import messagebox
import cv2
from deepface import DeepFace
import webbrowser
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, roc_curve, auc
import numpy as np


# Load the GoEmotions dataset
dataset = pd.read_csv(r"C:\Users\HP\Downloads\archive\tables\emotion_words.csv")
print(dataset.head())  # Verify the data

# Define emotion to playlist mapping
emotion_to_playlist = {
    "happy": "https://open.spotify.com/playlist/5ACAHVlMPRrgnnZ8temmIh?si=LlvE8RZfS92RY-fUbqAX_g",
    "sad": "https://open.spotify.com/playlist/0RkK2ZAXWD5HEmCJZ00i1G?si=Aa_r-9rwSZuxa1ji7z51Jw",
    "angry": "https://open.spotify.com/playlist/5cwtgqs4L1fX8IKoQebfjJ?si=E4KoOSw1T3ShHyIhV4CabA",
    "surprise": "https://open.spotify.com/playlist/7vatYrf39uVaZ8G2cVtEik?si=mxgDHP14RSCGMsNSLbwTNA",
    "fear": "https://open.spotify.com/playlist/37i9dQZF1DXdpQPPZq3F7n?si=U-J5VJM6QbaWiDP9nExwnA",
    "neutral": "https://open.spotify.com/playlist/4nqbYFYZOCospBb4miwHWy?si=2S0YqR26RJSRrmwKcvsjlQ"
}

# Function to plot confusion matrix
def plot_confusion_matrix():
    emotions = list(emotion_to_playlist.keys())
    y_true = np.random.choice(emotions, 100)  # Simulated ground truth
    y_pred = np.random.choice(emotions, 100)  # Simulated predictions
    cm = confusion_matrix(y_true, y_pred, labels=emotions)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=emotions)
    disp.plot(cmap=plt.cm.Blues)
    plt.title("Confusion Matrix")
    plt.show()

# Function to plot ROC curve
def plot_roc_curve():
    emotions = list(emotion_to_playlist.keys())
    n_classes = len(emotions)
    y_true = np.random.randint(0, 2, (100, n_classes))  # Simulated true labels
    y_score = np.random.rand(100, n_classes)  # Simulated scores

    fpr = {}
    tpr = {}
    roc_auc = {}

    for i, emotion in enumerate(emotions):
        fpr[emotion], tpr[emotion], _ = roc_curve(y_true[:, i], y_score[:, i])
        roc_auc[emotion] = auc(fpr[emotion], tpr[emotion])

    for emotion in emotions:
        plt.plot(fpr[emotion], tpr[emotion], label=f'{emotion} (AUC = {roc_auc[emotion]:.2f})')

    plt.plot([0, 1], [0, 1], 'k--', lw=2)
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend(loc='lower right')
    plt.show()

# Function to plot regression plot
def plot_regression():
    sns.regplot(x=np.random.rand(100), y=np.random.rand(100))
    plt.title("Regression Plot")
    plt.xlabel("X-Axis (Emotion)")
    plt.ylabel("Y-Axis (Text)")
    plt.show()

# Function to plot scatter plot
def plot_scatter():
    x = np.random.rand(100)
    y = np.random.rand(100)
    plt.scatter(x, y, color='purple')
    plt.title("Scatter Plot")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.show()

# Function to plot pie chart
def plot_pie_chart():
    emotions = list(emotion_to_playlist.keys())
    emotion_counts = np.random.randint(1, 100, size=len(emotions))  # Simulated counts
    plt.pie(emotion_counts, labels=emotions, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set3", len(emotions)))
    plt.title("Emotion Distribution")
    plt.show()

# Function to plot barplot
def plot_barplot():
    emotions = list(emotion_to_playlist.keys())
    emotion_counts = np.random.randint(1, 100, size=len(emotions))  # Simulated counts
    sns.barplot(x=emotions, y=emotion_counts, palette='Blues_d')
    plt.title("Emotion Count Barplot")
    plt.xlabel("Emotions")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.show()

# Function to plot boxplot
def plot_boxplot():
    emotions = list(emotion_to_playlist.keys())
    emotion_data = np.random.rand(len(emotions), 100)  # Simulated data
    sns.boxplot(data=emotion_data.T, orient="h")
    plt.title("Boxplot of Emotions")
    plt.yticks(ticks=np.arange(len(emotions)), labels=emotions)
    plt.show()

# Function to plot histogram
def plot_histogram():
    data = np.random.rand(100)
    plt.hist(data, bins=20, color='purple', edgecolor='black')
    plt.title("Histogram")
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.show()

# Function to plot pairplot
def plot_pairplot():
    emotions = list(emotion_to_playlist.keys())
    emotion_data = np.random.rand(len(emotions), 100)  # Simulated data
    df = pd.DataFrame(emotion_data.T, columns=emotions)
    sns.pairplot(df)
    plt.title("Pairplot of Emotions")
    plt.show()

# Function to detect emotion
def start_emotion_detection():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Error", "Unable to access the webcam.")
        return

    messagebox.showinfo("Info", "Look into the camera and express yourself freely!")
    while True:
        ret, frame = cap.read()
        if not ret:
            messagebox.showerror("Error", "Failed to capture frame.")
            break

        try:
            # Detect emotion
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            emotion = result['dominant_emotion'] if isinstance(result, dict) else result[0]['dominant_emotion']

            # Display detected emotion
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Your mood has been detected", f"Your emotion: {emotion}")

            # Open playlist based on detected emotion
            playlist = emotion_to_playlist.get(emotion, None)
            if playlist:
                webbrowser.open(playlist)
            else:
                messagebox.showinfo("Info", "No playlist available for this emotion.")
            break
        except Exception as e:
            messagebox.showerror("Error", f"Emotion detection failed: {e}")
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# GUI setup
root = tk.Tk()
root.title("Playlist for Your Mood")
root.geometry("500x500")
root.configure(bg="#F5F5F5")

# GUI Components
label = tk.Label(root, text="AURA TUNES: AI MOOD MELODIES", font=("Arial", 18), fg="indigo", bg="#F5F5F5")
label.pack(pady=20)

instruction_label = tk.Label(root, text="Click the button below to detect your mood\nand explore related tracks!", font=("Arial", 12))
instruction_label.pack(pady=10)

detect_button = tk.Button(root, text="DETECT MY MOOD!!", font=("Arial", 14), bg="purple", fg="white", command=start_emotion_detection)
detect_button.pack(pady=20)

quit_button = tk.Button(root, text="QUIT", font=("Arial", 14), bg="#FF1493", fg="white", command=root.quit)
quit_button.pack(pady=10)

# Automatically display the plots
plot_confusion_matrix()
plt.savefig('plot.jpg')  # Saves as plot.jpg

plot_roc_curve()
plot_regression()
plot_scatter()
plot_pie_chart()
plot_barplot()
plot_boxplot()
plot_histogram()
plot_pairplot()
