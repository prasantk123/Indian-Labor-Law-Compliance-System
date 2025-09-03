# Indian Labor Law Compliance System

A comprehensive web application for calculating statutory benefits and checking compliance requirements as per Indian labor laws for both Private and Government sectors.

## Features

### Phase 1: Core Calculators ✅
**Private Sector:**
- **Gratuity Calculator**: Calculate gratuity as per Payment of Gratuity Act, 1972
- **PF Calculator**: Calculate Provident Fund contributions for employees and employers
- **ESI Calculator**: Check ESI eligibility and calculate contributions
- **Leave Calculator**: Calculate leave entitlements as per Factories Act and state laws

**Government Sector:**
- **Government Gratuity Calculator**: Calculate gratuity as per CCS (Pension) Rules
- **GPF Calculator**: Calculate General Provident Fund contributions
- **NPS Calculator**: Calculate New Pension Scheme contributions
- **Government Leave Calculator**: Calculate leave entitlements as per CCS (Leave) Rules

**Common:**
- **Compliance Checker**: Generate personalized compliance checklists

### Phase 2: Web Application ✅
- Clean, responsive web interface using Bootstrap
- Sector selection (Private vs Government)
- Individual calculators with form inputs and result displays
- API endpoints for programmatic access
- Interactive compliance checklist with download functionality
- PDF report generation for all calculations

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
   Or double-click `start_application.bat` for easy startup

4. **Access the application**
   - Open your browser and go to: `http://localhost:5000`
   - Select your sector (Private or Government) to access relevant calculators

## Usage

### Private Sector Calculators

**Gratuity Calculator**
- Enter last drawn salary (Basic + DA) and years of service
- Minimum 5 years required for eligibility
- Maximum gratuity capped at ₹20,00,000

**PF Calculator**
- Enter basic salary and dearness allowance
- Calculates employee and employer contributions
- Shows EPF and EPS breakdown

**ESI Calculator**
- Enter monthly salary to check eligibility
- ESI applicable for salaries up to ₹21,000/month
- Shows employee (0.75%) and employer (3.25%) contributions

**Leave Calculator**
- Enter days worked in year, state, and establishment type
- Calculates earned leave, casual leave, and sick leave
- Based on Factories Act and state-specific rules

### Government Sector Calculators

**Government Gratuity Calculator**
- Enter last drawn basic pay and years of service
- Minimum 10 years required for eligibility
- No maximum limit for government employees
- Formula: (Basic Pay × Years × 15) ÷ 26

**GPF Calculator**
- Enter basic pay and dearness allowance
- Shows minimum (6%), recommended (12%), and maximum (100%) contributions
- Voluntary contribution scheme

**NPS Calculator**
- Enter basic pay, DA, and employee contribution rate (10-14%)
- Government contributes 14% automatically
- Applicable for post-2004 recruits

**Government Leave Calculator**
- Standardized leave entitlements as per CCS (Leave) Rules
- 30 days earned leave, 8 days casual leave, 20 days half-pay leave
- Additional leaves: Maternity (180 days), Paternity (15 days), Child Care (730 days)

### Common Features

**Compliance Checker**
- Select state, number of employees, and industry type
- Generates personalized compliance checklist
- Download checklist as PDF file

**PDF Reports**
- All calculators support PDF report generation
- Professional formatting with legal formulas and explanations
- Download reports for record keeping

## API Endpoints

All calculators are also available via REST API:

```bash
POST /api/calculate
Content-Type: application/json

# Private sector gratuity calculation
{
  "type": "gratuity",
  "salary": 50000,
  "years": 6,
  "sector": "private"
}

# Government sector gratuity calculation
{
  "type": "gratuity",
  "salary": 50000,
  "years": 15,
  "sector": "government"
}

# Private PF calculation
{
  "type": "pf",
  "basic": 25000,
  "da": 5000,
  "sector": "private"
}

# Government GPF calculation
{
  "type": "pf",
  "basic": 40000,
  "da": 8000,
  "sector": "government"
}

# NPS calculation
{
  "type": "nps",
  "basic": 45000,
  "da": 8000,
  "employee_rate": 10
}

# ESI calculation
{
  "type": "esi",
  "salary": 18000,
  "state": "general"
}

# Private sector leave calculation
{
  "type": "leave",
  "days_worked": 300,
  "state": "maharashtra",
  "establishment_type": "factory",
  "sector": "private"
}

# Government sector leave calculation
{
  "type": "leave",
  "sector": "government"
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

### Private Sector

**Gratuity**
- **Formula**: (Last Drawn Salary ÷ 26) × 15 × Years of Service
- **Eligibility**: Minimum 5 years of continuous service
- **Maximum**: ₹20,00,000 (as per 2018 amendment)

**Provident Fund**
- **Calculation Base**: Basic + DA, capped at ₹15,000
- **Employee Contribution**: 12% to EPF
- **Employer Contribution**: 12% (8.33% to EPS + 3.67% to EPF)

**ESI**
- **Wage Limit**: ₹21,000 per month
- **Employee Rate**: 0.75%
- **Employer Rate**: 3.25%

**Leave Entitlement**
- **Earned Leave**: 1 day per 20 days worked (Factories Act)
- **Casual Leave**: 7-12 days per year (varies by establishment)
- **Sick Leave**: 7-12 days per year (varies by establishment)

### Government Sector

**Gratuity**
- **Formula**: (Basic Pay × Years of Service × 15) ÷ 26
- **Eligibility**: Minimum 10 years of qualifying service
- **Maximum**: No limit for government employees

**General Provident Fund (GPF)**
- **Minimum Contribution**: 6% of basic pay
- **Maximum Contribution**: Up to 100% of basic pay
- **Voluntary**: Employee can choose contribution amount

**New Pension Scheme (NPS)**
- **Employee Contribution**: 10% (can increase to 14%)
- **Government Contribution**: 14% of Basic + DA
- **Applicable**: For employees recruited after 1st January 2004

**Leave Entitlement (CCS Rules)**
- **Earned Leave**: 30 days per year
- **Casual Leave**: 8 days per year
- **Half Pay Leave**: 20 days per year
- **Maternity Leave**: 180 days
- **Paternity Leave**: 15 days
- **Child Care Leave**: 730 days (during entire service)

## Testing

Run the test suite to verify calculations:

```bash
python core_calculators.py
```

## File Structure

```
Indian Labor Law Compliance System/
├── app.py                    # Flask web application
├── core_calculators.py       # Core calculation functions
├── pdf_generator.py          # PDF report generation
├── requirements.txt          # Python dependencies
├── README.md                # This file
├── start_application.bat    # Easy startup script
├── test_functionality.py    # Test all features
├── test_app.py              # Application tests
└── templates/               # HTML templates
    ├── base.html            # Base template
    ├── index.html           # Sector selection page
    ├── private_index.html   # Private sector home
    ├── government_index.html # Government sector home
    ├── gratuity.html        # Gratuity calculator (both sectors)
    ├── pf.html              # PF/GPF calculator
    ├── nps.html             # NPS calculator
    ├── esi.html             # ESI calculator
    ├── leave.html           # Leave calculator (both sectors)
    └── compliance.html      # Compliance checker
```

## Features Added ✅

- [x] **Sector Selection**: Choose between Private and Government sectors
- [x] **Government Calculators**: Gratuity, GPF, NPS, and Leave calculators
- [x] **Private Calculators**: Enhanced with sector-specific rules
- [x] **PDF Report Generation**: Professional PDF reports for all calculations
- [x] **Download Functionality**: Export reports as PDF with legal formulas
- [x] **Professional Layout**: Clean, formatted reports with tables and styling
- [x] **Legal Compliance**: Accurate formulas as per Indian labor laws
- [x] **Responsive Design**: Works on desktop and mobile devices

## Future Enhancements (Phase 3 & 4)

- [ ] **Database Integration**: Store calculations and user history
- [ ] **User Authentication**: Personal accounts and saved calculations
- [ ] **Advanced Compliance**: Tracking with deadlines and reminders
- [ ] **Government API Integration**: Real-time rate updates
- [ ] **Mobile App**: Native Android/iOS applications
- [ ] **Multi-language Support**: Hindi, regional languages
- [ ] **Email Notifications**: Compliance deadlines and updates
- [ ] **Pension Calculator**: Complete pension calculation for government employees
- [ ] **State-specific Rules**: Detailed state labor law variations
- [ ] **Bulk Processing**: Calculate for multiple employees at once

## Disclaimer

This application provides calculations based on general Indian labor law provisions. Specific requirements may vary by state, industry, and establishment size. Always consult with legal experts for complete compliance guidance.

## License

This project is for educational and informational purposes. Please ensure compliance with local laws and regulations.