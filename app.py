from flask import Flask, request, render_template
import random
import operator

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo_form.html')
    
@app.route('/froyo_results')
def show_froyo_results():
    context = {
        'users_froyo_flavor': request.args.get('flavor'),
        'users_toppings': request.args.get('toppings')
    }
    return render_template('froyo_results.html', **context)

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
        <form action="/favorites_results" method="GET">
            What's your favorite color?<br/>
            <input type="text" name="color"><br/>
            Whats your favorite animal?<br/>
            <input type="text" name="animal"><br/>
            Whats your favorite city?<br/>
            <input type="text" name="city"><br/>
            <input type="submit" value="Submit!!">
        </form>
    """ 

@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    fav_color = request.args.get("color")
    fav_animal = request.args.get('animal')
    fav_city = request.args.get('city')
    return f'You know in {fav_city} there\'s a lot of {fav_color} {fav_animal}s!'

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
        <form action="/message_results" method="POST">
            Enter a secret message:<br/>
            <input type="text" name='message'><br/>
            <input type='submit' value='submit secret message'>
        </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    user_message = request.form.get('message')
    print(f'user_message: {user_message}')
    scrambled_message = sort_letters(user_message)
    return f'Here\'s your secret message: <br/> {scrambled_message}'

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return """
    <form action="/calculator_results" method="GET">
        Please enter 2 numbers and select an operator.<br/><br/>
        <input type="number" name="operand1">
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="number" name="operand2">
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    ops = {"add": operator.add, "subtract": operator.sub, "multiply": operator.mul, "divide": operator.truediv}
    operation = request.args.get('operation')
    num1 = request.args.get('operand1')
    num2 = request.args.get('operand2')
    result = ops[operation](int(num1),int(num2))
    context = {
        'num1': num1,
        'num2': num2,
        'operation': operation,
        'result': result
    }
    return render_template('calculator_results.html', **context)


# List of compliments to be used in the `compliments_results` route (feel free 
# to add your own!) 
# https://systemagicmotives.com/positive-adjectives.htm
list_of_compliments = [
    'awesome',
    'beatific',
    'blithesome',
    'conscientious',
    'coruscant',
    'erudite',
    'exquisite',
    'fabulous',
    'fantastic',
    'gorgeous',
    'indubitable',
    'ineffable',
    'magnificent',
    'outstanding',
    'propitioius',
    'remarkable',
    'spectacular',
    'splendiferous',
    'stupendous',
    'super',
    'upbeat',
    'wondrous',
    'zoetic'
]

@app.route('/compliments')
def compliments():
    """Shows the user a form to get compliments."""
    return render_template('compliments_form.html')

@app.route('/compliments_results')
def compliments_results():
    """Show the user some compliments."""
    context = {
        # TODO: Enter your context variables here.
    }

    return render_template('compliments_results.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
