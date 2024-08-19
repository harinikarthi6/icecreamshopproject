import pickle
from flask import Flask,render_template,request
app=Flask(__name__)
model=pickle.load(open("model.pkl","rb"))
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/predict",methods=["GET","POST"])
def predict():
    prediction=model.predict([[float(request.form.get("temperature"))]])
    #prediction=model.predict([[28]])
    output=round(prediction[0],2)
    
    return render_template("index.html", prediction_text=f"Total revenue generated is Rs.{output}/-")
# for error backup
if __name__=="__main__":
    app.run(debug=True)