#!/usr/bin/env python3
from flask import Flask, render_template, request
from common import process_bill


app = Flask(__name__)

# Uncomment to make the server refresh the website
# as soon as there is a change in the source code.
app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        bill_input = request.form["bill_input"]
        bill_lines = bill_input.split("\n")
        bill_lines = [line.strip() for line in bill_lines]
        try:
            entity_vs_amount = process_bill(bill_lines)
            total_amount = sum(entity_vs_amount.values())
            output = str(entity_vs_amount) + \
                "\n\nTotal amount = {}".format(total_amount)
        except Exception as e:
            output = "Error while processing input:\n\n---- start ----\n{}\n---- end ----\n\n{}".format(
                bill_input, e)
        return render_template("index.html", bill_input=bill_input, output=output)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run()
