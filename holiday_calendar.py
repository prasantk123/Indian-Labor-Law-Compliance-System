"""
Government Holiday Calendar for Indian Labor Law Compliance System
Contains Central Government and Assam-specific holidays
"""

from datetime import datetime, date

def get_central_government_holidays_2025():
    """Get Central Government holidays for 2025"""
    holidays = [
        {'date': '2025-01-01', 'name': 'New Year\'s Day', 'type': 'Gazetted'},
        {'date': '2025-01-26', 'name': 'Republic Day', 'type': 'Gazetted'},
        {'date': '2025-03-14', 'name': 'Holi', 'type': 'Gazetted'},
        {'date': '2025-04-14', 'name': 'Dr. Ambedkar Jayanti', 'type': 'Gazetted'},
        {'date': '2025-04-18', 'name': 'Good Friday', 'type': 'Gazetted'},
        {'date': '2025-05-01', 'name': 'May Day', 'type': 'Gazetted'},
        {'date': '2025-08-15', 'name': 'Independence Day', 'type': 'Gazetted'},
        {'date': '2025-10-02', 'name': 'Gandhi Jayanti', 'type': 'Gazetted'},
        {'date': '2025-10-20', 'name': 'Dussehra', 'type': 'Gazetted'},
        {'date': '2025-11-09', 'name': 'Diwali', 'type': 'Gazetted'},
        {'date': '2025-11-10', 'name': 'Govardhan Puja', 'type': 'Gazetted'},
        {'date': '2025-12-25', 'name': 'Christmas Day', 'type': 'Gazetted'},
        
        # Restricted holidays (employees can choose 2)
        {'date': '2025-01-14', 'name': 'Makar Sankranti', 'type': 'Restricted'},
        {'date': '2025-02-26', 'name': 'Maha Shivratri', 'type': 'Restricted'},
        {'date': '2025-03-13', 'name': 'Holika Dahan', 'type': 'Restricted'},
        {'date': '2025-04-13', 'name': 'Baisakhi', 'type': 'Restricted'},
        {'date': '2025-04-17', 'name': 'Ram Navami', 'type': 'Restricted'},
        {'date': '2025-05-12', 'name': 'Buddha Purnima', 'type': 'Restricted'},
        {'date': '2025-08-12', 'name': 'Raksha Bandhan', 'type': 'Restricted'},
        {'date': '2025-08-20', 'name': 'Janmashtami', 'type': 'Restricted'},
        {'date': '2025-09-07', 'name': 'Ganesh Chaturthi', 'type': 'Restricted'},
        {'date': '2025-10-21', 'name': 'Karva Chauth', 'type': 'Restricted'},
        {'date': '2025-11-05', 'name': 'Dhanteras', 'type': 'Restricted'},
        {'date': '2025-11-11', 'name': 'Bhai Dooj', 'type': 'Restricted'}
    ]
    return holidays

def get_assam_specific_holidays_2025():
    """Get Assam-specific holidays for 2025"""
    holidays = [
        {'date': '2025-01-15', 'name': 'Magh Bihu/Bhogali Bihu', 'type': 'State'},
        {'date': '2025-04-14', 'name': 'Bohag Bihu/Rongali Bihu (Day 1)', 'type': 'State'},
        {'date': '2025-04-15', 'name': 'Bohag Bihu/Rongali Bihu (Day 2)', 'type': 'State'},
        {'date': '2025-04-16', 'name': 'Bohag Bihu/Rongali Bihu (Day 3)', 'type': 'State'},
        {'date': '2025-10-16', 'name': 'Kati Bihu/Kongali Bihu', 'type': 'State'},
        {'date': '2025-11-01', 'name': 'Kali Puja', 'type': 'State'},
        {'date': '2025-11-24', 'name': 'Guru Nanak Jayanti', 'type': 'State'},
        {'date': '2025-12-23', 'name': 'Srimanta Sankardeva\'s Birthday', 'type': 'State'},
        
        # Additional Assam festivals
        {'date': '2025-02-18', 'name': 'Saraswati Puja', 'type': 'State'},
        {'date': '2025-03-31', 'name': 'Chaitra Sankranti', 'type': 'State'},
        {'date': '2025-06-21', 'name': 'Ambubachi Mela (Start)', 'type': 'State'},
        {'date': '2025-08-31', 'name': 'Manasa Puja', 'type': 'State'},
        {'date': '2025-09-17', 'name': 'Vishwakarma Puja', 'type': 'State'}
    ]
    return holidays

def get_all_holidays_2025(state='central'):
    """Get all holidays for 2025 based on state"""
    central_holidays = get_central_government_holidays_2025()
    
    if state.lower() == 'assam':
        assam_holidays = get_assam_specific_holidays_2025()
        all_holidays = central_holidays + assam_holidays
    else:
        all_holidays = central_holidays
    
    # Sort by date
    all_holidays.sort(key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'))
    return all_holidays

def get_holidays_by_month(year=2025, state='central'):
    """Get holidays organized by month"""
    holidays = get_all_holidays_2025(state)
    months = {}
    
    for holiday in holidays:
        holiday_date = datetime.strptime(holiday['date'], '%Y-%m-%d')
        month_name = holiday_date.strftime('%B')
        
        if month_name not in months:
            months[month_name] = []
        
        months[month_name].append({
            'date': holiday_date.strftime('%d'),
            'day': holiday_date.strftime('%A'),
            'name': holiday['name'],
            'type': holiday['type']
        })
    
    return months

def count_working_days(year=2025, state='central'):
    """Calculate working days in a year excluding holidays and Sundays"""
    holidays = get_all_holidays_2025(state)
    holiday_dates = [datetime.strptime(h['date'], '%Y-%m-%d').date() for h in holidays]
    
    total_days = 365 if year % 4 != 0 else 366
    sundays = 52 if year % 4 != 0 else 53  # Approximate
    
    working_days = total_days - len(holiday_dates) - sundays
    return {
        'total_days': total_days,
        'holidays': len(holiday_dates),
        'sundays': sundays,
        'working_days': working_days
    }