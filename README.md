# 🧠 Customer Segmentation Dashboard (Streamlit App)

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)
![MachineLearning](https://img.shields.io/badge/ML-KMeans-yellow?logo=scikitlearn&logoColor=white)

---

## 🎯 Overview
This project is a **Machine Learning–powered Customer Segmentation Dashboard** built using **K-Means Clustering**.  
It enables businesses to identify unique customer groups based on demographics and spending behavior, helping them make **data-driven marketing and business decisions**.

---

## 🚀 Features
- ✅ Upload your own **CSV dataset**
- ✅ Automatic **data cleaning & null handling**
- ✅ **K-Means clustering** for customer segmentation
- ✅ Beautiful **visualizations** with Matplotlib & Plotly
- ✅ Interactive **Streamlit dashboard**
- ✅ Downloadable **cleaned and clustered dataset**

---

## 🧩 Tech Stack

| Category | Tools |
|-----------|--------|
| **Language** | Python 3.11 |
| **Framework** | Streamlit |
| **Libraries** | Pandas, NumPy, Scikit-learn, Matplotlib, Plotly, Seaborn |
| **ML Algorithm** | K-Means Clustering |

---

## 🗂️ Folder Structure
customer_segmentation_project/
│
├── app.py # Main Streamlit app
├── requirements.txt # Project dependencies
├── data/
│ └── Mall_Customers.csv # Sample dataset
├── venv/ # Virtual environment (optional)
└── README.md # Project documentation




## ⚙️ Setup Instructions

### 1️⃣ Create and activate a virtual environment
```bash
py -3.11 -m venv venv
.\venv\Scripts\activate
2️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Run the app
bash
Copy code
streamlit run app.py
Then open your browser at 👉 http://localhost:8501


📊 Usage Guide
Upload your dataset (.csv) containing customer data.
The app automatically:

Cleans null values

Performs K-Means clustering

Visualizes cluster distribution and centers

Displays interactive dashboards

Lets you download the clustered dataset

🧹 Handling Missing Values
The app automatically handles missing values:

Numeric columns → Median

Categorical columns → Mode

✅ No crashes or incomplete data issues — everything handled automatically!


🧠 Example Output
📊 Cluster Distribution (Bar Chart)
🎨 PCA Scatter Plot (optional enhancement)
📋 Cluster Centers (Table)


⬇️ Download button for segmented data

💡 Future Improvements
🚀 Add PCA-based visualization
🧭 Generate automatic cluster profiling summaries
☁️ Deploy on Streamlit Cloud / Hugging Face Spaces
📱 Add responsive layout for mobile users

👨‍💻 Author
Ahtasham Anjum
📧 [Email] (ahtashamd321@gmail.com)
🔗 [GitHub] (https:/github.com/ahtashamd321)
🔗 [LinkedIn] (https:/linkedin.com/in/ahtasham-anjum)


🌟 Show Your Support
If you found this project helpful:

⭐ Star the repo on GitHub
🤝 Connect with me on LinkedIn
💬 Share feedback or suggest improvements
