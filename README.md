# 🧠 Customer Segmentation Dashboard (Streamlit App)

This project is a **Machine Learning–based Customer Segmentation Dashboard** built using **K-Means Clustering**.  
It helps businesses identify distinct customer groups based on demographics and spending behavior, enabling targeted marketing and strategy decisions.

---

## 🚀 Features

✅ Upload your own CSV dataset  
✅ Automatic null value handling (no crashes!)  
✅ Data preprocessing and standardization  
✅ K-Means clustering with visualization  
✅ Interactive dashboards built with Streamlit  
✅ Downloadable clean data and cluster results  

---

## 🧩 Tech Stack

- **Language:** Python 3.11  
- **Framework:** Streamlit  
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Plotly  

---

## 🗂️ Folder Structure

customer_segmentation_project/
│
├── app.py # Main Streamlit app
├── requirements.txt # Dependencies
├── data/
│ └── Mall_Customers.csv # Sample dataset
├── venv/ # Virtual environment (optional)
└── README.md # Project documentation


## ⚙️ Setup Instructions

### 1️⃣ Create and activate virtual environment
```bash
py -3.11 -m venv venv
.\venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py



📊 Usage

Upload your dataset (.csv) containing customer data.

The app automatically:

Cleans null values

Performs K-Means clustering

Visualizes cluster distribution and centers

View customer insights and download the clustered dataset.

🧹 Handling Missing Values

The app automatically replaces:

Numeric nulls → Median

Categorical nulls → Mode

No more crashes due to incomplete data! 🚫

🧠 Example Output

📊 Cluster Distribution (Bar Chart)
🎨 2D PCA Scatter Plot (optional enhancement)
📋 Cluster Centers (Table)
⬇️ Download button for segmented data

💡 Future Improvements

Add PCA-based visualizations

Integrate customer profiling summary per cluster

Deploy on Streamlit Cloud or Hugging Face Spaces

👨‍💻 Author

Ahtasham Anjum
📧 ahtashamd321@gmail.com
🔗 (https://github.com/ahtashamd321)
![LinkedIn] (https://www.linkedin.com/in/ahtasham-anjum/)
