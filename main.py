import tkinter as tk
from tkinter import messagebox
from visualization import plot_all_visualizations
from mood_detection import start_emotion_detection

def open_visualization():
    try:
        plot_all_visualizations()
    except Exception as e:
        messagebox.showerror("Error", f"Visualization failed: {e}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Mood-Based Application")
root.geometry("500x400")
root.configure(bg="#F5F5F5")

# Add a title label
label = tk.Label(root, text="Mood Analysis and Visualization", font=("Arial", 18), fg="indigo", bg="#F5F5F5")
label.pack(pady=20)

# Add buttons for functionalities
detect_button = tk.Button(root, text="Detect My Mood", font=("Arial", 14), bg="purple", fg="white", command=start_emotion_detection)
detect_button.pack(pady=20)

visualize_button = tk.Button(root, text="View Visualizations", font=("Arial", 14), bg="blue", fg="white", command=open_visualization)
visualize_button.pack(pady=20)

quit_button = tk.Button(root, text="Quit", font=("Arial", 14), bg="#FF1493", fg="white", command=root.quit)
quit_button.pack(pady=10)

# Run the application
root.mainloop()
