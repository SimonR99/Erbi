import tensorflow as tf
import argparse
import pickle
import sys
print(sys.path)
from .transformers.model import transformer
from chatbot.transformers.dataset import get_dataset, preprocess_sentence
class Chatbot:
    def __init__(self):
        self.loaded_model = tf.keras.models.load_model("runs/save_model", compile=False)

        # load tokenizer
        with open('runs/tokenizer.pickle', 'rb') as handle:
            self.tokenizer = pickle.load(handle)
        
    def response(self, sentence):
        return self.predict(self.loaded_model, self.tokenizer, sentence)

    def inference(model, tokenizer, sentence):
        sentence = preprocess_sentence(sentence)

        start_token = [tokenizer.vocab_size]
        end_token = [tokenizer.vocab_size + 1]
        vocab_size = tokenizer.vocab_size + 2

        sentence = tf.expand_dims(
            start_token + tokenizer.encode(sentence) + end_token, axis=0
        )

        output = tf.expand_dims(start_token, 0)

        for i in range(40):
            predictions = model(inputs=[sentence, output], training=False)

            # select the last word from the seq_len dimension
            predictions = predictions[:, -1:, :]
            predicted_id = tf.cast(tf.argmax(predictions, axis=-1), tf.int32)

            # return the result if the predicted_id is equal to the end token
            if tf.equal(predicted_id, end_token[0]):
                break

            # concatenated the predicted_id to the output which is given to the decoder
            # as its input.
            output = tf.concat([output, predicted_id], axis=-1)

        return tf.squeeze(output, axis=0)

    def predict(self, model, tokenizer, sentence):
        prediction = self.inference(model, tokenizer, sentence)

        predicted_sentence = tokenizer.decode(
            [i for i in prediction if i < tokenizer.vocab_size]
        )

        return predicted_sentence
