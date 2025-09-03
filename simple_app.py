from flask import Flask, render_template, request
from core_calculators import calculate_gratuity

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Indian Labor Law Compliance System</h1>
    <p>System is working!</p>
    <a href="/test">Test Gratuity Calculator</a>
    '''

@app.route('/test')
def test():
    result = calculate_gratuity(50000, 6)
    return f'''
    <h2>Test Result</h2>
    <p>Gratuity for 50000 salary, 6 years: {result}</p>
    <a href="/">Back to Home</a>
    '''

if __name__ == '__main__':
    print("Starting simple Flask app on http://127.0.0.1:5000")
    app.run(host='127.0.0.1', port=5000, debug=True)