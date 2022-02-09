from flask import Flask, render_template, url_for, request

app = Flask(__name__)

 

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")



@app.route('/result',methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    print(output)
    modelFea = output["modelFea"]
    modelImg = output["modelImg"]
    modelName = output["modelName"]
    modelPrice = output["modelPrice"]
    modelDes = output["modelDes"]
    modelLink = output["modelLink"]


    return render_template('index.html', modelFea = modelFea, modelImg = modelImg, modelName = modelName, modelPrice = modelPrice, modelDes = modelDes, modelLink = modelLink)
    




if __name__ == "__main__":
    app.run(debug=True,port=5001)