from flask import Flask

app = Flask(__name__)

# Memberes Api Route

# this will be removed and  replaced with the real backend code of the project at a later date

@app.route("/members")
def members():
    return {"memberes": ["Member1", "Member2","Member3"]}


if __name__ == "__main__":
    app.run(debug=True)
