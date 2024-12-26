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
    plt.ylabel('True Positive Rate'
