from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# MySQL configuration
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nav@1801",
    database="playlist"
)

# Create a cursor
mycursor = mydb.cursor()

# Create songs table if it doesn't exist
mycursor.execute("CREATE TABLE IF NOT EXISTS songs (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255))")
@app.route('/')
def artistpage():
    return render_template('artistpage.html')

# Route for home page
@app.route('/btsbutter')
def btsbutter():
    return render_template('btsbutter.html', nav_bar=True)

# Route for adding a new song to the songs table
@app.route('/add_song', methods=['POST'])
def add_song():
    # Get data from form
    title = request.form['title']
    
    # Check if song already exists in database
    sql = "SELECT * FROM songs WHERE title = %s"
    val = (title,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    if result:
        return jsonify({'status': 'duplicate'})
    else:
        # Insert data into songs table
        sql = "INSERT INTO songs (title) VALUES (%s)"
        val = (title,)
        mycursor.execute(sql, val)
        mydb.commit()
        return jsonify({'status': 'success'})

# Route for adding a new song to the songs table using song ID
@app.route('/add-to-playlist', methods=['POST'])
def add_to_playlist():
    song_id = request.json['song_id']
    song_name = request.json['song_name']
    # Check if song already exists in database
    sql = "SELECT title FROM songs WHERE id = %s"
    val = (song_id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    if result:
        title = result[0]
    else:
        title = song_name
    # Insert new song into songs table
    if result:
        # Song already in playlist
        return jsonify({'status': 'duplicate'})
    else:
        sql = "INSERT INTO songs (id, title) VALUES (%s, %s)"
        val = (song_id, title)
        mycursor.execute(sql, val)
        mydb.commit()
        return jsonify({'status': 'success'})
@app.route('/playlistpage')
def playlistpage():
    return render_template('playlistpage.html')

@app.route('/api/playlist')
def get_playlist():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nav@1801",
        database="playlist"
    )
    c = conn.cursor()
    c.execute('SELECT id, title FROM songs')
    data = [{'id': row[0], 'title': row[1]} for row in c.fetchall()]
    conn.close()
    return jsonify(data)

@app.route('/api/delete_song', methods=['POST'])
def delete_song():
    song_id = request.form.get('id')
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nav@1801",
        database="playlist"
    )
    c = conn.cursor()
    c.execute('DELETE FROM songs WHERE id = %s', (song_id,))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')
@app.route('/bts')
def btsalbum():
    return render_template('bts.html')
@app.route('/btsdarkandwild')
def btsddark():
    return render_template('btsdarkandwild.html')
@app.route('/aboutpage')
def about():
    return render_template('aboutpage.html')
@app.route('/arijitsingh')
def arijitalbum():
    return render_template('arijitsingh.html')
@app.route('/arijitsinghAASHIQUI2')
def arijitAASHIQUI():
    return render_template('arijitsinghAASHIQUI2.html')
@app.route('/arijitsinghBrahmastra')
def arijitbrahamstra():
    return render_template('arijitsinghBrahmastra.html')
@app.route('/arijitsinghMSD')
def arijitMSD():
    return render_template('arijitsinghMSD.html')
@app.route('/arijitsinghTAMASHA')
def arijitTAMASHA():
    return render_template('arijitsinghTAMASHA.html')
@app.route('/arijitsinghYJHD')
def arijitYJHD():
    return render_template('arijitsinghYJHD.html')
@app.route('/ar_rahman')
def arrahmanalbum():
    return render_template('ar_rahman.html')
@app.route('/ar_rahmanbigil')
def arrahmanbigil():
    return render_template('ar_rahmanbigil.html')
@app.route('/ar_rahmanblue')
def arrahmanblue():
    return render_template('ar_rahmanblue.html')
@app.route('/ar_rahmanlagaan')
def arrahmanlagaan():
    return render_template('ar_rahmanlagaan.html')
@app.route('/ar_rahman_SlumDogMillionaire')
def arrahmanslumdog():
    return render_template('ar_rahman_SlumDogMillionaire.html')
@app.route('/ar_rahman_vande_mataram')
def arrahmanvande():
    return render_template('ar_rahman_vande_mataram.html')
@app.route('/btsbe')
def btsbe():
    return render_template('btsbe.html')
@app.route('/btsmapofthesoulPersona')
def btsmap():
    return render_template('btsmapofthesoulPersona.html')
@app.route('/btsThemostbeautifulmomentinlifePT1')
def btsmost():
    return render_template('btsThemostbeautifulmomentinlifePT1.html')
@app.route('/btswings')
def btswings():
    return render_template('btswings.html')
@app.route('/btsynwa')
def btsynwa():
    return render_template('btsynwa.html')
@app.route('/spotlight')
def spotlight():
    return render_template('spotlight.html')
@app.route('/charlieCHARLIE')
def charlieCHARLIE():
    return render_template('charlieCHARLIE.html')
@app.route('/charlieego')
def charlieego():
    return render_template('charlieego.html')
@app.route('/charlieninetrackmind')
def charlienine():
    return render_template('charlieninetrackmind.html')
@app.route('/charlieputh')
def charlieputh():
    return render_template('charlieputh.html')
@app.route('/charlieTHEOTTOTUNES')
def charlieTHEOTTO():
    return render_template('charlieTHEOTTOTUNES.html')
@app.route('/charlievoicenotes')
def charlienotes():
    return render_template('charlievoicenotes.html')
@app.route('/dualipa')
def dualipaalbum():
    return render_template('dualipa.html')
@app.route('/dualipaCLUBFUTURENOSTALGIA')
def dualipaCLUBNOSTALGIA():
    return render_template('dualipaCLUBFUTURENOSTALGIA.html')
@app.route('/dualipaDUALIPA')
def dualipaDUALIPA():
    return render_template('dualipaDUALIPA.html')
@app.route('/dualipaFUTURENOSTALGIA')
def dualipaNOSTALGIA():
    return render_template('dualipaFUTURENOSTALGIA.html')
@app.route('/dualipaspotifysessions')
def dualipaspotify():
    return render_template('dualipaspotifysessions.html')
@app.route('/dualipaTHEONLYEP')
def dualipaTHEONLYEP():
    return render_template('dualipaTHEONLYEP.html')
@app.route('/searchpage')
def search():
    return render_template('searchpage.html')
if __name__ == '__main__':
    app.run(debug=True)











       
       

        


























