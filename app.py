from flask import Flask, render_template, request
import RPI.GPIO as GPIO
app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)

#Dictionary called pins that stores the pin number, name and state
pins = {
        3 : {'name' : 'Green LED', 'state' : GPIO.LOW}
}

#Sets each pin as output and low
for pin pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)


@app.route("/")
def main():
        #For each pin, read the pin state and store it in the pins dictionary:
        for pin in pins:
                pins[pin]['state'] = GPIO.input(pin)
        #Put the pin dictionary into the template data dictionary
        templateData = {
                'pins' : pins
        }
        #Pass the template data into the template main.html and return it
        return render_template('main.html', **templateData)


#Function is executed when someone requests a URL with the pin number and action in it
@app.route("/<changePin>/<action>")
def action(changePin, action):
        #Converts the pin from URL into integer
        changePin = int(changePin)
        #Get the device name for the pin being changed
        deviceName = pins[changePin]['name']
        #If the action is ON, execute
        if action == "on":
                GPIO.output(changePin, GPIO.HIGH)
                message = "Turned " + deviceName + " on."
        if action == "off":
                GPIO.output(changePin, GPIO.LOW)
                message = "Turned " + deviceName + " off."
        if action == "toggle":
                #Read the pin and set it to whatever it is not
                GPIO.output(changePin, not GPIO.input(changePin))
                message = "Toggled " + deviceName + "."

        #For each pin, read the state and store it
        for pin in pins:
                pins[pin]['state'] = GPIO.input(pin)

        #Put the pin dictionary and message into templateData dictionary
        templateData = {
                'message' : message,
                'pins' : pins
        }

        return render_template('main.html', **templateData)
                

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
