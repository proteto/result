document.getElementById('class-section').addEventListener('change', fetchPrograms);
document.getElementById('program-section').addEventListener('change', fetchPrograms);
document.getElementById('add-entry').addEventListener('click', addEntry);

async function fetchPrograms() {
    const classSection = document.getElementById('class-section').value;
    const programSection = document.getElementById('program-section').value;
    const response = await fetch(`/programs?class_section=${classSection}&program_section=${programSection}`);
    const programs = await response.json();
    const programSelect = document.getElementById('program');
    programSelect.innerHTML = programs.map(p => `<option value="${p.program_id}">${p.name}</option>`).join('');
}

document.getElementById('result-form').addEventListener('input', async function(e) {
    if (e.target.id === 'reg-no') {
        const regNo = e.target.value;
        const response = await fetch(`/student/${regNo}`);
        const student = await response.json();
        if (student) {
            e.target.nextElementSibling.textContent = `Name: ${student.name}`;
            e.target.nextElementSibling.nextElementSibling.textContent = `Team: ${student.team}`;
        }
    }
});

function addEntry() {
    const newEntry = document.querySelector('.entry').cloneNode(true);
    document.getElementById('entries').appendChild(newEntry);
}

document.getElementById('result-form').addEventListener('submit', function(e) {
    e.preventDefault();
    // Handle form submission
});
