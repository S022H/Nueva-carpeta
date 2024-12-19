from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template para reproducir el video
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reproductor de Video</title>
</head>
<body>
    <h1>Reproductor de Video</h1>
    <form method="POST">
        <input type="text" name="video_url" placeholder="Ingrese la URL del video" required>
        <button type="submit">Reproducir</button>
    </form>
    {% if video_url %}
    <div>
        <h2>Video:</h2>
        <iframe width="560" height="315" src="{{ video_url }}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    </div>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    video_url = None
    if request.method == 'POST':
        url = request.form['video_url']
        if 'youtube.com' in url:
            video_id = url.split('v=')[1]
            video_url = f'https://www.youtube.com/embed/{video_id}'
        else:
            video_url = url
    return render_template_string(html_template, video_url=video_url)

if __name__ == '__main__':
    app.run(debug=True)
    
#entrada es http://127.0.0.1/
