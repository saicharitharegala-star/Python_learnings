from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def register():
    """Show the registration form and handle its submission."""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        city = request.form.get("city", "").strip()
        phone = request.form.get("phone", "").strip()

        if not name or not city or not phone:
            return render_template(
                "registration.html",
                error="Please complete all fields.",
                form_data={"name": name, "city": city, "phone": phone},
            )

        return render_template("confirmation.html", name=name, city=city, phone=phone)

    return render_template("registration.html", form_data={})


if __name__ == "__main__":
    app.run(debug=True)
