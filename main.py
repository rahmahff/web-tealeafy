from app.routes.main_routes import main_bp
from flask import Flask

# Pastikan folder template dan static mengarah ke dalam folder 'app'
app = Flask(__name__, 
            template_folder='app/templates', 
            static_folder='app/static')

app.register_blueprint(main_bp)

if __name__ == '__main__':
    print("Aplikasi Tealeafy Berjalan...")
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        use_reloader=False
    )