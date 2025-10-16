from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ---------------------------------------------
# DATASET (Blocks + Classes)
# ---------------------------------------------
blocks = {
    "Learning Centre 1": {"total_classrooms": 3, "students": []},
    "Learning Centre 2": {"total_classrooms": 3, "students": []},
    "Kalataranga": {"total_classrooms": 3, "students": []},
    "Alliance School of Applied Engineering": {"total_classrooms": 3, "students": []},
    "Alliance School of Law": {"total_classrooms": 3, "students": []},
}

# ---------------------------------------------
# FUNCTION: Assign class automatically
# ---------------------------------------------
def assign_class(block_name):
    count = len(blocks[block_name]["students"])
    if count < 50:
        return "A"
    elif count < 100:
        return "B"
    else:
        return "C"

# ---------------------------------------------
# HOME PAGE
# ---------------------------------------------
@app.route('/')
def index():
    return render_template('index.html', blocks=blocks)

# ---------------------------------------------
# ADD STUDENT ROUTE
# ---------------------------------------------
@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form['name']
    course = request.form['course']
    block_name = request.form['block']

    class_name = assign_class(block_name)
    blocks[block_name]["students"].append({
        "name": name,
        "course": course,
        "class": class_name
    })

    return redirect(url_for('index'))

# ---------------------------------------------
# VIEW STUDENTS IN A BLOCK
# ---------------------------------------------
@app.route('/view/<block_name>')
def view_block(block_name):
    block = blocks.get(block_name, {})
    return render_template('view.html', block_name=block_name, students=block.get("students", []))

# ---------------------------------------------
# RUN APP
# ---------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
