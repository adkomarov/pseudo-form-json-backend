from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate-json', methods=['POST'])
def generate_json():
    data = request.json
    form_data = {"форма": []}
    
    for field in data['fields']:
        field_json = {
            f"поле_{field['id']}": {
                "тип": field['type'],
                "зависимость": field['dependency'] or "нет",
                "список_значений": field.get('options', [])
            }
        }
        form_data["форма"].append(field_json)

    return jsonify(form_data)

if __name__ == '__main__':
    app.run(debug=True)
