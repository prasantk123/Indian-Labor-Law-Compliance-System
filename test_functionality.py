"""
Test script for Indian Labor Law Compliance System
Tests all the new government sector functionality
"""

from core_calculators import (
    calculate_gratuity, calculate_pf_contribution, calculate_nps_contribution,
    calculate_leave_entitlement, calculate_government_gratuity, calculate_government_gpf
)

def test_government_gratuity():
    print("=== Testing Government Gratuity ===")
    # Test eligible case
    result = calculate_gratuity(50000, 15, 'government')
    print(f"Government Gratuity (Rs.50,000, 15 years): {result}")
    
    # Test ineligible case
    result = calculate_gratuity(30000, 8, 'government')
    print(f"Government Gratuity (Rs.30,000, 8 years): {result}")
    print()

def test_private_gratuity():
    print("=== Testing Private Gratuity ===")
    # Test eligible case
    result = calculate_gratuity(50000, 6, 'private')
    print(f"Private Gratuity (Rs.50,000, 6 years): {result}")
    
    # Test ineligible case
    result = calculate_gratuity(30000, 4, 'private')
    print(f"Private Gratuity (Rs.30,000, 4 years): {result}")
    print()

def test_gpf():
    print("=== Testing Government GPF ===")
    result = calculate_pf_contribution(40000, 5000, 'government')
    print(f"GPF (Rs.40,000 basic, Rs.5,000 DA): {result}")
    print()

def test_private_pf():
    print("=== Testing Private PF ===")
    result = calculate_pf_contribution(25000, 3000, 'private')
    print(f"PF (Rs.25,000 basic, Rs.3,000 DA): {result}")
    print()

def test_nps():
    print("=== Testing NPS ===")
    result = calculate_nps_contribution(45000, 8000, 10)
    print(f"NPS (Rs.45,000 basic, Rs.8,000 DA, 10% employee): {result}")
    
    result = calculate_nps_contribution(45000, 8000, 14)
    print(f"NPS (Rs.45,000 basic, Rs.8,000 DA, 14% employee): {result}")
    print()

def test_government_leave():
    print("=== Testing Government Leave ===")
    result = calculate_leave_entitlement(0, '', '', 'government')
    print(f"Government Leave: {result}")
    print()

def test_private_leave():
    print("=== Testing Private Leave ===")
    result = calculate_leave_entitlement(300, 'maharashtra', 'factory', 'private')
    print(f"Private Leave (300 days, Maharashtra, Factory): {result}")
    print()

if __name__ == "__main__":
    print("Testing StatutoryCalc - Government Sector Features")
    print("=" * 70)
    
    test_government_gratuity()
    test_private_gratuity()
    test_gpf()
    test_private_pf()
    test_nps()
    test_government_leave()
    test_private_leave()
    
    print("All tests completed successfully!")
    print("\nTo run the web application:")
    print("1. Open command prompt")
    print("2. Navigate to the project folder")
    print("3. Run: python app.py")
    print("4. Open browser and go to: http://localhost:5000")