from flask import Flask, jsonify                            # used the flask framework
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)                                        # creates the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'  # database path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Represents the table : bank_branches
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

# GET all the distinct banks
@app.route('/banks', methods=['GET'])
def get_banks():
    banks = db.session.query(BankBranch.bank_id, BankBranch.bank_name).distinct().all()
    return jsonify([
        {'bank_id': bank.bank_id, 'bank_name': bank.bank_name}                                     # Returns in json format
        for bank in banks
    ])

# GET branch details by IFSC
@app.route('/branches/<string:ifsc>', methods=['GET'])
def get_branch_details(ifsc):
    branch = BankBranch.query.filter_by(ifsc=ifsc).first()
    if branch:
        return jsonify({
            'ifsc': branch.ifsc,
            'bank_id': branch.bank_id,
            'bank_name': branch.bank_name,
            'branch': branch.branch,
            'address': branch.address,
            'city': branch.city,
            'district': branch.district,
            'state': branch.state                                                 # Returns in json format
        })
    return jsonify({'error': 'Branch not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
