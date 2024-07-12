from flask import Blueprint, request, jsonify, render_template
import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/student/<reg_no>', methods=['GET'])
def get_student_details(reg_no):
    with open('data/student_details.json') as f:
        students = json.load(f)
    student = next((s for s in students if s['reg_no'] == reg_no), None)
    return jsonify(student)

@main.route('/programs', methods=['GET'])
def get_programs():
    class_section = request.args.get('class_section')
    program_section = request.args.get('program_section')
    with open('data/program_details.json') as f:
        programs = json.load(f)
    filtered_programs = [p for p in programs if p['class_section'] == class_section and p['program_section'] == program_section]
    return jsonify(filtered_programs)
