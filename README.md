# API Security Testing Framework

## Description
Developed an automated API security testing framework to identify vulnerabilities in REST APIs using Python, Flask, and security tools like OWASP ZAP and Burp Suite.

## Features
- JWT-based authentication testing
- BOLA vulnerability validation
- Rate-limiting enforcement testing
- API key exposure checks
- Automated security scanning

## Technologies Used
- Python
- Flask
- OWASP ZAP
- Burp Suite
- Postman

## Project Structure

api-security-testing/
│── api_server/
│   └── app.py
│── scanner/
│   └── security_scanner.py
│── requirements.txt
│── README.md

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run API server:
   python api_server/app.py

3. Run scanner:
   python scanner/security_scanner.py

## Key Results
- API availability confirmed
- JWT authentication working
- BOLA protection enforced
- Rate limiting validated
- No API key exposure detected

## Skills Demonstrated
- API Security Testing
- OWASP Top 10
- Vulnerability Assessment
- Automation using Python
- Security Tools Integration

## Future Improvements
- Integrate Kubernetes deployment
- Add advanced vulnerability scanning
- Automate CI/CD security testing

- ## 📄 Full Report
[View Detailed Report](project-report.pdf)
