from flask import Flask, render_template, request

app = Flask(__name__)

# Morse code dictionaries (moved to top level so both functions can access if needed)
MORSE_CODE_DICT = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
    "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
    "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
    ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
    "--..": "Z",
    "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
    ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",
    "/": " ", " ": " "  # Handle word spacing
}

MORSE_CODE_REVERSED = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    " ": "/"  # Use '/' to represent space between words in Morse
}

def morse_to_english(morse_code):
    output = ""
    words = morse_code.split(" ")
    for word in words:
        if word in MORSE_CODE_DICT:
            output += MORSE_CODE_DICT[word]
        else:
            output += " "
    return output.strip()

def english_to_morse(english_text):
    output = []
    for char in english_text.upper():
        if char in MORSE_CODE_REVERSED:
            output.append(MORSE_CODE_REVERSED[char])
        else:
            output.append(char)
    return " ".join(output)

@app.route('/', methods=['GET', 'POST'])
def index():
    morse_result = ""
    english_result = ""
    
    if request.method == 'POST':
        if 'morse_submit' in request.form:
            morse_input = request.form['morse_code']
            morse_result = morse_to_english(morse_input)
        elif 'english_submit' in request.form:
            english_input = request.form['english_text']
            english_result = english_to_morse(english_input)
    
    return render_template('index.html', 
                         morse_result=morse_result,
                         english_result=english_result)

if __name__ == '__main__':
    app.run(debug=True)