from sklearn.pipeline import Pipeline
import pickle





if __name__ == '__main__':

    with open("ml_pipe.pickle", "rb") as f:
        (pipe) = pickle.load(f)

    text= input()
    print(text)
    pred = pipe.predict([text])
    print(pred)


