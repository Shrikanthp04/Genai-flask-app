import sqlite3, os, json
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai
from table_info import table_definitions
from flask import Flask, render_template, request

load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))

def get_gemini_model(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([question])
    return response.text

def read_sql_query(query, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST', 'GET'])
def run():
    OUTPUT_DIR = "Output"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    if request.method == 'POST':
        user_text = request.form['userInput'].strip()
        
        prompt = "Give only the exact SQL query without any explanations, etc. queries must be sqlite3 only."
        
        input_text = f"{user_text}, {prompt}\n\n" + '\n'.join([table["definition"] for table in table_definitions])
        
        response = get_gemini_model(input_text)
        sql_query = response[6:-3]
        
        data = read_sql_query(query=sql_query, db='Sales.db')
        json_data = {"sql_query": sql_query, "database_result": data}
        
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        output_file = f'Output/result_{timestamp}.json'
        
        with open(output_file, 'w') as file:
            json.dump(json_data, file)
       
    return render_template('results.html', user_input_text=user_text, sql_query_by_llm=sql_query, db_result=data, json_data=json_data)


if __name__=='__main__':
    app.run(host='0.0.0.0' ,port=4000, debug=True)
