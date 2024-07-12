from flask import Flask
from app.routes import main

app = Flask(__name__)

@app.route('/student/<reg_no>', methods=['GET'])
def get_student_details(reg_no):
    with open('student_details.json') as f:
        students = json.load(f)
    student = next((s for s in students if s['reg_no'] == reg_no), None)
    return jsonify(student)

@app.route('/programs', methods=['GET'])
def get_programs():
    class_section = request.args.get('class_section')
    program_section = request.args.get('program_section')
    with open('program_details.json') as f:
        programs = json.load(f)
    filtered_programs = [p for p in programs if p['class_section'] == class_section and p['program_section'] == program_section]
    return jsonify(filtered_programs)

if __name__ == '__main__':
    app.run(debug=True)
