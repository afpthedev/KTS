from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    kurban_durumu = {
        'asamalar': [
            {'ad': 'Gönderi Alındı', 'tamamlandi': True},
            {'ad': 'Transfer Sürecinde', 'tamamlandi': True},
            {'ad': 'Dağıtıma Çıktı', 'tamamlandi': True},
            {'ad': 'Teslim Edildi', 'tamamlandi': False}
        ],
        'alici': 'ALT KAT BORAN TEL CEVAPSIZ',
        'adres': 'Örnek Mahallesi, Kurban Sokak No:123, Şehir/İlçe'
    }
    return render_template('index.html', kurban_durumu=kurban_durumu)

if __name__ == '__main__':
    app.run(debug=True)