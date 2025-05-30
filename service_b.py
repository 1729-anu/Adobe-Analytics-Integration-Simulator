from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize database to store incoming analytics data
def init_db():
    conn = sqlite3.connect('analytics_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            metric TEXT,
            value INTEGER,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Endpoint to receive data from Service A
@app.route('/receive-data', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()
        source = data.get('source')
        metric = data.get('metric')
        value = data.get('value')
        timestamp = data.get('timestamp')

        # Store the data in the SQLite database
        conn = sqlite3.connect('analytics_data.db')
        c = conn.cursor()
        c.execute('INSERT INTO logs (source, metric, value, timestamp) VALUES (?, ?, ?, ?)',
                  (source, metric, value, timestamp))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Data received and stored successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(port=5001)