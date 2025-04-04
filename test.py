import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""  # Default output

    if request.method == "POST":
        code = request.form["code"]  # Get Python code from form
        user_input = request.form.get("user_input", "")  # Get user input from form

        try:
            # Run the code using subprocess.Popen to support input
            process = subprocess.Popen(
                [r"C:\Python313\python.exe", "-c", code],  # Change to your Python path
                text=True,
                stdin=subprocess.PIPE,  # Enable input
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            # Send user input and capture output
            output, error = process.communicate(input=user_input, timeout=5)

            output = output if output else error  # Show output or error

        except subprocess.TimeoutExpired:
            output = "Error: Execution timed out."

        except Exception as e:
            output = f"Error: {str(e)}"

    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)
