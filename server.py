import os
from flask import Flask, render_template, request, jsonify, redirect, url_for, Response
from scraper.scraper import scrape_followers
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        return redirect(url_for('download_following_csv', username=username))
    return render_template('index.html')

@app.route('/download_following_csv/<username>', methods=['GET'])
def download_following_csv(username):
    following = scrape_followers(username)
    csv_data = [['Username']]
    for user in following:
        csv_data.append([user])
    
    # Prepare CSV response
    def generate():
        with open('following.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(csv_data)
        with open('following.csv', 'r') as file:
            yield from file

    return Response(generate(), mimetype='text/csv', headers={
        "Content-disposition": f"attachment; filename=following_{username}.csv"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
