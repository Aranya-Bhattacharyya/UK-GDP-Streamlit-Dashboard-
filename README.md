# UK GDP Quarterly Growth Dashboard

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

An interactive data dashboard built using **Python, Streamlit, Pandas, and Plotly** to analyse **UK quarterly GDP growth** using official data from the **Office for National Statistics (ONS)**.

The dashboard enables users to explore long-term economic trends, identify recession periods, and interpret GDP movements through interactive visualisations and automated insights.

---

## Live Demo

**Deployed App:** (https://uk-gdpdashboard.streamlit.app/)
*(Note: If the link is not active, please follow the installation instructions below to run locally.)*

---

## Key Features

- **Interactive Time-Range Analysis**: Use the slider to explore GDP trends across specific decades (e.g., 2008 Financial Crisis, COVID-19).
- **Growth Visualisation**: View quarter-on-quarter GDP growth alongside a **4-quarter rolling average** to highlight long-term trends versus short-term volatility.
- **Automated Recession Detection**: The app automatically identifies and shades recession periods.
  - *Definition used:* $\ge 2$ consecutive quarters of negative GDP growth.
- **KPI Metrics**: Real-time calculation of:
  - Latest GDP growth
  - Historical average growth
  - Volatility (Standard Deviation)
- **Auto-generated Insights**:
  - Total number of recession periods detected.
  - Identification of the worst-performing quarter on record.
  - Current economic trend indicators.

---

## Dataset

- **Source**: [Office for National Statistics (ONS)](https://www.ons.gov.uk/)
- **Frequency**: Quarterly
- **Coverage**: 1955 – Present
- **Metric**: UK GDP growth (Quarter-on-Quarter, %)

The dataset is preprocessed within the application to handle ONS metadata, inconsistent date formatting, and time-series conversions.

---

## Tech Stack

| Component | Library | Purpose |
| :--- | :--- | :--- |
| **Core** | `Python` | Main programming language. |
| **Frontend** | `Streamlit` | Interactive web application framework. |
| **Data** | `Pandas` | Data cleaning, manipulation, and time-series analysis. |
| **Viz** | `Plotly` | Interactive charting and recession shading. |

---

## Project Structure

```text
UK-GDP-Dashboard/
├── .streamlit/
│   └── config.toml      # Streamlit UI configuration
├── data/
│   └── uk_gdp_data.csv  # Raw data (or script to fetch via API)
├── src/
│   ├── data_loader.py   # Data cleaning and processing functions
│   ├── plotting.py      # Plotly chart generation logic
├── app.py               # Main application entry point
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## Installation

Follow these steps to set up the project environment and run the dashboard on your local machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/uk-gdp-dashboard.git](https://github.com/your-username/uk-gdp-dashboard.git)
cd uk-gdp-dashboard
```
### 2. Set Up a Virtual Environment (Recommended)

## For MacOS and Linux
```Bash
python3 -m venv venv
source venv/bin/activate
```
## For Windows
```Bash
python -m venv venv
venv\Scripts\activate
```
### 3. Install Dependencies 
```Bash 
pip install -r requirements.txt
```
### Usage
## Running Locally 
  To Launch the dashboard, run the following command in your terminal:
```Bash
streamlit run app.py
```
The application will open in your browser at http://localhost:8501/

### Navigating the Dashboard

- **Sidebar Filters**: Adjust the date range to focus on specific historical events.
- **Interactive Charts**: Hover over data points in the Plotly graph to see specific percentage growth for that quarter.
- **Recession Shading**: Areas shaded in red indicate periods meeting the technical definition of a recession.

### License

Distributed under the MIT License
