# app.py
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load student and program details
def load_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error decoding {filename}: {str(e)}")
        return []
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return []

students_details = load_json('students_details.json')
program_details = load_json('program_details.json')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_student', methods=['POST'])
def get_student():
    reg_no = request.json['reg_no']
    student = next((s for s in students_details if s['reg_no'] == reg_no), None)
    if student:
        return jsonify({'name': student['name'], 'team': student['team']})
    return jsonify({'error': 'Student not found'}), 404

@app.route('/get_programs', methods=['POST'])
def get_programs():
    class_section = request.json['class_section']
    program_section = request.json['program_section']
    programs = [p for p in program_details if p['class_section'] == class_section and p['program_section'] == program_section]
    return jsonify(programs)

if __name__ == '__main__':
    app.run(debug=True)