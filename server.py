from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

#THIS WILL MOVE LOCATIONS LATER -- (controller file)
@app.route('/play')
@app.route('/play/<int:number>')
@app.route('/play/<color>')
@app.route('/play/<int:number>/<color>')          # The "@" decorator associates this route with the function immediately following
@app.route('/play/<color>/<int:number>')          # The "@" decorator associates this route with the function immediately following
def squares(number = 3, color = "aqua"):
    return render_template('index.html', color=color, number=number)  # Return the string 'Hello World!' as a response

# def defaultsquares2():
#     number = 3
#     color = "aqua"
#     return render_template('index.html', color=color, number=number)  # Return the string 'Hello World!' as a response

# def defaultsquares(number):
#     color = "aqua"
#     return render_template('index.html', color=color, number=number)  # Return the string 'Hello World!' as a response

#This is always at the bottom!
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

