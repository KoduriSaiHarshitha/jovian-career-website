from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  "id": 1,
  "title": "Data Analyst",
  "location": "Bengaluru,IN",
  "salary": 'Rs.1000000'
}, {
  "id": 2,
  "title": "Data Scientist",
  "location": "Hyderabad,IN",
  "salary": 'Rs.1500000'
}, {
  "id": 3,
  "title": "Front-End Developer",
  "location": "Chennai,IN",
  "salary": 'Rs.9000000'
}, {
  "id": 4,
  "title": "Back-End Developer",
  "location": "Remote"
}]


@app.route("/")
def hello_jovian():
  return render_template('home.html', jobs=JOBS, company_name="Jovian Careers")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
