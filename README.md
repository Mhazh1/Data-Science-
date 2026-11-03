
# 🛡️ SafeTech Insights
### Sentiment Analysis of Personal Safety Application Reviews
### 🚀 Live Demo

Try the SafeTech Insights sentiment analysis app:

🔗 [Launch SafeTech Insights]([https://safetech-insights.streamlit.app/](https://safetech-insights.streamlit.app/))
## Project Overview
SafeTech Insights is a Natural Language Processing (NLP) and Machine Learning project that analyzes user reviews of personal safety applications.

The project explores user feedback, compares sentiment classification models, and provides an interactive web application built with Streamlit.

## Dataset
- **Source:** [Mendeley Data](https://data.mendeley.com/datasets/9v72t6tv5j/1)
- **Original reviews:** 6,527
- **Reviews after cleaning:** 6,521
- **Applications:** 15

### Sentiment Labeling
Sentiment labels were inferred from user ratings:
- 1–2 stars: Negative
- 3 stars: Neutral
- 4–5 stars: Positive

These are rating-derived labels, not manually annotated text sentiments.

## Methodology
1. Data exploration and cleaning
2. Exploratory Data Analysis (EDA)
3. Sentiment labeling
4. Text feature extraction using TF-IDF
5. Model training and comparison
6. Hyperparameter tuning with GridSearchCV
7. Error analysis
8. Binary sentiment classification
9. Streamlit application development

## Model Comparison

| Model | Accuracy | Macro F1 |
|---|---:|---:|
| Logistic Regression | 77.16% | 62.59% |
| Linear SVM | 83.52% | 66.21% |
| Multinomial Naive Bayes | 83.75% | 59.09% |
| Tuned Linear SVM | 84.14% | 67.57% |

The tuned Linear SVM achieved the highest three-class Macro F1 among the evaluated models.

## Binary Classification
A separate binary classifier was trained after excluding 3-star reviews.

- **Accuracy:** 84.01%
- **Macro F1:** 83.04%

Binary and three-class results are not directly comparable because they use different classification tasks.

## Streamlit Application
The interactive application uses the binary Linear SVM model to classify user-entered reviews as Positive or Negative.

### Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python -m streamlit run app/app.py
```

Open the local URL displayed in the terminal.

## Technologies
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- TF-IDF
- Linear SVM
- GridSearchCV
- Streamlit
- Joblib

## Limitations
- Sentiment labels are derived from star ratings.
- Neutral reviews are difficult to classify reliably.
- The dataset has imbalanced sentiment classes.
- The binary model excludes 3-star reviews.
- Predictions may be unreliable for ambiguous or mixed-sentiment reviews.

## Future Improvements
- Improve neutral sentiment detection
- Explore transformer-based NLP models
- Add application-level feedback analysis
- Expand the Streamlit dashboard

## Project Background
This project extends an interest in AI-based personal safety applications by exploring user feedback through NLP and Machine Learning.
