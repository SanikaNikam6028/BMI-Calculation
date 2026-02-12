from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def bmi_calculator():
    name = ""
    age = ""
    bmi = ""
    status = ""
    tips = ""
    color = "black"
    error = ""

    if request.method == "POST":
        try:
            name = request.form["name"]
            age = request.form["age"]
            weight = float(request.form["weight"])
            height = float(request.form["height"])

            if height <= 0:
                error = "Height must be greater than 0"
            else:
                bmi = round(weight / (height * height), 2)

                if bmi < 18.5:
                    status = "Underweight"
                    tips = "Eat nutritious food and increase calorie intake."
                    color = "orange"
                elif bmi <= 24.9:
                    status = "Normal"
                    tips = "Great! Maintain your healthy lifestyle."
                    color = "green"
                elif bmi <= 29.9:
                    status = "Overweight"
                    tips = "Do regular exercise and avoid junk food."
                    color = "red"
                else:
                    status = "Obese"
                    tips = "Consult a doctor and follow a proper diet plan."
                    color = "darkred"

        except:
            error = "Please enter valid values."

    return f"""
    <html>
    <head>
        <title>BMI Calculator</title>
        <style>
            body {{
                font-family: Arial;
                background-color: #f2f2f2;
            }}
            .box {{
                width: 320px;
                margin: 80px auto;
                padding: 20px;
                background: white;
                text-align: center;
                border-radius: 10px;
            }}
            input {{
                width: 90%;
                padding: 8px;
                margin: 8px 0;
            }}
            button {{
                padding: 8px 20px;
                background: green;
                color: white;
                border: none;
                cursor: pointer;
            }}
            .reset {{
                background: gray;
            }}
            .error {{
                color: red;
            }}
        </style>
    </head>
    <body>
        <div class="box">
            <h2>BMI Calculator</h2>

            <form method="post">
                <input type="text" name="name" placeholder="Name" required>
                <input type="number" name="age" placeholder="Age" required>
                <input type="number" step="0.1" name="weight" placeholder="Weight (kg)" required>
                <input type="number" step="0.01" name="height" placeholder="Height (meters)" required>

                <button type="submit">Calculate</button>
                <button type="reset" class="reset">Reset</button>
            </form>

            <p class="error">{error}</p>

            <h3>Name: {name}</h3>
            <h3>Age: {age}</h3>
            <h3>BMI: {bmi}</h3>
            <p style="color:{color}; font-weight:bold;">Status: {status}</p>
            <p>{tips}</p>

            <hr>
            <h4>BMI Chart</h4>
            <p>Below 18.5 → Underweight</p>
            <p>18.5 – 24.9 → Normal</p>
            <p>25 – 29.9 → Overweight</p>
            <p>30+ → Obese</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)