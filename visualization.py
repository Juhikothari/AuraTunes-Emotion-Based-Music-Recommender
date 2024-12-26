### 1. **Confusion Matrix Plot**
   A confusion matrix helps visualize the performance of a classification model by showing the actual vs predicted labels.

   ```python
   from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
   import matplotlib.pyplot as plt

   def plot_confusion_matrix(y_true, y_pred, labels):
       cm = confusion_matrix(y_true, y_pred, labels=labels)
       disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
       disp.plot(cmap=plt.cm.Blues)
       plt.title("Confusion Matrix")
       plt.show()
   ```

### 2. **ROC Curve Plot**
   The ROC (Receiver Operating Characteristic) curve is useful for evaluating classification models, especially in the case of binary classification or multi-class problems.

   ```python
   from sklearn.metrics import roc_curve, auc
   import matplotlib.pyplot as plt

   def plot_roc_curve(y_true, y_score, labels):
       fpr = {}
       tpr = {}
       roc_auc = {}

       for i, label in enumerate(labels):
           fpr[label], tpr[label], _ = roc_curve(y_true[:, i], y_score[:, i])
           roc_auc[label] = auc(fpr[label], tpr[label])

       for label in labels:
           plt.plot(fpr[label], tpr[label], label=f'{label} (AUC = {roc_auc[label]:.2f})')

       plt.plot([0, 1], [0, 1], 'k--', lw=2)
       plt.xlabel('False Positive Rate')
       plt.ylabel('True Positive Rate')
       plt.title('ROC Curve')
       plt.legend(loc='lower right')
       plt.show()
   ```

### 3. **Bar Plot for Emotion Distribution**
   A bar plot helps visualize the distribution of different emotions.

   ```python
   import seaborn as sns
   import matplotlib.pyplot as plt

   def plot_emotion_distribution(emotions, counts):
       sns.barplot(x=emotions, y=counts, palette='viridis')
       plt.title("Emotion Distribution")
       plt.xlabel("Emotions")
       plt.ylabel("Count")
       plt.xticks(rotation=45)
       plt.show()
   ```

### 4. **Pie Chart for Emotion Proportions**
   This plot shows the proportion of different emotions as a pie chart.

   ```python
   import matplotlib.pyplot as plt
   import seaborn as sns

   def plot_pie_chart(emotions, counts):
       plt.pie(counts, labels=emotions, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set3", len(emotions)))
       plt.title("Emotion Proportions")
       plt.show()
   ```

### 5. **Scatter Plot**
   A scatter plot visualizes the relationship between two variables, such as emotion scores and text features.

   ```python
   import matplotlib.pyplot as plt

   def plot_scatter(x, y):
       plt.scatter(x, y, color='purple')
       plt.title("Emotion vs Text Feature")
       plt.xlabel("Emotion Score")
       plt.ylabel("Text Feature")
       plt.show()
   ```

### 6. **Regression Plot**
   Regression plots are used to visualize the relationship between two continuous variables.

   ```python
   import seaborn as sns
   import matplotlib.pyplot as plt

   def plot_regression(x, y):
       sns.regplot(x=x, y=y)
       plt.title("Regression Plot")
       plt.xlabel("Emotion Score")
       plt.ylabel("Other Feature")
       plt.show()
   ```

### 7. **Main Block for Visualizing Data (Optional)**
   You can include some simulated or real data inside a `__main__` block, which would allow you to test the functions directly.

   ```python
   if __name__ == "__main__":
       emotions = ['happy', 'sad', 'angry', 'surprise', 'fear', 'neutral']
       emotion_counts = [50, 30, 15, 10, 25, 20]  # Example simulated counts

       # Example for confusion matrix and ROC curve plotting
       y_true = np.random.choice(emotions, 100)  # Simulated ground truth
       y_pred = np.random.choice(emotions, 100)  # Simulated predictions
       y_true_bin = np.random.randint(0, 2, (100, len(emotions)))  # Simulated binary true labels
       y_score = np.random.rand(100, len(emotions))  # Simulated prediction scores

       plot_confusion_matrix(y_true, y_pred, emotions)
       plot_roc_curve(y_true_bin, y_score, emotions)
       plot_emotion_distribution(emotions, emotion_counts)
       plot_pie_chart(emotions, emotion_counts)
       plot_scatter(np.random.rand(100), np.random.rand(100))
       plot_regression(np.random.rand(100), np.random.rand(100))
   ```

IMAGES:


