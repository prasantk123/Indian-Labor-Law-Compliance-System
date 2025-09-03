"""
PDF Report Generator for Indian Labor Law Compliance System
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime
import io

def generate_calculation_report(calc_type, data, result):
    """Generate PDF report for calculations"""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []
    
    # Title
    title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], 
                                fontSize=18, spaceAfter=30, alignment=1)
    story.append(Paragraph("Indian Labor Law Compliance Report", title_style))
    story.append(Spacer(1, 12))
    
    # Report info
    info_data = [
        ['Report Type:', calc_type.title() + ' Calculator'],
        ['Generated On:', datetime.now().strftime('%d %B %Y at %I:%M %p')],
        ['System:', 'Indian Labor Law Compliance System'],
        ['Developer:', 'Prasant Kumar']
    ]
    info_table = Table(info_data, colWidths=[2*inch, 4*inch])
    info_table.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('GRID', (0,0), (-1,-1), 1, colors.lightgrey)
    ]))
    story.append(info_table)
    story.append(Spacer(1, 20))
    
    if calc_type == 'gratuity':
        story.extend(_generate_gratuity_content(data, result, styles))
    elif calc_type == 'pf':
        story.extend(_generate_pf_content(data, result, styles))
    elif calc_type == 'gpf':
        story.extend(_generate_gpf_content(data, result, styles))
    elif calc_type == 'nps':
        story.extend(_generate_nps_content(data, result, styles))
    elif calc_type == 'esi':
        story.extend(_generate_esi_content(data, result, styles))
    elif calc_type == 'leave':
        story.extend(_generate_leave_content(data, result, styles))
    
    # Footer
    story.append(Spacer(1, 30))
    footer_text = "This report is generated for informational purposes. Please consult legal experts for complete compliance."
    story.append(Paragraph(footer_text, styles['Normal']))
    story.append(Spacer(1, 10))
    developer_text = "Developed by Prasant Kumar | Indian Labor Law Compliance System"
    story.append(Paragraph(developer_text, styles['Normal']))
    
    doc.build(story)
    buffer.seek(0)
    return buffer

def _generate_gratuity_content(data, result, styles):
    content = []
    
    sector = result.get('sector', 'private')
    title = f"{'Government' if sector == 'government' else 'Private Sector'} Gratuity Calculation Report"
    content.append(Paragraph(title, styles['Heading2']))
    content.append(Spacer(1, 12))
    
    # Input data
    salary_label = 'Last Drawn Basic Pay' if sector == 'government' else 'Last Drawn Salary (Basic + DA)'
    input_data = [
        ['Parameter', 'Value'],
        [salary_label, f"₹{data['salary']:,.2f}"],
        ['Years of Service', f"{data['years']} years"],
        ['Sector', sector.title()]
    ]
    
    input_table = Table(input_data, colWidths=[3*inch, 2*inch])
    input_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 12),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ]))
    content.append(input_table)
    content.append(Spacer(1, 20))
    
    # Results
    if result['eligible']:
        if sector == 'government':
            formula = f"({data['salary']:,.2f} × {data['years']} × 15) ÷ 26"
        else:
            formula = f"({data['salary']:,.2f} ÷ 26) × 15 × {data['years']}"
            
        result_data = [
            ['Calculation Result', 'Amount'],
            ['Gratuity Amount', f"₹{result['gratuity_amount']:,.2f}"],
            ['Status', 'Eligible'],
            ['Formula Used', formula]
        ]
        
        if result.get('capped_at_maximum'):
            result_data.append(['Note', 'Amount capped at maximum ₹20,00,000'])
        elif sector == 'government':
            result_data.append(['Note', result.get('note', 'No maximum limit for government employees')])
    else:
        result_data = [
            ['Calculation Result', 'Status'],
            ['Gratuity Amount', '₹0.00'],
            ['Status', 'Not Eligible'],
            ['Reason', result['reason']]
        ]
    
    result_table = Table(result_data, colWidths=[3*inch, 2*inch])
    result_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightblue),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 11),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ]))
    content.append(result_table)
    
    return content

def _generate_pf_content(data, result, styles):
    content = []
    
    content.append(Paragraph("Provident Fund Calculation Report", styles['Heading2']))
    content.append(Spacer(1, 12))
    
    # Input data
    input_data = [
        ['Parameter', 'Value'],
        ['Basic Salary', f"₹{data['basic']:,.2f}"],
        ['Dearness Allowance', f"₹{data.get('da', 0):,.2f}"],
        ['PF Eligible Salary', f"₹{result['pf_eligible_salary']:,.2f}"]
    ]
    
    input_table = Table(input_data, colWidths=[3*inch, 2*inch])
    input_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 12),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ]))
    content.append(input_table)
    content.append(Spacer(1, 20))
    
    # Results
    result_data = [
        ['Contribution Type', 'Amount', 'Rate'],
        ['Employee EPF', f"₹{result['employee_contribution']:,.2f}", '12%'],
        ['Employer EPF', f"₹{result['employer_epf_contribution']:,.2f}", '3.67%'],
        ['Employer EPS', f"₹{result['employer_eps_contribution']:,.2f}", '8.33%'],
        ['Total Monthly PF', f"₹{result['total_monthly_pf']:,.2f}", '24%']
    ]
    
    result_table = Table(result_data, colWidths=[2.5*inch, 1.5*inch, 1*inch])
    result_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightblue),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 11),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ]))
    content.append(result_table)
    
    return content

def _generate_gpf_content(data, result, styles):
    content = []
    
    content.append(Paragraph("General Provident Fund (GPF) Report", styles['Heading2']))
    content.append(Spacer(1, 12))
    
    # Input data
    input_data = [
        ['Parameter', 'Value'],
        ['Basic Pay', f"₹{data['basic']:,.2f}"],
        ['Dearness Allowance', f"₹{data.get('da', 0):,.2f}"],
        ['Sector', 'Government']
    ]
    
    input_table = Table(input_data, colWidths=[3*inch, 2*inch])
    input_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 12),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ]))
    content.append(input_table)
    content.append(Spacer(1, 20))
    
    # Results
    result_data = [
        ['GPF Contribution Options', 'Amount', 'Rate'],
        ['Minimum Contribution', f"₹{result['min_gpf_contribution']:,.2f}", '6%'],
        ['Recommended Contribution', f"₹{result['recommended_contribution']:,.2f}", '12%'],
        ['Maximum Contribution', f"₹{result['max_gpf_contribution']:,.2f}", '100%']
    ]
    
    result_table = Table(result_data, colWidths=[2.5*inch, 1.5*inch, 1*inch])
    result_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightgreen),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 11),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ]))
    content.append(result_table)
    
    # Note
    content.append(Spacer(1, 12))
    note_text = f"Note: {result.get('note', 'GPF contribution is voluntary for government employees')}"
    content.append(Paragraph(note_text, styles['Normal']))
    
    return content

def _generate_nps_content(data, result, styles):
    content = []
    
    content.append(Paragraph("New Pension Scheme (NPS) Report", styles['Heading2']))
    content.append(Spacer(1, 12))
    
    # Input data
    input_data = [
        ['Parameter', 'Value'],
        ['Basic Pay', f"₹{data['basic']:,.2f}"],
        ['Dearness Allowance', f"₹{data.get('da', 0):,.2f}"],
        ['NPS Eligible Salary', f"₹{result['nps_eligible_salary']:,.2f}"],
        ['Employee Contribution Rate', f"{data.get('employee_rate', 10)}%"]
    ]
    
    input_table = Table(input_data, colWidths=[3*inch, 2*inch])
    input_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 12),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ]))
    content.append(input_table)
    content.append(Spacer(1, 20))
    
    # Results
    result_data = [
        ['NPS Contribution', 'Amount', 'Rate'],
        ['Employee Contribution', f"₹{result['employee_contribution']:,.2f}", f"{result['employee_rate']}%"],
        ['Government Contribution', f"₹{result['employer_contribution']:,.2f}", f"{result['employer_rate']}%"],
        ['Total Monthly NPS', f"₹{result['total_contribution']:,.2f}", f"{result['employee_rate'] + result['employer_rate']}%"]
    ]
    
    result_table = Table(result_data, colWidths=[2.5*inch, 1.5*inch, 1*inch])
    result_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightcoral),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 11),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ]))
    content.append(result_table)
    
    # Note
    content.append(Spacer(1, 12))
    note_text = "Note: NPS is applicable for government employees recruited on or after 1st January 2004. The scheme provides market-linked returns."
    content.append(Paragraph(note_text, styles['Normal']))
    
    return content

def _generate_esi_content(data, result, styles):
    content = []
    
    content.append(Paragraph("ESI Calculation Report", styles['Heading2']))
    content.append(Spacer(1, 12))
    
    # Input data
    input_data = [
        ['Parameter', 'Value'],
        ['Monthly Salary', f"{data['salary']:,.2f}"],
        ['State', data.get('state', 'General').title()]
    ]
    
    input_table = Table(input_data, colWidths=[3*inch, 2*inch])
    input_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 12),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ]))
    content.append(input_table)
    content.append(Spacer(1, 20))
    
    # Results
    if result['eligible']:
        result_data = [
            ['Contribution Type', 'Amount', 'Rate'],
            ['Employee ESI', f"{result['employee_contribution']:,.2f}", '0.75%'],
            ['Employer ESI', f"{result['employer_contribution']:,.2f}", '3.25%'],
            ['Total ESI', f"{result['total_contribution']:,.2f}", '4.00%'],
            ['Status', 'Eligible', '']
        ]
    else:
        result_data = [
            ['Result', 'Status'],
            ['ESI Eligibility', 'Not Eligible'],
            ['Reason', result['reason']]
        ]
    
    result_table = Table(result_data, colWidths=[2.5*inch, 1.5*inch, 1*inch])
    result_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightblue),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 11),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ]))
    content.append(result_table)
    
    return content

def _generate_leave_content(data, result, styles):
    content = []
    
    sector = result.get('sector', 'private')
    title = f"{'Government' if sector == 'government' else 'Private Sector'} Leave Entitlement Report"
    content.append(Paragraph(title, styles['Heading2']))
    content.append(Spacer(1, 12))
    
    # Input data
    if sector == 'government':
        input_data = [
            ['Parameter', 'Value'],
            ['Sector', 'Government'],
            ['Rules', 'CCS (Leave) Rules, 1972']
        ]
    else:
        input_data = [
            ['Parameter', 'Value'],
            ['Days Worked in Year', f"{data['days_worked']} days"],
            ['State', data.get('state', 'General').title()],
            ['Establishment Type', data.get('establishment_type', 'Factory').title()],
            ['Sector', 'Private']
        ]
    
    input_table = Table(input_data, colWidths=[3*inch, 2*inch])
    input_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 12),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ]))
    content.append(input_table)
    content.append(Spacer(1, 20))
    
    # Results
    result_data = [
        ['Leave Type', 'Days Entitled']
    ]
    
    if sector == 'government':
        result_data.extend([
            ['Earned Leave', f"{result['earned_leave']} days per year"],
            ['Casual Leave', f"{result['casual_leave']} days per year"],
            ['Half Pay Leave', f"{result['sick_leave']} days per year"],
            ['Maternity Leave', f"{result['maternity_leave']} days"],
            ['Paternity Leave', f"{result['paternity_leave']} days"],
            ['Child Care Leave', f"{result['child_care_leave']} days (entire service)"],
            ['Total Annual Leave', f"{result['total_annual_leave']} days"]
        ])
    else:
        result_data.extend([
            ['Earned Leave', f"{result['earned_leave']} days"],
            ['Casual Leave', f"{result['casual_leave']} days"],
            ['Sick Leave', f"{result['sick_leave']} days"],
            ['Total Annual Leave', f"{result['total_annual_leave']} days"]
        ])
    
    result_table = Table(result_data, colWidths=[3*inch, 2*inch])
    result_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightblue),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 11),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ]))
    content.append(result_table)
    
    # Add note for government employees
    if sector == 'government':
        content.append(Spacer(1, 12))
        note_text = result.get('note', 'As per CCS (Leave) Rules, 1972')
        content.append(Paragraph(f"Note: {note_text}", styles['Normal']))
    
    return content

def generate_compliance_report(state, num_employees, industry_type, checklist):
    """Generate PDF report for compliance checklist"""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []
    
    # Title
    title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], 
                                fontSize=18, spaceAfter=30, alignment=1)
    story.append(Paragraph("Compliance Checklist Report", title_style))
    story.append(Spacer(1, 12))
    
    # Report info
    info_data = [
        ['State:', state],
        ['Number of Employees:', str(num_employees)],
        ['Industry Type:', industry_type],
        ['Generated On:', datetime.now().strftime('%d %B %Y at %I:%M %p')],
        ['Total Requirements:', str(len(checklist))],
        ['Developer:', 'Prasant Kumar']
    ]
    info_table = Table(info_data, colWidths=[2*inch, 4*inch])
    info_table.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('GRID', (0,0), (-1,-1), 1, colors.lightgrey)
    ]))
    story.append(info_table)
    story.append(Spacer(1, 20))
    
    # Checklist
    story.append(Paragraph("Compliance Requirements Checklist", styles['Heading2']))
    story.append(Spacer(1, 12))
    
    checklist_data = [['S.No.', 'Compliance Requirement', 'Status']]
    for i, item in enumerate(checklist, 1):
        checklist_data.append([str(i), item, '☐ Pending'])
    
    checklist_table = Table(checklist_data, colWidths=[0.5*inch, 4.5*inch, 1*inch])
    checklist_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('VALIGN', (0,0), (-1,-1), 'TOP')
    ]))
    story.append(checklist_table)
    
    # Footer
    story.append(Spacer(1, 30))
    footer_text = "This checklist is based on general compliance requirements. Specific requirements may vary. Please consult with legal experts for complete compliance guidance."
    story.append(Paragraph(footer_text, styles['Normal']))
    story.append(Spacer(1, 10))
    developer_text = "Developed by Prasant Kumar | Indian Labor Law Compliance System"
    story.append(Paragraph(developer_text, styles['Normal']))
    
    doc.build(story)
    buffer.seek(0)
    return buffer