import joblib
import pandas as pd
import numpy as np
import get_feature_for_new_file as get_feature
from sklearn.preprocessing import RobustScaler

path = r"audio_file.wav"

mfcc = get_feature.save_mfcc(path, 'mfcc', num_segments=3)
mels = get_feature.save_mfcc(path, 'mels', num_segments=3)
cqt = get_feature.save_mfcc(path, 'chroma_cqt', num_segments=3)
stft = get_feature.save_mfcc(path, 'chroma_stft', num_segments=3)

def convert_to_2d(X):
    x = []
    for i in range(len(X)):
        x.append(X[i].flatten())
        
    return np.array(x)


xmels = convert_to_2d(mfcc)
xmfcc = convert_to_2d(mels)
xstft = convert_to_2d(stft)
xcqt = convert_to_2d(cqt)


xnew = np.concatenate((xmels, xmfcc, xstft, xcqt))
scale = RobustScaler()
x = scale.fit_transform(xnew)

mlp_model = joblib.load(r"selected_model.joblib")
prediction = mlp_model.predict(x)
emotions, counts = np.unique(prediction, return_counts=True)
mapping = {0:'Anger', 1:'Disgust', 2:'Fear', 3:'Happy', 4:'Neutral', 5:'Sad', 6:'Surprise'}

predictions = pd.DataFrame(emotions, counts).reset_index()
predictions.columns = ['count', 'emotion']
predictions['emotion'] = predictions['emotion'].map(mapping)
predictions = predictions.sort_values(by='count', ascending=False)
print('Predicted Emotions are:\n', list(predictions['emotion'][:2]))