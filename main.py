from flask import Flask, request, render_template
import mysql.connector
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('customer.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        # 获取输入的 productName 值
        productName = request.form['productName']
        # 连接 MySQL 数据库
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="massage"
        )
        mycursor = mydb.cursor()
        # 使用 MySQL LIKE 运算符进行模糊搜索，并获取所有匹配结果
        sql = "SELECT * FROM product WHERE productName LIKE '%{}%'".format(productName)
        mycursor.execute(sql)
        results = mycursor.fetchall()
        return render_template('results.html', results=results)
    else:
        return "Invalid request method. Please use POST."
@app.route('/customer')
def customer():
    return render_template('customer.html')

@app.route('/purchase')
def purchase():
    return render_template('purchase.html')

@app.route('/marketing')
def marketing():
    return render_template('marketing.html')

@app.route('/sales')
def sales():
    return render_template('sales.html')

@app.route('/kpi')
def kpi():
    return render_template('kpi.html')

@app.route('/chart')         #折線圖
def chart():
    # 连接到 MySQL 数据库
    cnx = mysql.connector.connect(user='root', password='1234',
                                  host='localhost', database='massage')
    cursor = cnx.cursor()

    # 准备查询
    query = "SELECT semester, orderNum FROM `order`"

    # 执行查询
    cursor.execute(query)

    # 提取结果
    results = cursor.fetchall()

    # 关闭连接
    cursor.close()
    cnx.close()
if __name__ == '__main__':
    app.run(debug=True)
