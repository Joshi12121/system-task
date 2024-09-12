from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory storage for products
products = []

@app.route('/')
def index():
    return render_template('page1.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/add-products', methods=['POST'])
def add_products():
    global products
    data = request.json
    new_products = data.get('products', [])
    
    for product in new_products:
        # Check if product already exists
        if not any(p['sku'] == product['sku'] for p in products):
            products.append(product)
    
    return jsonify({"status": "success", "products": products})

@app.route('/get-products', methods=['GET'])
def get_products():
    return jsonify({"products": products})

if __name__ == '__main__':
    app.run(debug=True)
