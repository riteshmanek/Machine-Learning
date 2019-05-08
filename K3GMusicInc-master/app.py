from flask import Flask, render_template, request

import scrapperclassifier
app= Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def get_data():
    if request.method == 'POST':
        # Get Lyrics
        k = int(request.form['k'])
    scr = scrapperclassifier.scrape(k)
    pred_song = scrapperclassifier.song_classifier(scr)
    print(pred_song)
    return render_template('results.html',scr=pred_song)
    
if __name__ == '__main__':
    app.run(debug=True)

