from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    kurban_durumu = {
        'asamalar': [
            {'ad': 'İstek Alındı', 'tamamlandi': True, 'icon': 'clipboard-check'},
            {'ad': 'Kesime Hazır', 'tamamlandi': True, 'icon': 'tasks'},
            {'ad': 'Kesildi', 'tamamlandi': False, 'icon': 'cut'},
            {'ad': 'Teslim Edildi', 'tamamlandi': False, 'icon': 'truck'}
        ],
        'tamamlanan': 2,
        'toplam': 4,
        'alici': 'ALT KAT BORAN TEL CEVAPSIZ',
        'adres': 'Örnek Mahallesi, Kurban Sokak No:123, Şehir/İlçe'
    }
    return render_template('index.html', kurban_durumu=kurban_durumu)

if __name__ == '__main__':
    app.run(debug=True)