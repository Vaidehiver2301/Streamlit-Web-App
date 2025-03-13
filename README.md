# Streamlit Web App - Data Analysis Tool

Welcome to the **Streamlit Web App** repository! This application is designed to help you perform basic data analysis tasks directly in your web browser using Python and Streamlit. The app allows you to upload a dataset in CSV format and provides various features to explore and analyze the data.

---

## Key Features

1. **Upload Your Dataset**  
   - Upload your dataset in CSV format directly through the app interface.

2. **Preview Dataset**  
   - View the first few rows (`head`) or the last few rows (`tail`) of your dataset.

3. **Check Data Types**  
   - Display the data types of each column in the dataset.

4. **Dataset Shape**  
   - Check the number of rows and columns in your dataset.

5. **Null Values Detection**  
   - Identify null values in the dataset with a heatmap visualization.

6. **Duplicate Values Detection**  
   - Detect and remove duplicate values from the dataset.

7. **Summary Statistics**  
   - View overall statistics (e.g., count, mean, min, max, etc.) for the dataset.

8. **About Section**  
   - Learn more about the app, the libraries used, and the developer.

---

## How to Use

1. **Upload Your Dataset**  
   - Click on the "Upload Your File in CSV format" button to upload your dataset.

2. **Explore the Dataset**  
   - Use the checkboxes and buttons to preview the dataset, check data types, and view the shape of the dataset.

3. **Analyze the Dataset**  
   - Detect null values, remove duplicates, and view summary statistics using the provided options.

4. **About the App**  
   - Click the "About" button to learn more about the app and its developer.

---

## Libraries Used

- **Streamlit**: For building the web app interface.
- **Pandas**: For data manipulation and analysis.
- **Seaborn**: For data visualization (heatmap).
- **Matplotlib**: For creating plots and visualizations.

---

## Installation and Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Streamlit-Web-App.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Streamlit-Web-App
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

5. Open your web browser and navigate to the provided local URL (usually `http://localhost:8501`).

---

## Try the App Online

You can try the app directly without any setup by visiting the following link:  
👉 [**Streamlit Web App - Data Analysis Tool**](https://data-analys-is.streamlit.app/)

---

## Example Usage

1. Upload a CSV file (e.g., `example.csv`).
2. Click "Preview DataSet" and choose "Head" or "Tail" to view the first or last few rows.
3. Use the "Data Types" checkbox to view column data types.
4. Check the shape of the dataset by selecting "rows" or "columns".
5. Detect null values using the "Null Values" button.
6. Remove duplicate values if any are found.
7. View summary statistics by clicking the "Summary" button.

---

## About the Developer

This app was built by **Vaidehi Verma** using Streamlit, Pandas, Seaborn, and Matplotlib. Feel free to contribute to the project or reach out with any questions or suggestions!

---

Enjoy exploring your data with the **Streamlit Web App**!  🚀
