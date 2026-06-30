# Personal Finance Tracker

A simple, interactive expense tracker built with **Streamlit** to help users record transactions, monitor monthly spending, and visualize spending patterns. This project was developed to gain hands-on experience with Streamlit by implementing session state, forms, sidebar filters, interactive charts, tabs, and file persistence.

---

## Features

### Dashboard

The dashboard provides an overview of your finances through:

* Total amount spent
* Remaining monthly budget
* Total number of transactions
* Spending by category (Bar Chart)
* Category distribution (Donut Chart)
* Spending over time (Line Chart)

### Add Transactions

Users can add new expense records by entering:

* Date
* Category
* Description
* Amount

The application validates all inputs before saving the transaction.

### Transaction History

The history page allows users to:

* View all recorded transactions
* Filter transactions by category
* Export transaction history as a CSV file
* Reset all stored transactions with a single click

### Sidebar Controls

The sidebar provides options to:

* Set a monthly budget
* Filter transactions by category

These filters are applied throughout the application.

### Data Persistence

All transactions are stored in a local CSV file, ensuring data remains available even after refreshing or restarting the application.

---

## Tech Stack

| Technology     | Purpose                               |
| -------------- | ------------------------------------- |
| Streamlit      | Interactive web application framework |
| Pandas         | Data manipulation and analysis        |
| Plotly Express | Interactive charts and visualizations |

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/finance-tracker-streamlit.git
cd finance-tracker-streamlit
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run main.py
```

The application will open automatically in your browser at:

```
http://localhost:8501
```

---

## Project Structure

```text
finance-tracker-streamlit/
│
├── main.py                 # Main Streamlit application
├── requirements.txt        # Python dependencies
├── transactions.csv        # Stores transaction data (created automatically)
├── .gitignore              # Excludes cache files and personal data
└── README.md               # Project documentation
```

---

## Streamlit Concepts Covered

| Feature                                           | Purpose                                             |
| ------------------------------------------------- | --------------------------------------------------- |
| `st.session_state`                                | Persist transaction data across reruns              |
| `st.tabs`                                         | Navigate between Dashboard, Entry Form, and History |
| `st.sidebar`                                      | Budget settings and category filters                |
| `st.form`                                         | Group user inputs and avoid unnecessary reruns      |
| `st.metric`                                       | Display key financial metrics                       |
| `st.columns`                                      | Create responsive layouts                           |
| `st.plotly_chart`                                 | Display interactive charts                          |
| `st.dataframe`                                    | Display transaction history                         |
| `st.download_button`                              | Export data as CSV                                  |
| `st.expander`                                     | Display raw transaction data                        |
| `st.success`, `st.warning`, `st.error`, `st.info` | Provide user feedback                               |

---

## Future Improvements

Planned enhancements include:

* Multi-user authentication
* Database integration using SQLite or PostgreSQL
* Recurring transactions
* Custom date-range filtering
* Multiple currency support
* Improved analytics and financial insights
* Mobile-responsive layout

---

## Learning Outcomes

This project demonstrates practical experience with:

* Building interactive applications using Streamlit
* Managing application state with `st.session_state`
* Working with forms and user input validation
* Data visualization using Plotly Express
* Data manipulation using Pandas
* CSV-based data persistence
* Interactive filtering and data export functionality

---

## License

This project is intended for educational and portfolio purposes. You are welcome to fork, modify, and extend it for your own learning.
