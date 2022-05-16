from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')       # 路由解析
def index():
    return render_template("index.html")      # 模版渲染



@app.route('/index')
def home():
    # return render_template("index.html")
    return index()



@app.route('/movie')
def movie():
    datalist = []
    conn = sqlite3.connect("movie.db")
    cur = conn.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template("movie.html", movies = datalist)



@app.route('/score')
def score():
    score = []    # 评分
    num = []      # 每个评分所统计出的电影数量
    conn = sqlite3.connect("movie.db")
    cur = conn.cursor()
    sql = "select score, count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])
        num.append(item[1])
    cur.close()
    conn.close()
    return render_template("score.html", score = score, num = num)



@app.route('/word')
def word():
    return render_template("word.html")



@app.route('/team')
def team():
    return render_template("team.html")






if __name__ == '__main__':
    app.run()


#  修改提交后