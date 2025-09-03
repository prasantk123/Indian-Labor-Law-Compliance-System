"""
Flask Web Application for Indian Labor Law Compliance System
"""

from flask import Flask, render_template, request, jsonify, send_file
from core_calculators import (
    calculate_gratuity, calculate_pf_contribution, is_esi_applicable,
    calculate_leave_entitlement, generate_compliance_checklist
)
from pdf_generator import generate_calculation_report, generate_compliance_report

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gratuity', methods=['GET', 'POST'])
def gratuity_calculator():
    if request.method == 'POST':
        try:
            salary = float(request.form['salary'])
            years = float(request.form['years'])
            result = calculate_gratuity(salary, years)
            return render_template('gratuity.html', result=result, salary=salary, years=years)
        except ValueError:
            error = "Please enter valid numbers"
            return render_template('gratuity.html', error=error)
    return render_template('gratuity.html')

@app.route('/pf', methods=['GET', 'POST'])
def pf_calculator():
    if request.method == 'POST':
        try:
            basic = float(request.form['basic'])
            da = float(request.form.get('da', 0))
            result = calculate_pf_contribution(basic, da)
            return render_template('pf.html', result=result, basic=basic, da=da)
        except ValueError:
            error = "Please enter valid numbers"
            return render_template('pf.html', error=error)
    return render_template('pf.html')

@app.route('/esi', methods=['GET', 'POST'])
def esi_calculator():
    if request.method == 'POST':
        try:
            salary = float(request.form['salary'])
            state = request.form.get('state', 'general')
            result = is_esi_applicable(salary, state)
            return render_template('esi.html', result=result, salary=salary, state=state)
        except ValueError:
            error = "Please enter valid numbers"
            return render_template('esi.html', error=error)
    return render_template('esi.html')

@app.route('/leave', methods=['GET', 'POST'])
def leave_calculator():
    if request.method == 'POST':
        try:
            days_worked = int(request.form['days_worked'])
            state = request.form.get('state', 'general')
            establishment_type = request.form.get('establishment_type', 'factory')
            result = calculate_leave_entitlement(days_worked, state, establishment_type)
            return render_template('leave.html', result=result, days_worked=days_worked, 
                                 state=state, establishment_type=establishment_type)
        except ValueError:
            error = "Please enter valid numbers"
            return render_template('leave.html', error=error)
    return render_template('leave.html')

@app.route('/compliance', methods=['GET', 'POST'])
def compliance_checker():
    if request.method == 'POST':
        try:
            state = request.form['state']
            num_employees = int(request.form['num_employees'])
            industry_type = request.form['industry_type']
            checklist = generate_compliance_checklist(state, num_employees, industry_type)
            return render_template('compliance.html', checklist=checklist, 
                                 state=state, num_employees=num_employees, 
                                 industry_type=industry_type)
        except ValueError:
            error = "Please enter valid information"
            return render_template('compliance.html', error=error)
    return render_template('compliance.html')

@app.route('/download/<calc_type>/<format>')
def download_report(calc_type, format):
    """Download calculation reports"""
    if format != 'pdf':
        return "Invalid format", 400
    
    # Get data from session or request args
    if calc_type == 'gratuity':
        salary = float(request.args.get('salary', 0))
        years = float(request.args.get('years', 0))
        data = {'salary': salary, 'years': years}
        result = calculate_gratuity(salary, years)
    elif calc_type == 'pf':
        basic = float(request.args.get('basic', 0))
        da = float(request.args.get('da', 0))
        data = {'basic': basic, 'da': da}
        result = calculate_pf_contribution(basic, da)
    elif calc_type == 'esi':
        salary = float(request.args.get('salary', 0))
        state = request.args.get('state', 'general')
        data = {'salary': salary, 'state': state}
        result = is_esi_applicable(salary, state)
    elif calc_type == 'leave':
        days_worked = int(request.args.get('days_worked', 0))
        state = request.args.get('state', 'general')
        establishment_type = request.args.get('establishment_type', 'factory')
        data = {'days_worked': days_worked, 'state': state, 'establishment_type': establishment_type}
        result = calculate_leave_entitlement(days_worked, state, establishment_type)
    elif calc_type == 'compliance':
        state = request.args.get('state', '')
        num_employees = int(request.args.get('num_employees', 0))
        industry_type = request.args.get('industry_type', '')
        checklist = generate_compliance_checklist(state, num_employees, industry_type)
        pdf_buffer = generate_compliance_report(state, num_employees, industry_type, checklist)
        return send_file(pdf_buffer, as_attachment=True, download_name=f'compliance_report.pdf', mimetype='application/pdf')
    else:
        return "Invalid calculation type", 400
    
    pdf_buffer = generate_calculation_report(calc_type, data, result)
    return send_file(pdf_buffer, as_attachment=True, download_name=f'{calc_type}_report.pdf', mimetype='application/pdf')

@app.route('/api/calculate', methods=['POST'])
def api_calculate():
    """API endpoint for calculations"""
    data = request.get_json()
    calc_type = data.get('type')
    
    try:
        if calc_type == 'gratuity':
            result = calculate_gratuity(data['salary'], data['years'])
        elif calc_type == 'pf':
            result = calculate_pf_contribution(data['basic'], data.get('da', 0))
        elif calc_type == 'esi':
            result = is_esi_applicable(data['salary'], data.get('state', 'general'))
        elif calc_type == 'leave':
            result = calculate_leave_entitlement(
                data['days_worked'], 
                data.get('state', 'general'),
                data.get('establishment_type', 'factory')
            )
        elif calc_type == 'compliance':
            result = generate_compliance_checklist(
                data['state'], 
                data['num_employees'], 
                data['industry_type']
            )
        else:
            return jsonify({'error': 'Invalid calculation type'}), 400
        
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    print("Starting Flask app on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)