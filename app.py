#run this in "flask"(name of virtual enviourment) virtual enviourment
#minimal web app code copied from google
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')#this are endpoint(pages) of our web app
def hello_world():
    # return 'Hello, World!'
    return render_template('index.html')

@app.route('/products')#this is how we make routes to new pages in our web app(website)
def products():
    return "This is the products page"

if __name__=="__main__":
    app.run(debug=True,port=7860)
    #app.run(debug=True,port=7860) used to run our app
    #debug=True means open app in debugging mode so that we can see the errors if occurs
    #port=7860(optional) in this we are expicitly changing the port from default to our choice