from keras.preprocessing import sequence
import numpy
import re
from predict import datas
from keras.backend import clear_session
import pickle
from keras.models import load_model

def load_obj(name):
    with open('/home/sovietspy2/nn_data/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def load_stuff():
    model = load_model("/home/sovietspy2/nn_data/model2.h5")
    max_sentence_length = 200
    vocab_to_int = load_obj('vocab_to_int')
    int_to_languages = load_obj('int_to_languages')
    return (model,max_sentence_length,vocab_to_int,int_to_languages)

def convert_to_int(data, data_int):
    """Converts all our text to integers
    :param data: The text to be converted
    :return: All sentences in ints
    """
    all_items = []
    for sentence in data:
        all_items.append([data_int[word] if word in data_int else data_int["<UNK>"] for word in str(sentence).split()])

    return all_items

def process_sentence(sentence):
    '''Removes all special characters from sentence. It will also strip out
    extra whitespace and makes the string lowercase.
    '''
    return re.sub('[^A-Za-z0-9]+', ' ', sentence).lower().strip()

def predict_sentence(sentence):
    """Converts the text and sends it to the model for classification
    :param sentence: The text to predict
    :return: string - The language of the sentence
    """
    clear_session()

    model, max_sentence_length, vocab_to_int, int_to_languages = load_stuff()

    # Clean the sentence
    sentence = process_sentence(sentence)

    # Transform and pad it before using the model to predict
    x = numpy.array(convert_to_int([sentence], vocab_to_int))
    #print("numpy array: ", x)
    x = sequence.pad_sequences(x, maxlen=max_sentence_length)

    prediction = model.predict(x)

    # Get the highest prediction
    lang_index = numpy.argmax(prediction)

    return int_to_languages[lang_index]
