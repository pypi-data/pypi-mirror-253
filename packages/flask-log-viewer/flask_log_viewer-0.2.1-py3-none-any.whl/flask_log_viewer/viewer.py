from flask import Blueprint, render_template
import time
import os
import random
import pygtail



log_blueprint = Blueprint('flask_log_viewer', __name__, template_folder='templates', static_folder='static')
_base_path = None
_allowed_directories = None
_style_sheet = None



def is_file_in_allowed_directories( file_path):
    absolute_file_path = os.path.abspath(file_path)
    return any(
        os.path.commonpath([absolute_file_path, allowed_dir]) == allowed_dir
        for allowed_dir in _allowed_directories
    )

@log_blueprint.route('/stream_log/<string:log_filename>')
def get(log_filename):
    
    print("log_filename", log_filename)
    
    full_path = os.path.join(_base_path, log_filename)

    if not is_file_in_allowed_directories(full_path):
        return "Access denied: File is not in an allowed directory", 403

    def generate():
        for line in pygtail.Pygtail(full_path):
            yield f"data: {line}\\n \n\n"
            #print(".") # Verify that the generator stops when the client disconnects
            
    def random_log():
        import random
        while True:
            sentence = generate_sentence(pig_latin_words, length=7)

            yield f"data: {sentence} \n\n"
            time.sleep(1)

    if log_filename == "random.log":
        return random_log(), {"Content-Type":'text/event-stream'}
    else:
        return generate(), {"Content-Type":'text/event-stream'}
    


@log_blueprint.route('/view/')
@log_blueprint.route('/view/<string:log_filename>')
def viewer(log_filename='random.log'):
    return render_template('viewer.html', log_file=log_filename, style_sheet=_style_sheet)



def log_viewer_blueprint(base_path, allowed_directories):    
    global _base_path, _allowed_directories
    _base_path=base_path
    _allowed_directories=allowed_directories
    return log_blueprint




def pig_latin(word):
    if word[0] in 'aeiou':
        return word + 'way'
    else:
        for i in range(len(word)):
            if word[i] in 'aeiou':
                return word[i:] + word[:i] + 'ay'
        return word + 'ay'  # For words without vowels

def generate_sentence(word_list, length=5):
    return ' '.join(random.choice(word_list) for _ in range(length))

# For demo purposes
english_words = ["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit"]
pig_latin_words = [pig_latin(word) for word in english_words]
