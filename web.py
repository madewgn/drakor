from flask import *
from main import *
app = Flask(__name__)

@app.route("/")
def index():
    x = extract_data()
    print(x)
    return render_template("base.html")


@app.route("/<string:end>/", methods=['GET', 'POST'])
def buka(end):
    #return end
    x = extract_article_content(end)
    # if x is not None:
    print(x)
    return render_template("c.html",data=x)
    # else:
    #     return "Article not found or content is empty"

if __name__ == "__main__":
    app.run(debug=True)
