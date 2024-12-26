# AuraTunes: Emotion-Based Music Recommender

AuraTunes is an AI-powered music recommendation system that detects your emotions in real-time and suggests personalized Spotify playlists. It uses facial emotion recognition to analyze your mood and provides curated playlists and visual insights based on emotional analysis in music.

---

## Features

- **Emotion Detection**: Uses DeepFace to recognize dominant emotions like happy, sad, angry, surprise, fear, and neutral.
- **Spotify Integration**: Maps detected emotions to mood-specific Spotify playlists.
- **Visualizations**: Includes plots for confusion matrix, ROC curve, scatter plots, pie charts, and more.
- **Interactive GUI**: Built with Tkinter for user-friendly interaction.
- **Real-Time Camera Access**: Captures facial expressions via webcam.

---

## Installation

### Prerequisites

- Python 3.7+
- Required libraries (install via `requirements.txt`)
- A webcam for emotion detection

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/Juhikothari/AuraTunes.git
   cd AuraTunes
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Download the DEAM dataset:

   - Download from [Kaggle](https://www.kaggle.com/datasets/diogofernan/DEAM and save the files in the `datasets/` folder.

4. Run the application:

   ```bash
   python main.py
   ```

---

## Usage

### Emotion-Based Spotify Playlist Recommendation

1. Launch the application by running `main.py`.
2. Click on the **"DETECT MY MOOD!!"** button.
3. Look at the webcam, and the app will analyze your emotion.
4. Your detected emotion will:
   - Open a related Spotify playlist.
   - Display your detected mood in the GUI.
5. To exit the application, click the **"QUIT"** button.

### Visualization Plots

1. Run the visualization script (`visualization.py`) to generate the following plots:
   - Confusion Matrix
   - ROC Curve
   - Regression and Scatter Plots
   - Pie Chart, Barplot, Boxplot, and Histogram
   - Pairplot for emotion distribution
2. Plots are displayed automatically and saved as images in the `results/` folder.

---

## Dataset

### DEAM Dataset

- Used for emotional analysis in music.
- Contains annotations of arousal and valence for music tracks.
- Download from [Kaggle](https://www.kaggle.com/datasets/diogofernan/DEAM.

### GoEmotions Dataset

- Used for emotional word mapping.
- Contains emotion annotations for text.
- Download from [Kaggle]https://www.kaggle.com/datasets/google/goemotions
).

---

## Files and Directory Structure

```
AuraTunes/
│
├── main.py                  # Main application script (Spotify recommendation and GUI)
├── visualization.py        # Script to generate all visualizations
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── LICENSE                 # License file
├── .gitignore              # Ignored files
│
├── datasets/               # Folder for datasets
│   ├── deam_dataset.csv    # DEAM dataset for analysis
│   ├── emotion_words.csv   # GoEmotions dataset
│   └── other_emotion_data.csv
│
├── models/                 # Pre-trained models
│   └── deepface_model.h5
│
├── results/                # Outputs and visualizations
│   ├── confusion_matrix.png
│   ├── roc_curve.png
│   ├── scatter_plot.png
│   ├── pie_chart.png
│   └── barplot.png
│
└── download_data.py        # Script to download datasets
```

---

## Technologies Used

- **Python**: Main programming language
- **DeepFace**: For emotion detection
- **OpenCV**: Real-time image capture and processing
- **Tkinter**: GUI development
- **Matplotlib & Seaborn**: Data visualization (e.g., arousal-valence plots, confusion matrix, etc.)

---

## Example Output

### GUI Screenshot

1. **Emotion-Based Playlist Recommendation**:
   - ![image](https://github.com/user-attachments/assets/68c855f5-f927-4b33-8909-583ce20d3345)



### Visualization Examples

2. **Confusion Matrix**: ![Confusion Matrix](results/confusion_matrix.png)

3. **ROC Curve**: ![ROC Curve](results/roc_curve.png)

4. **Barplot**: ![Barplot](results/barplot.png)

---

## Future Enhancements

- Add support for audio input for emotion detection.
- Improve model accuracy with fine-tuned datasets.
- Expand to other music platforms (e.g., YouTube, Apple Music).
- Implement a feedback mechanism for better recommendations.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [DEAM Dataset]((https://www.kaggle.com/datasets/diogofernan/DEAM)) for providing emotional annotations in music.
- [GoEmotions Dataset](https://www.kaggle.com/datasets/google/goemotions) for emotion annotations in text.
- [DeepFace](https://github.com/serengil/deepface) for facial emotion detection.
- Inspiration from emotion-based music recommendation research.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## Contact

For queries or suggestions, please contact:

- Name: [JUHI KOTHARI]
- Email: [juhikthr@gmail.com]
- GitHub: (https://github.com/Juhikothari)

