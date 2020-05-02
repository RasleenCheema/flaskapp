from flask import (
    Flask, request, jsonify
)
from settings import db, app
from models import User


@app.route('/create', methods=['POST', 'GET'])
def create_user():
    message = {
        'status': 404,
        'message': 'Something went wrong'
    }
    if request.method == "GET":
        data = User.query.with_entities(
            User.id, User.name,
            User.email, User.mobile_number,
            User.password).all()
        message.update({
            'status': 200,
            'message': 'ALl records are fetched',
            'data': data
        })
    elif request.method == "POST":
        try:

            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('pwd')
            mobile_number = request.form.get('mobile')
            user = User(
                name=name,
                email=email,
                password=password,
                mobile_number=mobile_number
            )
            db.session.add(user)
            db.session.commit()
            message.update({
                'status': 201,
                'message': 'User created successfuly!!! ',
                'user_id': user.id
            })
        except:
            pass
    resp = jsonify(message)
    return resp


@app.route('/update/<int:id>', methods=['PUT'])
def update_user(id):
    message = {
        'status': 404,
        'message': 'user not found'
    }
    try:
        new_name = request.form.get('name', None)
        new_email = request.form.get('email', None)
        new_password = request.form.get('pwd', None)
        new_mobile_number = request.form.get('mobile', None)

        try:
            current_user = User.query.get_or_404(id)
        except:
            return jsonify(message)

        if new_email:
            current_user.email = new_email
        if new_name:
            current_user.name = new_name
        if new_password:
            current_user.password = new_password
        if new_mobile_number:
            current_user.mobile_number = new_mobile_number

        db.session.commit()
        message.update({
            'status': 200,
            'message': 'User details updated successfuly!!! '
        })
    except:
        pass
    resp = jsonify(message)
    return resp


@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    message = {
        'status': 404,
        'message': 'user not found'
    }
    try:
        current_user = User.query.get_or_404(id)
        db.session.delete(current_user)
        db.session.commit()
        message.update({
            'status': 200,
            'message': 'user record delete successfuly!!! '
        })
    except:
        pass
    resp = jsonify(message)
    return resp


@app.route('/detect_pime', methods=['POST'])
def detect_prime_nuber():
    message = {
        'status': 404,
        'message': 'is not prime'
    }
    num = request.form.get('number', None)
    if num is None:
        return jsonify(message)
    f = 0
    for i in range(1000000, int(num / 2) + 1):
        if num % i == 0:
            f = 1
            break
    if f == 0:
        message.update({
            'status': 200,
            'message': 'is prime and greater than 1 million'
        })
    return jsonify(message)


if __name__ == "__main__":
    db.create_all()
    app.run(host="0.0.0.0", debug=True)

