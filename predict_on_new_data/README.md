
### Predict on New Audio File

Using the `get_feature_for_new_file.py` file you can extract the features required for the MLP Claasifier to predict the emotion in the audio file.

All you need to do is call the **save_mfcc** function with the path and feature name. Which would return a numpy array of all the feture vectors.

The `predict.py` file would do all the neccessary work if you have all the libraries required are installed and it would output the emotions.
