from flask import Flask, render_template
from post import Post

app = Flask(__name__)

# create a blog object
blog_data = Post()


@app.route('/')
def home():
    return render_template("index.html", data=blog_data.blog())


@app.route('/post/<int:num>')
def get_blog(num):
    return render_template("post.html", data=blog_data.blog(), num=num)


if __name__ == "__main__":
    app.run(debug=True)