import tkinter as tk
from tkinter import messagebox
import cv2
from deepface import DeepFace
import webbrowser

# Define emotion-to-playlist mapping
emotion_to_playlist = {
    "happy": "https://open.spotify.com/playlist/5ACAHVlMPRrgnnZ8temmIh?si=LlvE8RZfS92RY-fUbqAX_g",
    "sad": "https://open.spotify.com/playlist/0RkK2ZAXWD5HEmCJZ00i1G?si=Aa_r-9rwSZuxa1ji7z51Jw",
    "angry": "https://open.spotify.com/playlist/5cwtgqs4L1fX8IKoQebfjJ?si=E4KoOSw1T3ShHyIhV4CabA",
    "surprise": "https://open.spotify.com/playlist/7vatYrf39uVaZ8G2cVtEik?si=mxgDHP14RSCGMsNSLbwTNA",
    "fear": "https://open.spotify.com/playlist/37i9dQZF1DXdpQPPZq3F7n?si=U-J5VJM6QbaWiDP9nExwnA",
    "neutral": "https://open.spotify.com/playlist/4nqbYFYZOCospBb4miwHWy?si=2S0YqR26RJSRrmwKcvsjlQ"
}

def get_playlist_link(emotion):
    return emotion_to_playlist.get(emotion, "https://open.spotify.com/playlist/5ACAHVlMPRrgnnZ8temmIh")  # Default playlist

# Function to start emotion detection
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

            # Display emotion and open playlist
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Your mood has been detected", f"Your emotion: {emotion}")
            playlist = get_playlist_link(emotion)
            webbrowser.open(playlist)
            break
        except Exception as e:
            messagebox.showerror("Error", f"Emotion detection failed: {e}")
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Quit detection with 'q'
            break

    cap.release()
    cv2.destroyAllWindows()

# Create the main Tkinter window
root = tk.Tk()
root.title("Playlist for Your Mood")
root.geometry("400x300")
root.resizable(False, False)

# Set background color
root.configure(bg="#F5F5F5")

# Add a welcome label
label = tk.Label(root, text="AURA TUNES: AI MOOD MELODIES", font=("Arial", 18), fg="indigo", bg="#F5F5F5")
label.pack(pady=20)

# Add an instruction label
instruction_label = tk.Label(root, text="Click the button below to detect your mood\nand make it even better!", font=("Arial", 12))
instruction_label.pack(pady=0)

# Add a button to start emotion detection
detect_button = tk.Button(root, text="DETECT MY MOOD!!", font=("Arial", 14), bg="purple", fg="white", command=start_emotion_detection)
detect_button.pack(pady=20)

# Add a quit button
quit_button = tk.Button(root, text="QUIT", font=("Arial", 14), bg="#FF1493", fg="white", command=root.quit)
quit_button.pack(pady=10)

# Run the application
root.mainloop()
