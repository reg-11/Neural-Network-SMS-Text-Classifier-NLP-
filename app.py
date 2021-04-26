import streamlit as st
import pickle
from keras.models import load_model
from itertools import chain
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

PAGE_CONFIG = {"page_title":"SMS_Classifier.io","layout":"centered"}
st.set_page_config(**PAGE_CONFIG)


pickle_in = open('tokenizer.pkl','rb')
tokenizer = pickle.load(pickle_in)

#load model
model = load_model('model.h5')

def predict_message(pred_text):
  temp= []
  temp.append(pred_text)
  new_seq = tokenizer.texts_to_sequences(temp)
  padded = pad_sequences(new_seq, maxlen =60,
                      padding = "post",
                      truncating="post")
  pred = model.predict(padded)


  pred = list(chain.from_iterable(pred))
 
  return (pred)

def main():
    st.title("Neural Network SMS Text Classifier")
    html_temp = """
    <div style="background-color:mustard;padding:10px">
    <h2 style="color:white;text-align:center;">Neural Network SMS Classifier </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    msg = st.text_input("Message","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_message(msg)
    st.success('The output is {}'.format(result))
    st.text("The higher the value of the prediction result, the higher the probability of being a scam message.")


if __name__=='__main__':
    main()