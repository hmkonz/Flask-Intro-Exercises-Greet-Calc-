from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# Part One

@app.route('/add')
def add_parameters():
    """Add a and b parameters"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = add(a, b)

    return str(result)

@app.route('/sub')
def subtract_parameters():
    """Subtract a and b parameters"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = sub(a, b) 
   
    return str(result)

@app.route('/mult')
def multiply_parameters():
    """Multiply a and b parameters"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = mult(a, b) 
   
    return str(result)

@app.route('/div')
def divide_parameters():
    """Multiply a and b parameters"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = div(a, b) 
   
    return str(result)

OPERATORS = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

# Part Two

@app.route('/math/<operator_name>')
def math_operations(operator_name):
    """Performs math operation in operators.py file depending on operator_name"""
    operation = OPERATORS[operator_name]
    a = int(request.args['a'])
    b = int(request.args['b'])

    result = operation(a, b)
    return str (result)


    