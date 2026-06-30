Personal Finance Tracker
A simple, interactive expense tracker built with Streamlit to log transactions, visualize spending by category, and monitor a monthly budget.
Built as a hands-on project to learn core Streamlit concepts: session state, forms, tabs, sidebar filters, charts, and file persistence.

Features

Dashboard — KPI cards (total spent, budget left, transaction count), bar chart, donut chart, and spending-over-time line chart
Entry Form — Add transactions with date, category, description, and amount, with input validation
History — Filterable transaction table, CSV export, and a one-click reset
Sidebar Filters — Filter the entire app by category and set a custom monthly budget
Persistence — Transactions are saved to a local CSV file, so data survives a page refresh


Tech Stack

Streamlit — UI framework
Pandas — data handling
Plotly Express — interactive charts


Getting Started
1. Clone the repo
git clone https://github.com/YOUR_USERNAME/finance-tracker-streamlit.git
cd finance-tracker-streamlit
2. Install dependencies
pip install -r requirements.txt
3. Run the app
streamlit run main.py
The app will open automatically at http://localhost:8501

Project Structure
finance-tracker-streamlit/
├── main.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .gitignore           # Excludes cache files and personal transaction data
└── readme.md

Streamlit Concepts Covered
ConceptUsed Forst.session_statePersisting transaction data across rerunsst.tabsDashboard / Entry Form / History navigationst.sidebarCategory filters and budget inputst.formGrouping form inputs to avoid reruns on every keystrokest.metricKPI cardsst.columnsSide-by-side layoutst.plotly_chartBar, donut, and line chartsst.dataframeInteractive transaction tablest.download_buttonCSV exportst.expanderCollapsible raw data viewst.success / st.warning / st.error / st.infoUser feedback

Future Improvements

Multi-user support with authentication
Switch from CSV storage to a proper database (SQLite/Postgres)
Recurring transactions
Custom date-range filtering
Currency selector