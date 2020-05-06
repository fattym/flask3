from flask import render_template, request, Blueprint
from flask3.models import Post,Comment

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
       
    comments =Comment.query.all()
    return render_template('home.html', posts=posts,comments=comments)


@main.route("/about")
def about():
    return render_template('about.html', title='About')