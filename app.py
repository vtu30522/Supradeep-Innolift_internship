from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = [
    {
        "name": "Rahul",
        "course": "Python",
        "gender": "Male"
    },
    {
        "name": "Priya",
        "course": "Java",
        "gender": "Female"
    }
]


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name")
        course = request.form.get("course")
        gender = request.form.get("gender")

        students.append(
            {
                "name": name,
                "course": course,
                "gender": gender
            }
        )

        return redirect("/students")

    return render_template("register.html")


@app.route("/students")
def students_page():
    return render_template(
        "students.html",
        students=students
    )


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)