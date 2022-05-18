from utils import *
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def main_page():
    candidates = get_candidates()
    return render_template('list.html', items=candidates)


@app.route("/candidates/<name>")
def candidate_page(name):
    candidate_info = get_candidate_name(name)
    return render_template('single.html', candidate=candidate_info)


@app.route("/search/<name>")
def search_page(name):
    search_candidates, count = find_candidate_name(name)
    return render_template('search.html', items=search_candidates, count=count)


@app.route("/skill/<skill>")
def search_skill(skill):
    search_candidates_skill, count = find_candidates_skill(skill)
    return render_template('skill.html', items=search_candidates_skill, count=count)


if __name__ == '__main__':
    app.run()
