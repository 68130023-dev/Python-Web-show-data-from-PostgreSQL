from flask import Flask, render_template
import psycopg2

host = "localhost"
port = "5432"
database = "movie"
user = "postgres"
password = "0336"

app = Flask(__name__)

# -----------------------
# ส่วนตั้งค่าการเชื่อมต่อ Database
# -----------------------
def get_db_connection():
    conn = psycopg2.connect(
        
        host=host,
        port=port,
        database=database,
        user=user,
        password=password

        #host="localhost",      # ถ้าใช้เครื่องตัวเองให้เป็น localhost
        #database="movie_db",   # ชื่อ database ที่สร้างใน pgAdmin
        #user="postgres",       # ชื่อ user (เช่น postgres)
        #password="0336",  # รหัสผ่านของ postgres
        #port="5432"            # port ปกติของ PostgreSQL
    )
    return conn

# -----------------------
# Route หน้าแรก "/"
# -----------------------
@app.route("/")
def index():
    student_name = "Yuttana Emyong"     # เปลี่ยนเป็นชื่อจริงของนักศึกษา
    student_id = "68130023"           # เปลี่ยนเป็นรหัสนักศึกษา
    return render_template("index.html",
                           student_name=student_name,
                           student_id=student_id)

# -----------------------
# Route "/movie" สำหรับแสดงตารางหนัง
# -----------------------
@app.route("/movie")
def movie_list():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT mid, m_name, release_date, genre, country FROM movies ORDER BY mid;")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    # rows จะเป็น list ของ tuple เช่น [(1,'Men in Black', ...), (...)]
    return render_template("movie.html", movies=rows)

# -----------------------
# Run App
# -----------------------
if __name__ == "__main__":
    app.run(debug=True)
