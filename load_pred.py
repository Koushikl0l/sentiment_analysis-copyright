import os
import shutil
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text
#from official.nlp import optimization  # to create AdamW optimizer
tf.get_logger().setLevel('ERROR')
tf.keras.backend.set_floatx('float16')



    
def predict(text):
    saved_model_path='./saved_model'
    reloaded_model = tf.saved_model.load(saved_model_path)
    pred=tf.sigmoid(reloaded_model(tf.constant([str(text)])))
    
    return pred

