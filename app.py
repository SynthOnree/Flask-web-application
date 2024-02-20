import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# Request:
# GET /hello?name=David

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name'] # The value is 'David'

    # Send back a friendly greeting with the name
    return f"Hello {name}!"

@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']

    return f"I am waving at {name}"

# To make a request, run:
# curl "http://localhost:5000/hello?name=David"

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"Goodbye {name}!"

@app.route("/Hello_world", methods=['POST'])
def hello_world():
    name = request.form['name']
    message = request.form['message']

    return f"Thanks {name}, you sent this message: {message}"


@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text']
    vowel_count = sum(x in "aeiouAEIOU" for x in text)

    return f'There are {vowel_count} vowels in "{text}"'

@app.route('/sort-names', methods=['POST'])
def sort_names():
    names = request.form['name'].split(',')
    names.sort()
    return ','.join(names)

@app.route('/names', methods=['GET'])
def add_eddie():
    names = ["Julia", "Alice", "Karim"]
    name_to_add = request.args.get('add')
    if name_to_add:
        names.append(name_to_add)
    return ', '.join(names)



# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

