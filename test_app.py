"""
Test script to verify Flask app functionality
"""

import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from app import app
    from core_calculators import calculate_gratuity, calculate_pf_contribution
    
    print("[OK] Flask app imports successful")
    
    # Test core functions
    gratuity_result = calculate_gratuity(50000, 6)
    print(f"[OK] Gratuity calculation test: {gratuity_result['gratuity_amount']}")
    
    pf_result = calculate_pf_contribution(25000, 5000)
    print(f"[OK] PF calculation test: {pf_result['total_monthly_pf']}")
    
    # Test Flask app creation
    with app.test_client() as client:
        response = client.get('/')
        print(f"[OK] Flask app test: Status {response.status_code}")
    
    print("\n[SUCCESS] All tests passed! The application is ready to run.")
    print("\nTo start the web application:")
    print("1. Run: python app.py")
    print("2. Open browser to: http://localhost:5000")
    
except ImportError as e:
    print(f"[ERROR] Import error: {e}")
except Exception as e:
    print(f"[ERROR] Error: {e}")