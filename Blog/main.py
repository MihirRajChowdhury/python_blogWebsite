from flask import Flask,render_template
import requests
app = Flask(__name__)

res = requests.get("https://api.npoint.io/4765302cbf53820839c5")

data = res.json()




@app.route("/")
def get_home():
    return render_template("index.html",data=data)
@app.route("/about")
def get_about():
    return render_template("about.html")

@app.route("/contact")
def get_contact():
    return render_template("contact.html")

@app.route("/post")
def get_post():
    return render_template("samplePost.html")

@app.route("/show_post/<int:id>")
def show_post(id):
    request_post = None
    print(id)
    for post in data:
        if post["id"] == id:
            request_post = post
    return render_template("post.html",post=request_post)


if __name__ =="__main__":
    app.run(debug=True)



