from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

API_KEY = 'enochkung'

# Temporary in-memory storage
storage = {}

@app.route('/api/submit', methods=['POST'])
def submit_xml():
    try:
        api_key = request.headers.get('Authorization')
        if not api_key or api_key != f'Bearer {API_KEY}':
            return jsonify({'status': 'error', 'message': 'Unauthorized'}), 401
        xml_data = request.data.decode('utf-8')
        record_id = str(len(storage) + 1)
        storage[record_id] = xml_data
        print('record_id', record_id)
        return jsonify({'status': 'success', 'id': record_id, 'data': xml_data}), 201
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/api/records/<record_id>', methods=['GET'])
def get_record(record_id):
    try:
        xml_data = storage.get(record_id)
        if xml_data:
            return jsonify({'status': 'success', 'id': record_id, 'data': xml_data}), 200
        else:
            return jsonify({'status': 'error', 'message': 'Record not found'}), 404
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400
    

@app.route('/')
def serve_html():
    return send_file('sample.html')


if __name__ == '__main__':
    app.run(debug=True)
