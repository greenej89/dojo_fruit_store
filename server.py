from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry = int(request.form['strawberry'])
    raspberry = int(request.form['raspberry'])
    apple = int(request.form['apple'])
    count = strawberry + raspberry + apple

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    customer_name = f"{first_name} {last_name}" 

    print(f"Charging {customer_name} for {count} fruits")

    # DO NOT RENDER TEMPLATE ON ROUTES WITH POST METHOD AFTER THIS ASSIGNMENT.
    return render_template("checkout.html", strawberry=strawberry, raspberry=raspberry, apple = apple, count = count,
                            first_name = first_name, last_name = last_name, student_id = request.form['student_id'])

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)  
    # app.run(debug=True, port=5001)   #For Mac users who use Google Chrome