from flask import Flask, render_template, request, jsonify
import commands

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def server():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        msg = request.form['message']
        response = ""
        #not a command
        if msg.find('!') == -1:
            msg = msg.lower()
            if msg.find('thank') != -1:
                return 'No need to thank me, I am built to serve you!'
            elif msg.find('hate') != -1:
                return 'Why the hate :('
            elif msg.find('love') != -1:
                return 'I love you too; now I need to get back to work!'
            elif msg.find('problem') != -1:
                return 'If you have an issue, please use the !help command'
            else:
                return jsonify(message='Please enter a command. Enter !help if you want a list of commands')
        else:#is a command
            parse = msg.split(' ', 1)
            command = parse[0]
            args = ''
            if len(parse) > 1:
                args = parse[1]
            if command == '!calc':
                return jsonify(message=commands.calc(args))
            elif command == '!help':
                return commands.help()
            elif command == '!xkcd':
                return jsonify(message=commands.xkcd(args))
            else:
                return jsonify(message='Sorry, that command is invalid')
