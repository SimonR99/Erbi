import tensorflow as tf
import argparse

from transformer.model import transformer
from transformer.dataset import get_dataset, preprocess_sentence

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

def predict(model, tokenizer, sentence):
    prediction = inference(model, tokenizer, sentence)

    predicted_sentence = tokenizer.decode(
        [i for i in prediction if i < tokenizer.vocab_size]
    )

    return predicted_sentence


import pickle
#sentence = "the force is strong with this one"
loaded_model = tf.keras.models.load_model("runs/save_model", compile=False)

# loading
with open('runs/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

while True:
    ans = input("input : ")
    if ans == "bye":
        name = True
        print("Good bye")
        break
    else:
        output = predict(loaded_model, tokenizer, ans)
        print(output)
