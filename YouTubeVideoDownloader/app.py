from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('url').strip()
        if 'https://www.youtube.com' in url:
            try:
                flag=True
                yt = YouTube(url)
                stream = yt.streams.first()
                file_path = stream.download()
                return send_file(file_path, as_attachment=True)
            except Exception as e:
                flag=False
                error = 'An error occurred. Please try again.'
                return render_template('index.html', error=error)
            finally:
                try:
                    os.remove(file_path)
                except:
                    pass
                if flag:
                    return render_template('index.html', success='Downloaded successfully.')
        else:
            error = 'Please enter a valid YouTube video URL.'
            return render_template('index.html', error=error)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=False)
