# Synthetic Data Generation using CTGAN

A Flask-based web application for generating realistic synthetic datasets using Conditional Tabular GANs (CTGAN). This project was developed for the PWC Cyber Hackathon 2024: Fiercest Competitor 3.0 to address the challenge of creating privacy-compliant test data for financial institutions.

## 🌟 Features

- Generate synthetic data for two types of datasets:
  - Employee Dataset (personal information)
  - PCI Dataset (payment card information)
- Multiple output formats supported:
  - CSV
  - Excel
  - JSON
  - Doc
- Dynamic data generation (1,000 to 10,000 records)
- Secure user authentication system
- Privacy-compliant synthetic data generation
- Luhn algorithm validation for credit card numbers
- Responsive Vue.js frontend interface

## 🛠️ Technology Stack

### Backend
- Flask - Web framework
- Flask-RESTful - REST API implementation
- SQLAlchemy - Database ORM
- Flask-Security - Authentication and authorization
- SDV (Synthetic Data Vault) - Synthetic data generation
- CTGAN - Deep learning model for synthetic data

### Frontend
- Vue.js 2.7
- Vue Router
- Bootstrap 5
- Custom CSS

### Database
- SQLite
- Redis (for caching)

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/SaiSatya16/Synthetic-Data-Generation-using-CTGAN
cd Synthetic-Data-Generation-using-CTGAN
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
python upload_initial_data.py
```

5. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 💻 Usage

1. Log in to the application using your credentials
2. Select the dataset type (Employee or PCI)
3. Choose the desired output format
4. Specify the number of records (1,000-10,000)
5. Click "Generate and Download Data"

## 📁 Project Structure

```bash
synthetic-data-generator/
├── app.py                 # Main application file
├── api.py                 # API endpoints and data generation logic
├── config.py             # Configuration settings
├── model.py              # Database models
├── sec.py                # Security configurations
├── static/               # Static files
│   ├── style.css
│   └── vue/             # Vue.js components
├── templates/            # HTML templates
│   └── index.html
└── content/             # Data storage
```

## 🔒 Security Features

- Token-based authentication
- Password hashing
- Role-based access control
- Session management
- CSRF protection
- Inactivity timeout (30 minutes)

## ⚙️ Data Generation Details

### Employee Dataset Fields
- Name
- User ID
- Email
- SSN
- Blood group
- Gender
- Address
- Date of birth
- U.S. Driver License Number

### PCI Dataset Fields
- Card holder name
- Security code/CVV
- Expiration date
- Credit Card number
- Card provider


## 🏆 Acknowledgments

This project was developed as part of the PWC Cyber Hackathon 2024: Fiercest Competitor 3.0 challenge.