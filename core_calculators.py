"""
Indian Labor Law Compliance System - Core Calculators
Handles Gratuity, PF, ESI, and Leave calculations as per Indian labor laws
"""

def calculate_gratuity(last_drawn_salary, years_of_service, sector='private', is_covered_establishment=True):
    """
    Calculate gratuity as per Payment of Gratuity Act, 1972 (Private) or CCS Rules (Government)
    
    Args:
        last_drawn_salary: Last drawn basic + DA salary
        years_of_service: Total years of service
        sector: 'private' or 'government'
        is_covered_establishment: True for establishments covered under the Act
    
    Returns:
        dict: Contains gratuity amount and eligibility status
    """
    if sector == 'government':
        return calculate_government_gratuity(last_drawn_salary, years_of_service)
    
    if years_of_service < 5:
        return {
            'eligible': False,
            'gratuity_amount': 0,
            'reason': 'Minimum 5 years of service required',
            'sector': 'private'
        }
    
    # Formula: (Last Drawn Salary / 26) * 15 * Years of Service
    # Maximum gratuity: Rs. 20,00,000 (as per 2018 amendment)
    gratuity_amount = (last_drawn_salary / 26) * 15 * years_of_service
    max_gratuity = 2000000  # Rs. 20 lakhs
    
    if gratuity_amount > max_gratuity:
        gratuity_amount = max_gratuity
    
    return {
        'eligible': True,
        'gratuity_amount': round(gratuity_amount, 2),
        'capped_at_maximum': gratuity_amount == max_gratuity,
        'sector': 'private'
    }

def calculate_government_gratuity(last_drawn_salary, years_of_service):
    """
    Calculate gratuity for government employees as per CCS (Pension) Rules
    
    Args:
        last_drawn_salary: Last drawn basic pay
        years_of_service: Total qualifying service
    
    Returns:
        dict: Government gratuity calculation
    """
    if years_of_service < 10:
        return {
            'eligible': False,
            'gratuity_amount': 0,
            'reason': 'Minimum 10 years of qualifying service required for government employees',
            'sector': 'government'
        }
    
    # Government gratuity formula: (Basic Pay * Years of Service * 15) / 26
    # No maximum limit for government employees
    gratuity_amount = (last_drawn_salary * years_of_service * 15) / 26
    
    return {
        'eligible': True,
        'gratuity_amount': round(gratuity_amount, 2),
        'sector': 'government',
        'note': 'No maximum limit for government employees'
    }

def calculate_pf_contribution(basic_salary, da=0, sector='private', employee_contribution_rate=12, employer_contribution_rate=12):
    """
    Calculate PF/GPF contribution as per applicable rules
    
    Args:
        basic_salary: Basic salary
        da: Dearness allowance
        sector: 'private' or 'government'
        employee_contribution_rate: Employee contribution percentage (default 12%)
        employer_contribution_rate: Employer contribution percentage (default 12%)
    
    Returns:
        dict: PF/GPF contribution details
    """
    if sector == 'government':
        return calculate_government_gpf(basic_salary, da)
    
    # PF is calculated on Basic + DA, capped at Rs. 15,000
    pf_eligible_salary = min(basic_salary + da, 15000)
    
    employee_contribution = (pf_eligible_salary * employee_contribution_rate) / 100
    employer_contribution = (pf_eligible_salary * employer_contribution_rate) / 100
    
    # Employer contribution split: 8.33% to EPS, 3.67% to EPF
    eps_contribution = (pf_eligible_salary * 8.33) / 100
    epf_contribution = employer_contribution - eps_contribution
    
    return {
        'pf_eligible_salary': pf_eligible_salary,
        'employee_contribution': round(employee_contribution, 2),
        'employer_epf_contribution': round(epf_contribution, 2),
        'employer_eps_contribution': round(eps_contribution, 2),
        'total_employer_contribution': round(employer_contribution, 2),
        'total_monthly_pf': round(employee_contribution + employer_contribution, 2),
        'sector': 'private'
    }

def calculate_government_gpf(basic_salary, da=0):
    """
    Calculate GPF for government employees
    
    Args:
        basic_salary: Basic pay
        da: Dearness allowance
    
    Returns:
        dict: GPF contribution details
    """
    # GPF: Minimum 6% of basic pay, can contribute up to full basic pay
    min_contribution = (basic_salary * 6) / 100
    max_contribution = basic_salary
    
    return {
        'basic_salary': basic_salary,
        'min_gpf_contribution': round(min_contribution, 2),
        'max_gpf_contribution': round(max_contribution, 2),
        'recommended_contribution': round((basic_salary * 12) / 100, 2),
        'sector': 'government',
        'note': 'GPF contribution is voluntary, minimum 6% of basic pay'
    }

def calculate_nps_contribution(basic_salary, da=0, employee_rate=10, employer_rate=14):
    """
    Calculate NPS contribution for government employees (post-2004 recruits)
    
    Args:
        basic_salary: Basic pay
        da: Dearness allowance
        employee_rate: Employee contribution rate (default 10%)
        employer_rate: Government contribution rate (default 14%)
    
    Returns:
        dict: NPS contribution details
    """
    nps_eligible_salary = basic_salary + da
    
    employee_contribution = (nps_eligible_salary * employee_rate) / 100
    employer_contribution = (nps_eligible_salary * employer_rate) / 100
    
    return {
        'nps_eligible_salary': nps_eligible_salary,
        'employee_contribution': round(employee_contribution, 2),
        'employer_contribution': round(employer_contribution, 2),
        'total_contribution': round(employee_contribution + employer_contribution, 2),
        'employee_rate': employee_rate,
        'employer_rate': employer_rate,
        'sector': 'government'
    }

def is_esi_applicable(monthly_salary, state='general'):
    """
    Check ESI eligibility as per Employees' State Insurance Act, 1948
    
    Args:
        monthly_salary: Monthly salary
        state: State (some states have different limits)
    
    Returns:
        dict: ESI eligibility and contribution details
    """
    # ESI wage limit: Rs. 21,000 per month (as of 2022)
    esi_wage_limit = 21000
    
    if monthly_salary > esi_wage_limit:
        return {
            'eligible': False,
            'reason': f'Monthly salary exceeds ESI limit of Rs. {esi_wage_limit}',
            'employee_contribution': 0,
            'employer_contribution': 0
        }
    
    # ESI contribution rates: Employee 0.75%, Employer 3.25%
    employee_rate = 0.75
    employer_rate = 3.25
    
    employee_contribution = (monthly_salary * employee_rate) / 100
    employer_contribution = (monthly_salary * employer_rate) / 100
    
    return {
        'eligible': True,
        'employee_contribution': round(employee_contribution, 2),
        'employer_contribution': round(employer_contribution, 2),
        'total_contribution': round(employee_contribution + employer_contribution, 2)
    }

def calculate_leave_entitlement(days_worked_in_year, state='general', establishment_type='factory', sector='private'):
    """
    Calculate leave entitlement as per applicable laws
    
    Args:
        days_worked_in_year: Number of days worked in the year
        state: State (different states may have variations)
        establishment_type: Type of establishment (factory, shop, etc.)
        sector: 'private' or 'government'
    
    Returns:
        dict: Leave entitlement details
    """
    if sector == 'government':
        return calculate_government_leave_entitlement()
    
    # Earned Leave (Annual Leave) - Factories Act: 1 day for every 20 days worked
    if establishment_type.lower() == 'factory':
        earned_leave = days_worked_in_year // 20
        # Maximum 30 days can be accumulated
        earned_leave = min(earned_leave, 30)
    else:
        # For shops and establishments: varies by state, generally 1 day per 20 days
        earned_leave = days_worked_in_year // 20
        earned_leave = min(earned_leave, 21)  # Common limit for shops
    
    # Casual Leave - typically 7-12 days per year
    casual_leave = 7 if establishment_type.lower() == 'shop' else 12
    
    # Sick Leave - varies by state and establishment
    sick_leave = 7 if establishment_type.lower() == 'shop' else 12
    
    # State-specific adjustments
    if state.lower() in ['maharashtra', 'karnataka', 'tamil nadu']:
        if establishment_type.lower() == 'shop':
            earned_leave = min(days_worked_in_year // 18, 21)  # Slightly better ratio
    
    return {
        'earned_leave': earned_leave,
        'casual_leave': casual_leave,
        'sick_leave': sick_leave,
        'total_annual_leave': earned_leave + casual_leave + sick_leave,
        'establishment_type': establishment_type,
        'state': state,
        'sector': 'private'
    }

def calculate_government_leave_entitlement():
    """
    Calculate leave entitlement for government employees as per CCS (Leave) Rules
    
    Returns:
        dict: Government leave entitlement details
    """
    return {
        'earned_leave': 30,  # 30 days per year
        'casual_leave': 8,   # 8 days per year
        'sick_leave': 20,    # 20 days per year (half pay leave)
        'maternity_leave': 180,  # 180 days
        'paternity_leave': 15,   # 15 days
        'child_care_leave': 730, # 2 years during entire service
        'study_leave': 'As per rules',
        'total_annual_leave': 58,  # Earned + Casual + Sick
        'sector': 'government',
        'note': 'As per CCS (Leave) Rules, 1972'
    }

def generate_compliance_checklist(state, num_employees, industry_type):
    """
    Generate compliance checklist based on establishment details
    
    Args:
        state: State of operation
        num_employees: Number of employees
        industry_type: Type of industry (factory, shop, IT, etc.)
    
    Returns:
        list: Compliance requirements checklist
    """
    checklist = []
    
    # Basic registrations for all establishments
    checklist.append("Obtain Trade License from local municipal authority")
    checklist.append("Register for GST if annual turnover exceeds Rs. 20 lakhs")
    
    # Employee-based compliances
    if num_employees >= 1:
        checklist.append("Maintain attendance register for all employees")
        checklist.append("Issue appointment letters to all employees")
    
    if num_employees >= 10:
        checklist.append("Register under applicable Shops and Establishment Act")
        if industry_type.lower() == 'factory':
            checklist.append("Register under Factories Act, 1948")
            checklist.append("Obtain Factory License from State Factory Inspector")
    
    if num_employees >= 20:
        checklist.append("Register for Employee Provident Fund (EPF)")
        checklist.append("Register for Employee State Insurance (ESI)")
        checklist.append("Comply with Payment of Gratuity Act, 1972")
    
    if num_employees >= 30:
        checklist.append("Constitute Internal Complaints Committee (ICC) for POSH Act")
    
    if num_employees >= 100:
        checklist.append("Register under Contract Labour Act (if applicable)")
    
    # Industry-specific compliances
    if industry_type.lower() == 'factory':
        checklist.append("Maintain factory registers as per Factories Act")
        checklist.append("Conduct annual medical examination of workers")
        if num_employees >= 50:
            checklist.append("Appoint Safety Officer")
    
    if industry_type.lower() in ['it', 'software', 'services']:
        checklist.append("Comply with IT Act provisions for data protection")
        checklist.append("Register under Professional Tax Act")
    
    # State-specific additions
    state_lower = state.lower()
    if state_lower == 'maharashtra':
        checklist.append("Register under Maharashtra Shops and Establishment Act")
        if num_employees >= 5:
            checklist.append("Register for Professional Tax in Maharashtra")
    elif state_lower == 'karnataka':
        checklist.append("Register under Karnataka Shops and Commercial Establishment Act")
    elif state_lower == 'tamil nadu':
        checklist.append("Register under Tamil Nadu Shops and Establishment Act")
    
    return checklist

# Test functions
def run_tests():
    """Run comprehensive tests for all calculators"""
    print("Running Core Calculator Tests...")
    
    # Test Gratuity Calculator
    print("\n1. Testing Gratuity Calculator:")
    test_cases = [
        (50000, 6, True),   # Eligible case
        (30000, 4, True),   # Not eligible - less than 5 years
        (100000, 15, True), # High salary case
    ]
    
    for salary, years, covered in test_cases:
        result = calculate_gratuity(salary, years, covered)
        print(f"Salary: {salary}, Years: {years} -> {result}")
    
    # Test PF Calculator
    print("\n2. Testing PF Calculator:")
    pf_result = calculate_pf_contribution(25000, 5000)
    print(f"PF for Basic: 25000, DA: 5000 -> {pf_result}")
    
    # Test ESI Calculator
    print("\n3. Testing ESI Calculator:")
    esi_result = is_esi_applicable(18000)
    print(f"ESI for salary 18000 -> {esi_result}")
    
    # Test Leave Calculator
    print("\n4. Testing Leave Calculator:")
    leave_result = calculate_leave_entitlement(300, 'maharashtra', 'factory')
    print(f"Leave for 300 days worked -> {leave_result}")
    
    # Test Compliance Checklist
    print("\n5. Testing Compliance Checklist:")
    checklist = generate_compliance_checklist('Maharashtra', 25, 'Factory')
    print(f"Checklist for Maharashtra, 25 employees, Factory:")
    for item in checklist[:5]:  # Show first 5 items
        print(f"- {item}")

if __name__ == "__main__":
    run_tests()