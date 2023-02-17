
# Speech Emotion Recognition

This is a speech emotion recognition project that uses MLP classifier to predict the emotion of an audio file. The goal of this project is to develop a model that can accurately classify the emotion of a speaker using their speech



## Dataset

The dataset consists of 4,800 audio files in WAV format, with a duration of 3-5 seconds each. The audio files are labeled with one of seven emotions: neutral, calm, happy, sad, angry, fearful, and disgust. The dataset was preprocessed by extracting the features from each audio file and combining them into a feature vector. The dataset was preprocessed by trimming the audio signals and normalizing the audio to ensure that each audio has the same sound.
## Feature Extraction

- Time and frequency domain features were extracted from all datasets using a frame size of 1024 and a hop length of 512 and than `SMA, MAD, Mean, Median, Max, Min, Skewness, Kurtosis, Energy, Entropy, STD, IQR` were calculated for each signal.
- MFCC and mel spectrograms were extracted from all datasets, except TESS, using a frame size of `2048` and a hop length of `512`. The number of mel filters used was `26`.
- MFCC, mel spectrograms, chroma STFT, and chroma CQT were extracted from TESS using a frame size of 2048 and a hop length of `512`. The number of mel filters used was `40`, and the number of chroma bins used was also `40`.
#### Features
`Time Domain: Amplitude Envelope(AE), Root Mean Squared Energy(RMSE), Zero Crossing Rate(ZRC)`

`Frequency Domain: Spectral Centroid(SC), Spectral Bandwidth(SB)`


| Feature | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Time Domain Features`      | `12 Central measures of tendency for each signal` | These features show how a signal changes with time. |
| `Frequency Domain features` | `12 Central measures of tendency for each signal` | These show how much of the signal lies within each given frequency band over a range of frequencies.|
| `MFCC`      | `The raw vectors for RAVDESS and SAVEE` | Features that capture the shape of the spectral envelope of audio signal. |
| `Mel Spectrograms`      | `The raw vectors for RAVDESS and SAVEE` | Representation of audio signal that are mapped to the mel scale to better approximate human auditory perception. |
| `Chrom STFT`      | `The raw vectors for all datasets` | Features that represent the energy of audio signal across 12 pitch classes. |
| `Chrom CQT`      | `The raw vectors for all datasets` | Features that represent the energy of audio signal across 12 pitch classes, with logarithmically spaced frequency bins. |




## Models Used

Four different machine learning models were used for the classification task:

- CNN (Convolutional Neural Network)
- Random Forest Classifier
- LSTM (Long Short-Term Memory)
- MLP (Multi-Layer Perceptron) Classifier
## Methodology

The `MLP classifier` was choosen to predict the emotion of each audio file based on the feature vectors extracted from the audio files. The feature vectors were standardized using `Robust Scaler` before training the model. The model was trained on 80% of the dataset and tested on the remaining 20%. The performance of the model was evaluated using accuracy, precision, recall, and F1 score.


## Results

The MLP Classifier achieved an accuracy of `84%`, which is promising. However, it was found that all existing solutions only use MFCC and mel spec features, without giving importance to scaling and transformation of data or hyperparameter tuning.

## Applications

This project has potential applications in call centers and other customer service industries, where automation could be used to capture the emotions of the speaker and respond accordingly.
## Conclusion

This project demonstrates that even complex models such as CNN can fail to generalize well in some cases. While this project is not the best, it provides a good starting point for further research and development in speech emotion recognition.
## Documentation

[Documentation](https://linktodocumentation)


## Contributors

- Rohit BC [@bcrohit](https://www.github.com/bcrohit)
- Smrithi Shaji [@smrit18](https://www.github.com/smrit18)

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rohit-bc-7a25741b3)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/karnatrohit)

## Feedback

If you have any feedback, please [Mail Us](gowdarohith2003@gmail.com)

