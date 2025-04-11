# 🎬 GenieCue — Movie Recommendation App

GenieCue is a **modern, ML-powered movie recommendation system** built with **Streamlit** that helps users discover movies similar to their favorites in a sleek, interactive interface. Whether you're into thrillers, rom-coms, or indie gems, GenieCue has a recommendation for you!

![GenieCue Demo](assets/geniecue-demo.gif) <!-- Replace with your actual screenshot or gif path -->

---

## 🚀 Live Demo

👉 [Try it now on Streamlit Cloud](https://geniecue.streamlit.app)  
*(Replace with your actual link once deployed)*

---

## 📌 Features

- 🔍 **Search & Recommend:** Instantly get top 5 movie recommendations based on your selection.
- 🧠 **ML-Driven:** Uses NLP and cosine similarity to compute recommendations.
- 🎨 **Modern UI:** Built with Streamlit for an intuitive and clean user interface.
- ⚡ **Fast Performance:** Loads data from preprocessed pickle files for instant results.
- 🌐 **Deployable Anywhere:** Streamlit allows for one-click cloud deployment.

---

## 🛠️ Tech Stack

| Layer        | Technology                           |
|--------------|---------------------------------------|
| Frontend     | [Streamlit](https://streamlit.io)     |
| Backend      | Python, `pickle`, Pandas, scikit-learn|
| ML Model     | TF-IDF + Cosine Similarity            |
| Deployment   | Streamlit Cloud / Local Host          |

---

## 🧠 How It Works

1. The dataset is processed to extract relevant movie features like genres, overview, keywords, cast, etc.
2. A **TF-IDF Vectorizer** is used to convert the text features into numerical vectors.
3. **Cosine similarity** is calculated between all movie vectors to determine similarity.
4. When a user selects a movie, the top 5 most similar ones are recommended.

The entire model logic is available in the [`MovieRecommendation.ipynb`](MovieRecommendation.ipynb) file.

---

## 📁 Project Structure

GenieCue/ ├── app.py # Streamlit frontend ├── MovieRecommendation.ipynb # Model development and training ├── similarity.pkl # Precomputed similarity matrix ├── movie_dict.pkl # Preprocessed movie dataset ├── assets/ │ └── geniecue-demo.gif # Demo animation or screenshot ├── requirements.txt # Python dependencies └── README.md # You're here!


---

## 📦 Installation & Local Setup

> Run the app locally on your machine with the following steps:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/geniecue.git
cd geniecue
```
2. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Launch the App
```bash
streamlit run app.py
```

☁️ Deployment on Streamlit Cloud
To deploy GenieCue publicly:

Push your code to GitHub

Go to Streamlit Cloud

Click "New App"

Select your GitHub repo, branch, and point to app.py

Click "Deploy" 🎉

💡 Future Improvements
🎯 Add filters for genre, language, release year

🧩 Incorporate collaborative filtering for hybrid recommendations

📱 Make layout responsive for mobile

🌐 Use TMDB API for live data fetching

📊 Add popularity or rating scores to recommendations

🤝 Contributing
Contributions are welcome!

Fork the repository

Create your feature branch: git checkout -b feature/YourFeature

Commit your changes: git commit -m "Add YourFeature"

Push to the branch: git push origin feature/YourFeature

Open a pull request

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙌 Acknowledgements
Streamlit for building fast, shareable Python apps

Kaggle & TMDB for movie datasets

Scikit-learn for ML utilities

OpenAI ChatGPT for development assistance

💬 Feedback & Contact
Have feedback or suggestions?
Reach out via LinkedIn or open an Issue.

Made with ❤️ by Soumya


---

Let me know if you'd like a matching `LICENSE` file or if you'd like help creating a deployment link or a `demo.gif`.
