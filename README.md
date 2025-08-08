# Equifax Breach Educational Demo

**IMPORTANT: This is an educational demonstration only. Do not use these techniques on any systems without authorization.**

This project demonstrates the Apache Struts vulnerability (CVE-2017-5638) that led to the Equifax data breach in a controlled, safe environment.

## Project Structure
- `app/`: Contains the vulnerable web application
- `exploit/`: Contains the demonstration exploit script
- `data/`: Sample (fake) data for demonstration

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run the demo app: `python app/app.py`
3. Access the web interface at `http://localhost:5000`

## Educational Purpose
This demo is designed to:
1. Understand how the vulnerability worked
2. Learn about proper security practices
3. Demonstrate the importance of patch management

## Disclaimer
This is purely for educational purposes. The application intentionally contains vulnerabilities to demonstrate security concepts. Do not deploy this in any production environment.
