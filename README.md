# Arabic Dialect classifier
This is an Arabic dialect classifier that takes text and predict the dialect from 18 dialects.

## Dataset
The dataset used is discussed [here!](https://arxiv.org/pdf/2005.06557.pdf)
Dataset fetching is found in `Data_Fetching.ipynb` and then it was preprocessed in `preprocessing.ipynb`.

## Model 
In `Model_Training.ipynb` 2 models were trained; an SVM which got accuracy of 46% and a deep learning model which got accuarcy of 38% on the test set. The final SVM pipeline is saved as `ml_pipe.pickle`.

## Deployment
The model was deployed in a flask app in `app.py`.

## To Run 
```
pip install -r requirements.txt
```
```
python app.py
```