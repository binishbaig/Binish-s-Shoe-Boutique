from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/products')
def products():
    return render_template("products.html")

@app.route('/product/<int:product_id>')
def product(product_id):
    product = [{'id':1, 'name': "Product 1", 'description': "This is the best prodcut ever!",
                'image': "https://www.dropbox.com/sh/ujpqpimyfnvhney/AACZX5QcAVmsTQ2lrgkg5FOGa/christian_purple_pump.jpg"},
               {'id':2, 'name': "Product 2", 'description': "This is the second best prodcut ever!" },
               {'id':3, 'name': "Product 3", 'description': "This is the third best prodcut ever!" },
               {'id':4, 'name': "Product 4", 'description': "This is the fourth best prodcut ever!" },
               {'id':5, 'name': "Product 5", 'description': "This is the fifth best prodcut ever!" },
               {'id':6, 'name': "Product 6", 'description': "This is the sixth best prodcut ever!" },
               {'id':7, 'name': "Product 7", 'description': "This is the seventh best prodcut ever!" },
               {'id':8, 'name': "Product 8", 'description': "This is the eighth best prodcut ever!" },
               {'id':9, 'name': "Product 9", 'description': "This is the ninth best prodcut ever!" },]

    return render_template('product.html', product=product[product_id-1],)


app.run(debug=True)

