######FRNN_sample_model.h5 contains a sample model from FRNN for demonstration
######It is a very small version (small dense_size and rnn_size) that does not perform well
from keras.models import load_model
model=load_model('FRNN_sample_model.h5')
model.summary()
