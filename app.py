from flask import Flask, render_template, request
from my_stack_array import Stack

app = Flask(__name__)

stack = Stack()


@app.route("/")
def home():
    return render_template(
        "index.html",
        data=stack.data,
        top=stack.top
    )


@app.route("/push", methods=["POST"])
def push():

    value = int(request.form["value"])

    stack.push(value)

    return render_template(
        "index.html",
        data=stack.data,
        top=stack.top,
        message=f"Pushed {value}"
    )


@app.route("/pop", methods=["POST"])
def pop():

    try:
        value = stack.pop()

        return render_template(
            "index.html",
            data=stack.data,
            top=stack.top,
            message=f"Popped {value}"
        )

    except IndexError:

        return render_template(
            "index.html",
            data=stack.data,
            top=stack.top,
            message="🛑 STOP! The stack is empty! There is literally NOTHING to pop out 😂"
        )


@app.route("/peek", methods=["POST"])
def peek():

    try:
        value = stack.peek()

        return render_template(
            "index.html",
            data=stack.data,
            top=stack.top,
            message=f"Top element is {value}"
        )

    except IndexError as e:

        return render_template(
            "index.html",
            data=stack.data,
            top=stack.top,
            message=str(e)
        )


if __name__ == "__main__":
    app.run(debug=False)