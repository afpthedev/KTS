from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Örnek veri - gerçek uygulamada bu veri bir veritabanından gelebilir
    kurban_durumu = {
        'asamalar': [
            {'ad': 'Kurban İsteğiniz Alındı', 'tamamlandi': True},
            {'ad': 'Kurban Kesime Hazırlanıyor', 'tamamlandi': True},
            {'ad': 'Kesildi', 'tamamlandi': False}
        ],
        'alici': 'ALT KAT BORAN TEL CEVAPSIZ'
    }
    return render_template('index.html', kurban_durumu=kurban_durumu)

if __name__ == '__main__':
    app.run(debug=True)