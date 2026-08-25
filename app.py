from flask import Flask,request,jsonify
app=Flask(__name__)

@app.route('/generate',methods=['POST'])
def generate():
    return jsonify({"message": "AI response will be generated here"})

if name=="__main__":
    app.run(debug=True)

