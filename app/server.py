from flask import Flask, jsonify, request, render_template       #uses flask framework
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'  # Path to SQLite DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Bank Branch model
class BankBranch(db.Model):
    __tablename__ = 'bank_branches'
    ifsc = db.Column(db.String(20), primary_key=True)
    bank_id = db.Column(db.Integer, nullable=False)
    bank_name = db.Column(db.String(100), nullable=False)
    branch = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    city = db.Column(db.String(100))
    district = db.Column(db.String(100))
    state = db.Column(db.String(100))

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Render bank list in HTML table
@app.route('/banks', methods=['GET'])
def get_banks():
    banks = db.session.query(BankBranch.bank_id, BankBranch.bank_name).distinct().all()
    return render_template('bank_list.html', banks=banks)

# Render branch details in HTML table
@app.route('/branches/<string:ifsc>', methods=['GET'])
def get_branch_details(ifsc):
    branch = BankBranch.query.filter_by(ifsc=ifsc).first()
    return render_template('Branch_details.html', branch=branch, ifsc=ifsc)

if __name__ == '__main__':
    app.run(debug=True)
