from flask import Flask, render_template, request

app = Flask(__name__)

def get_current_page():
    return request.endpoint

@app.route('/')
def home():
    return render_template('index.html', current_page=get_current_page())

@app.route('/about')
def about():
    return render_template('about.html', current_page=get_current_page())

@app.route('/booking')
def booking():
    return render_template('booking.html', current_page=get_current_page())

@app.route('/contact')
def contact():
    return render_template('contact.html', current_page=get_current_page())

@app.route('/destination')
def destination():
    return render_template('destination.html', current_page=get_current_page())

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', current_page=get_current_page())

@app.route('/guides')
def guides():
    return render_template('guides.html', current_page=get_current_page())

@app.route('/packages')
def packages():
    return render_template('packages.html', current_page=get_current_page())

@app.route('/services')
def services():
    return render_template('services.html', current_page=get_current_page())

@app.route('/success')
def success():
    return render_template('success.html', current_page=get_current_page())

@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html', current_page=get_current_page())

@app.route('/tour')
def tour():
    return render_template('tour.html', current_page=get_current_page())

if __name__ == '__main__':
    app.run(debug=True)
