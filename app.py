from flask import Flask,request,render_template,redirect
from dotenv import load_dotenv

try:
   load_dotenv()
except Exception as e:
   print(".env noot available\n")
   print(f"Error:{e}")

app = Flask(__name__)

@app.route("/")
def home():
   return render_template("index.html")

if __name__ == "__main__":
   app.run(debug = True,port = 3000)