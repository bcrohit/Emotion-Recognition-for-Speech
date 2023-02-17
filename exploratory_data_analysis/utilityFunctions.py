# dirpath = r"D:\SER-RO-MAHA\Sample Speech Data"

# neutral, sr = utf.return_audio_array('03-01-01-01-01-01-01.wav', dirpath, 'Neutral')
# happy, _ = utf.return_audio_array('03-01-03-01-01-01-01.wav', dirpath, 'Happy')
# sad, _ = utf.return_audio_array('03-01-04-01-01-01-01.wav', dirpath, 'Sad')
# angry, _ = utf.return_audio_array('03-01-05-01-01-01-01.wav', dirpath, 'Anger')
# fear, _ = utf.return_audio_array('03-01-06-01-01-01-01.wav', dirpath, 'Fear')
# disgust, _ = utf.return_audio_array('03-01-07-01-01-01-01.wav', dirpath, 'Disgust')
# surprise, _ = utf.return_audio_array('03-01-08-01-01-01-01.wav', dirpath, 'Surprise')
    
    
def return_audio_array(file, dirpath, emotion):
    import os
    import librosa
    emotion_folder = os.walk(dirpath)
    emotions = list(emotion_folder)[0][1]
    for i in emotions:
        if i == emotion:
            path = os.path.join(dirpath, i, file)
            return librosa.load(path)   
