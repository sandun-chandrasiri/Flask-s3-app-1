from flask import Flask, request, render_template, redirect 
import boto3

app = Flask(__name__)

@app.route("/") 
def index():
    return render_template("index.html")

@app.route("/create-bucket", methods=['POST'])
def create_bucket():
    bucket_name = request.form["bucket_name"]
    #s3 = boto3.resource('s3')
    #bucket = s3.create_bucket(Bucket=bucket_name)
    #above commented and the below 2 lines of codes should
    #be checked again and confirmed whether which 2 lines work. 
    client = boto3.client("s3")
    client.create_bucket(Bucket=bucket_name)
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True,port=8080,host='0.0.0.0')
