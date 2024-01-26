from typing import Tuple
import json
from Preprocess import preprocess_row, read_and_preprocess_dataset_from_csv
from scipy import spatial
import numpy as np
import pandas as pd
import xgboost
import ast
import os
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from scipy.spatial.distance import cdist





class FakeClassifier:

    def __init__(self, seed):
        self.seed = seed
        self.model = None
        self.le_encoders = None
        self.df_embeddings = None
        self.y_train = None
        self.x_train = None

    def fit_fake_classifier(self, x_train, y_train, model_name):
        xg = xgboost.XGBClassifier(objective="binary:logistic", max_depth=12, n_estimators=250, random_state=self.seed)
        if not os.path.isfile("trained_models/" + model_name + "_" + str(self.seed) + "_" + "_.pkl"):
            print(" Training XGB...")
            xg.fit(x_train, y_train)
            joblib.dump(xg, "trained_models/" + model_name + "_" + str(self.seed) + "_" + "_.pkl")
        else:
            xg = joblib.load("trained_models/" + model_name + "_" + str(self.seed) + "_" + "_.pkl")

        # y_pred = xg.predict(x_test)
        # acc = accuracy_score(y_test, y_pred)
        # print("XGBoost Accuracy Score on Test: ", acc, "seed: ", seed)
        self.model = xg
        # return xg

    def load_encoders(self):
        encoders = {}

        categorical_features = ['subjects', 'speaker_name', 'speaker_job',
                                'speaker_state', 'speaker_affiliation']

        le = LabelEncoder()
        for feature in categorical_features:
            le = joblib.load("Fake_statements_data/" + feature + "_le_encoder.pkl")
            # Store the encoder in the dictionary
            encoders[feature] = le
            # Save encoders locally

        return encoders

    def predict_dict(self, dict_data: dict, top_k=2):
        answer = {"truthfulness": None,
                  "justification": None}
        # Convert the JSON data to a DataFrame
        df_row = pd.DataFrame.from_dict(dict_data, orient='index').transpose()
        df_row, statement_embedding = preprocess_row(df_row, self.le_encoders)
        closest_texts = self.find_most_similar_texts(statement_embedding, self.df_embeddings, top_k)
        prediction = self.model.predict(df_row.astype(float))[0]
        if prediction == 1:
            answer["truthfulness"] = True
        else:
            answer["truthfulness"] = False
        answer[
            "justification"] = "The Fake Detection model learned from similar statements to the given one to make its" \
                               " prediction. "+ str(top_k) +" of the most similar statements from the training data are: " + str(
                                closest_texts)
        return answer

    def predict_json_by_path(self, json_path: str, top_k=2):
        answer = {"truthfulness": None,
                  "justification": None}

        with open(json_path, 'r') as f:
            json_data = json.load(f)

        # Convert the JSON data to a DataFrame
        df_row = pd.DataFrame.from_dict(json_data, orient='index').transpose()
        df_row, statement_embedding = preprocess_row(df_row, self.le_encoders)
        closest_texts = self.find_most_similar_texts(statement_embedding, self.df_embeddings, top_k)
        prediction = self.model.predict(df_row.astype(float))[0]
        if prediction == 1:
            answer["truthfulness"] = True
        else:
            answer["truthfulness"] = False
        answer[
            "justification"] = "The Fake Detection model learned from similar statements to the given one to make its" \
                               " prediction. "+ str(top_k) +" of the most similar statements from the training data are: " + str(
                                closest_texts)
        return answer

    def find_most_similar_texts(self, new_embedding, embeddings_df, top_k=2):
        if top_k > 10:
            top_k = 10
        # Compute Euclidean distances between the new embedding and existing embeddings
        distances = cdist(new_embedding, embeddings_df['embeddings'].tolist(), metric='euclidean')
        # Find the indices of the top k closest texts
        closest_indices = np.argpartition(distances, top_k, axis=1)[:, :top_k]
        # Retrieve the closest texts
        closest_texts = [embeddings_df.at[index, 'text'] for index in closest_indices[0]]
        return closest_texts

    def load_embedding_df(self):
        df = pd.read_csv("Fake_statements_data/embedding_df_.csv")
        # Convert each string representation of a list to an actual list using ast.literal_eval
        df['embeddings'] = df['embeddings'].apply(ast.literal_eval)
        # Convert each list of strings to a list of floats
        df['embeddings'] = df['embeddings'].apply(lambda x: [float(item) for item in x])
        return df.drop("Unnamed: 0", axis=1)

    def load_and_preprocess_dataset_from_csv(self, path: str, new_dataset=False) -> Tuple[pd.DataFrame, pd.Series]:
        target_label = "Label"
        df_train = read_and_preprocess_dataset_from_csv(path, new_dataset)
        y_train = df_train[target_label]
        x_train = df_train.drop([target_label], axis=1)
        self.le_encoders = self.load_encoders()
        self.df_embeddings = self.load_embedding_df()
        self.x_train = x_train
        self.y_train = y_train
        return x_train, y_train
