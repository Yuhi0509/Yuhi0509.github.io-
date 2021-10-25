from flask import Flask # 載入 Flask
from flask import request # 載入 Resquest 物件
from flask import redirect # 載入 redirect 函式
from flask import render_template #載入 reander template 函式
from flask import session
import json
# 建立 Application 物件，可以設定靜態檔案
app=Flask(
    __name__,
    static_folder="static", #靜態檔案的資料夾名稱
    static_url_path="/static" #靜態檔案對應的網址路徑
    )
app.secret_key="momi" # 設定 Sesion 的密鑰
# 使用 POST 方法，處理路徑 / 的對應函式
@app.route("/")
def index(): # 用來回應路徑 / 的處理函式
    return render_template("index2.html")
#------------------------------------------------------
# 使用 GET 方法處理路徑 /hello,name=使用者的名字
@app.route("/hello")
def hello():
    name=request.args.get("name","")
    secondname=request.args.get("secondname","")
    fullname=name+secondname
    session["username"]=fullname # session["欄位名稱"]=資料
    return render_template("talk.html")
# 使用 GET 方法處理路徑 /talk
@app.route("/talk")
def talk():
    name=session["username"]
    return name+"歡迎光臨"
# 啟動網站伺服器的port
app.run(port=3000)