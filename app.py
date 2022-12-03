from math import sin, cos, tan, sqrt,exp, log, acosh,asinh,asin, acos, atanh
from flask import Flask, render_template, url_for, request

app = Flask(__name__)


# route == link == url

# main route
@app.route("/")
def main():
    return render_template("index.html", home=True)

@app.route("/advanced")
def advanced():
    return render_template("advanced.html")

@app.route("/simple")
def simple():
    return render_template("simple.html")

@app.route("/carbon")
def carbon_emissions():
    return render_template("carbon_emissions.html")

@app.route("/calculate", methods=["post"])
def calculate():
    first_number = int(request.form["firstNumber"])
    operation = request.form["operation"]
    second_number = int(request.form["secondNumber"])
    note = ""
    color = "alert-success"
    if operation == "plus":
        result = first_number + second_number
        note = "Addition was performed successfully"
    elif operation == "minus":
        result = first_number - second_number
        note = "Subtraction was performed successfully"
    elif operation == "multiply":
        result = first_number * second_number
        note = "Multiplication was performed successfully"
    elif operation == "divide":
        result = first_number / second_number
        note = "Division was performed successfully"
    else:
        note = "This is an error, please try again"
        color = "alert-danger"
        return render_template("simple.html", note=note,color=color)
    return render_template("simple.html", result=result, note=note,color = color)

@app.route("/calculate_advanced", methods=["post"])
def calculate_advanced():
    first_number = int(request.form["firstNumber"])
    operation = request.form["operation"]
    note = ""
    color = "alert-success"
    try:
        if operation == "sin":
            result = sin(first_number)
            note = "Sine was performed successfully"
        elif operation == "cos":
            result = cos(first_number)
            note = "Cosine was performed successfully"
        elif operation == "tan":
            result = tan(first_number)
            note = "Tangent was performed successfully"
        elif operation == "squr":
            result = sqrt(first_number)
            note = "Square root was performed successfully"
        elif operation == "log":
            result = log(first_number)
            note = "Log was performed successfully"
        elif operation == "exp":
            result = exp(first_number)
            note = "exp was performed successfully"
        elif operation == "asinh":
            result = asinh(first_number)
            note = "Asinh was performed successfully"
        elif operation == "acosh":
            result = acosh(first_number)
            note = "Acosh was performed successfully"
        elif operation == "atanh":
            result = atanh(first_number)
            note = "Atanh was performed successfully"
        elif operation == "asin":
            result = asin(first_number)
            note = "Asin was performed successfully"
        elif operation == "acos":
            result = acos(first_number)
            note = "Acos was performed successfully"
        else:
            color = "alert-danger"
            note = "This is an error, please try again"
            return render_template("advanced.html", note=note, color=color)
    except ValueError:
        return render_template("advanced.html", result=0, color="alert-warning", note="Math error!")

    return render_template("advanced.html", result=result, color=color, note=note)


@app.route("/carbon_calculate", methods=["post"])
def carbon_calculate():

    # import ipdb;ipdb.set_trace()
    try:
        color = "alert-success"
        c=0
        kg=0
        # if request.form.get('action')  == "Calculate1":
        fertilizer = request.form["fertilizer"]
        plant = request.form["plant"]
        soil = request.form["soil"]
        post = request.form["post"]
        transport = request.form["transport"]
        weight = request.form["weight"]

        def yes_no(name):
            if name == "yes":
                name = 1
            else:
                name = 0
            return name

        fertilizer = yes_no(fertilizer)
        plant = yes_no(plant)
        soil = yes_no(soil)
        post = yes_no(post)

        c += 0.132 * fertilizer
        c += 0.028 * plant
        c += 0.03 * soil
        c += 0.033 * post
        c += 0.237*(0.2*0.37 + 0.8*0.167)*0.17 # energy for spray (0.2) and drip (0.8) irragation; 0.17kg co2e in spain 2021 
        c += 0.00015 * float(transport)
        kg = float(weight)


        # vertical farming
        c2=0
        kg2=0
        # if request.form.get('action') == "Calculate2":
        fl = float(request.form["vf_fertilizer"])
        pl = float(request.form["vf_plant"])
        sm = float(request.form["vf_soil"])
        pc = float(request.form["vf_ph"])
        bm = float(request.form["vf_bm"])
        he =float(request.form.get("vf_heat"))
        li =float(request.form["vf_light"])
        wa =float(request.form["vf_water"])
        tr = float(request.form["vf_transport"])
        kg2 = float(request.form["vf_weight"])

        c2 = 0
        c2 += 0.023 * fl/100
        c2 += 0.028 * pl/100
        c2 += 0.157 * sm/100
        c2 += 0.091 * pc/100
        c2 += 0.007 * bm/100
        c2 += 0.49*he
        c2 += 0.05*li
        c2 += 0.59/1000*wa
        # c2 += 0.15 *tr

        total=c2*kg2+0.15 *tr
            
        note1 = (f"The carbon emission of 1kg of lettuce: {c:.5f}\nThe overall carbon emissions: {c*kg:.5f}.\n\n"
            f"The fertilizer you have chosen: " + request.form["fertilizer"] + " .\r\n" 
            f"The plant you have chosen: " + request.form["plant"] +" .\r\n" 
            f"The soil you have chosen: " + request.form["soil"] +" .\r\n" 
            f"The post you have chosen: " + request.form["post"] +" .\r\n"
            )  

        note2 = f"The carbon emission of 1kg of lettuce: {total/kg2:.5f}\nThe overall carbon emissions: {total:.5f}.\n" 

    except ValueError:
        return render_template("carbon_emissions.html", result1=0, result2=0, color="alert-warning", note="Math error!")

    return render_template("carbon_emissions.html", result1="{:.8f}".format(c), result2="{:.8f}".format(c2), note1=note1, note2=note2, color=color)


if __name__ == '__main__':
    app.run(debug=True)

