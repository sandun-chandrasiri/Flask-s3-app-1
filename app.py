from flask import Flask, request, render_template, redirect 
import boto3

app = Flask(__name__)

@app.route("/") 
def index():
    return render_template("index.html")

@app.route("/create-bucket", methods=['POST'])
def create_bucket():
    bucket_name = request.form["bucket_name"]
    s3 = boto3.resource('s3')
    bucket = s3.create_bucket(Bucket=bucket_name)
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True,port=8080,host='0.0.0.0')
