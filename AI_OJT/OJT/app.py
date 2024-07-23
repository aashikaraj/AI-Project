from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/destination')
def destination():
    return render_template('destination.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/guides')
def guides():
    return render_template('guides.html')

@app.route('/packages')
def packages():
    return render_template('packages.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

@app.route('/tour')
def tour():
    return render_template('tour.html')

if __name__ == '__main__':
    app.run(debug=True)
