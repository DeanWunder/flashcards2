from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def root():
    
    return render_template('root.html')

@app.route('/json')
def json():
    dictionary = open('cedict_ts.u8', 'r')

    contents = dictionary.readlines()

    dictionary.close()

    jsonOutput = []
    for line in contents:
        if line[0] == '#':
            continue
        lineSplit = line.split(' ')
        jsonObject = {
            'traditional': lineSplit[0],
            'simplified': lineSplit[1],
            'pinyin': lineSplit[2][1:-1],
            'english': line.split('/')[1:-1]
        }
        jsonOutput.append(jsonObject)
        
    return jsonify(jsonOutput)

if __name__ == '__main__':
    app.run(debug = True)
