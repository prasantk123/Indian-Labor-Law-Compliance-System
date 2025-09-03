# Indian Labor Law Compliance System

A comprehensive web application for calculating statutory benefits and checking compliance requirements as per Indian labor laws.

## Features

### Phase 1: Core Calculators ✅
- **Gratuity Calculator**: Calculate gratuity as per Payment of Gratuity Act, 1972
- **PF Calculator**: Calculate Provident Fund contributions for employees and employers
- **ESI Calculator**: Check ESI eligibility and calculate contributions
- **Leave Calculator**: Calculate leave entitlements as per Factories Act and state laws
- **Compliance Checker**: Generate personalized compliance checklists

### Phase 2: Web Application ✅
- Clean, responsive web interface using Bootstrap
- Individual calculators with form inputs and result displays
- API endpoints for programmatic access
- Interactive compliance checklist with download functionality

## Installation & Setup

1. **Clone or download the project**
   ```bash
   cd c:\Users\prasa\Documents\project\law
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Open your browser and go to: `http://localhost:5000`

## Usage

### Gratuity Calculator
- Enter last drawn salary (Basic + DA) and years of service
- Minimum 5 years required for eligibility
- Maximum gratuity capped at ₹20,00,000

### PF Calculator
- Enter basic salary and dearness allowance
- Calculates employee and employer contributions
- Shows EPF and EPS breakdown

### ESI Calculator
- Enter monthly salary to check eligibility
- ESI applicable for salaries up to ₹21,000/month
- Shows employee (0.75%) and employer (3.25%) contributions

### Leave Calculator
- Enter days worked in year, state, and establishment type
- Calculates earned leave, casual leave, and sick leave
- Based on Factories Act and state-specific rules

### Compliance Checker
- Select state, number of employees, and industry type
- Generates personalized compliance checklist
- Download checklist as text file

## API Endpoints

All calculators are also available via REST API:

```bash
POST /api/calculate
Content-Type: application/json

# Gratuity calculation
{
  "type": "gratuity",
  "salary": 50000,
  "years": 6
}

# PF calculation
{
  "type": "pf",
  "basic": 25000,
  "da": 5000
}

# ESI calculation
{
  "type": "esi",
  "salary": 18000,
  "state": "general"
}

# Leave calculation
{
  "type": "leave",
  "days_worked": 300,
  "state": "maharashtra",
  "establishment_type": "factory"
}

# Compliance checklist
{
  "type": "compliance",
  "state": "Maharashtra",
  "num_employees": 25,
  "industry_type": "Factory"
}
```

## Legal Formulas & Rules

### Gratuity
- **Formula**: (Last Drawn Salary ÷ 26) × 15 × Years of Service
- **Eligibility**: Minimum 5 years of continuous service
- **Maximum**: ₹20,00,000 (as per 2018 amendment)

### Provident Fund
- **Calculation Base**: Basic + DA, capped at ₹15,000
- **Employee Contribution**: 12% to EPF
- **Employer Contribution**: 12% (8.33% to EPS + 3.67% to EPF)

### ESI
- **Wage Limit**: ₹21,000 per month
- **Employee Rate**: 0.75%
- **Employer Rate**: 3.25%

### Leave Entitlement
- **Earned Leave**: 1 day per 20 days worked (Factories Act)
- **Casual Leave**: 7-12 days per year (varies by establishment)
- **Sick Leave**: 7-12 days per year (varies by establishment)

## Testing

Run the test suite to verify calculations:

```bash
python core_calculators.py
```

## File Structure

```
law/
├── app.py                 # Flask web application
├── core_calculators.py    # Core calculation functions
├── pdf_generator.py       # PDF report generation
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── run_app.bat           # Easy startup script
├── test_app.py           # Application tests
└── templates/            # HTML templates
    ├── base.html         # Base template
    ├── index.html        # Home page
    ├── gratuity.html     # Gratuity calculator
    ├── pf.html           # PF calculator
    ├── esi.html          # ESI calculator
    ├── leave.html        # Leave calculator
    └── compliance.html   # Compliance checker
```

## Features Added ✅

- [x] **PDF Report Generation**: Professional PDF reports for all calculations
- [x] **Download Functionality**: Export reports as PDF with company branding
- [x] **Professional Layout**: Clean, formatted reports with tables and styling

## Future Enhancements (Phase 3 & 4)

- [ ] Database integration for storing calculations
- [ ] User authentication and saved calculations
- [ ] Advanced compliance tracking with deadlines
- [ ] Integration with government APIs
- [ ] Mobile app version
- [ ] Multi-language support
- [ ] Email notifications for compliance deadlines

## Disclaimer

This application provides calculations based on general Indian labor law provisions. Specific requirements may vary by state, industry, and establishment size. Always consult with legal experts for complete compliance guidance.

## License

This project is for educational and informational purposes. Please ensure compliance with local laws and regulations.