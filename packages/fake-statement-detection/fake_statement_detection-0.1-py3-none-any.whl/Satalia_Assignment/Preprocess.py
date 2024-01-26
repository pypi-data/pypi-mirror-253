from typing import Tuple, Union, Any, Dict, Optional
import joblib
import pandas as pd
import spacy
import re
import json
import os
from langchain.embeddings import HuggingFaceBgeEmbeddings
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import subprocess


# maybe not
# os.environ["OPENAI_API_KEY"] = _config["OPENAI_API_KEY"]
with open('config_file.json', 'r') as f:
    _config = json.load(f)


# Specify the spaCy model to download
model_name = "en_core_web_sm"
# Run the command to download the spaCy model
# subprocess.run(["python", "-m", "spacy", "download", model_name])
nlp = spacy.load(model_name)


def train_test_split_(df: pd.DataFrame, target_label, seed):
    df_train, df_val = train_test_split(df, test_size=0.2, random_state=seed)
    df_val, df_test = train_test_split(df_val, test_size=0.5, random_state=seed)
    y_train = df_train[target_label]
    y_val = df_val[target_label]
    y_test = df_test[target_label]
    # remove y
    x_train, x_val, x_test = [x.drop([target_label], axis=1) for x in [df_train, df_val, df_test]]
    return x_train, x_val, x_test, y_train, y_val, y_test


def print_basic_info(df: pd.DataFrame) -> None:
    print("Shape: ", '\n', df.shape, '\n')
    print("Dataset Info: ")
    print(df.info(verbose=True), '\n')
    print("Labels Frequency: ", '\n', df.Label.value_counts(), '\n')
    # print first five rows
    print("Five First Samples: ", '\n')
    df.apply(lambda row: print_row(df, row.name) if row.name < 5 else None, axis=1)


# Clean the dataset
def clean_text(text):
    '''Make text lowercase, remove punctuation and remove words containing numbers.'''
    text = str(text)  # Convert the input to a string
    text = text.lower()  # Convert the text to lowercase
    text = re.sub('.*?¿', '', text)  # Remove any characters followed by '¿'
    text = re.sub('\n', '', text)  # Remove newline characters
    text = re.sub(r" +", " ", text)  # Replace multiple spaces with a single space
    return text


def binarize_labels(label_columns: str, df: pd.DataFrame) -> pd.DataFrame:
    # 0 represent false
    # 1 represent true
    binary_map = {
        'true': 1,
        'mostly-true': 1,
        'half-true': 1,
        'extremely-false': 0,
        'false': 0,
        'barely-true': 0
    }

    df[label_columns] = df[label_columns].map(binary_map)
    return df


def drop_unrelevant_features(df: pd.DataFrame) -> None:
    df.drop('statement', axis=1, inplace=True)
    df.drop('cleaned_statement', axis=1, inplace=True)
    df.drop('statement_context', axis=1, inplace=True)
    df.drop('cleaned_context', axis=1, inplace=True)


def encode_categorical_features(df: pd.DataFrame) -> pd.DataFrame:
    # Create a dictionary to store encoders for each feature
    encoders = {}

    categorical_features = ['subjects', 'speaker_name', 'speaker_job',
                            'speaker_state', 'speaker_affiliation']

    le = LabelEncoder()
    for feature in categorical_features:
        df[feature] = le.fit_transform(df[feature])
        # Store the encoder in the dictionary
        encoders[feature] = le
        # Save encoders locally
        joblib.dump(encoders, "Fake_statements_data/" + feature + "_le_encoder.pkl")

    return df


def print_row(input_df: pd.DataFrame, index: int) -> None:
    print(f"speaker: {input_df.at[index, 'speaker_name']}")
    print(f"subjects: {input_df.at[index, 'subjects']}")
    print(f"statement: {input_df.at[index, 'statement']}")
    print(f"label: {input_df.at[index, 'Label']}", '\n')


def create_vector_store(embeddings: list, df: pd.DataFrame, new_dataset=False) -> None:
    if not os.path.isfile("Fake_statements_data/embedding_df_.csv") or new_dataset:
        embeddings_df = pd.DataFrame(columns=['text', 'embeddings'])
        embeddings_df['text'] = df['cleaned_statement']

        # Assign the lists of floats directly to the 'embeddings' column
        embeddings_df['embeddings'] = embeddings
        embeddings_df.to_csv("Fake_statements_data/embedding_df_.csv")


def generate_embeddings_for_column(df: pd.DataFrame, column_name: str, per_sample=False) -> Tuple[
    Union[pd.DataFrame, pd.Series], Any]:
    model_name = "BAAI/bge-small-en-v1.5"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': True}  # set True to compute cosine similarity
    model = HuggingFaceBgeEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )

    embeddings = model.embed_query(df[column_name])

    if column_name == "cleaned_context":
        # Perform PCA with 5 components only for statement_context embeddings
        if not per_sample:
            pca = PCA(n_components=5)
            embeddings = pca.fit_transform(embeddings)
            joblib.dump(pca, "Fake_statements_data/pca.pkl")
        else:
            pca = joblib.load("Fake_statements_data/pca.pkl")
            embeddings = pca.transform(embeddings)

    # Create a DataFrame from the embeddings list
    embeddings_df = pd.DataFrame(embeddings,
                                 columns=[f"{column_name}_embedding_{i + 1}" for i in range(len(embeddings[0]))])

    # Concatenate the original DataFrame (df) with the new embeddings DataFrame
    df_concatenated = pd.concat([df, embeddings_df], axis=1)

    return df_concatenated, embeddings


def read_and_preprocess_dataset_from_csv(path: str, new_dataset=False) -> pd.DataFrame:
    if not os.path.isfile("Fake_statements_data/fake_dataset_preprocessed.csv") or new_dataset:
        df = pd.read_csv(path).head(3000)
        print_basic_info(df)
        df = binarize_labels("Label", df)
        df['cleaned_statement'] = df['statement'].apply(clean_text)
        df['cleaned_context'] = df['statement_context'].apply(clean_text)
        df, statement_embeddings = generate_embeddings_for_column(df, "cleaned_statement")
        df, context_embeddings = generate_embeddings_for_column(df, "cleaned_context")
        create_vector_store(statement_embeddings, df, new_dataset)
        df = encode_categorical_features(df)
        drop_unrelevant_features(df)
        df.to_csv("Fake_statements_data/fake_dataset_preprocessed.csv")
    else:
        df = pd.read_csv("Fake_statements_data/fake_dataset_preprocessed.csv")
        df = df.drop("Unnamed: 0", axis=1)

    return df


def preprocess_row(row: pd.DataFrame, le_encoders: Dict[str, Dict[str, LabelEncoder]]) -> Tuple[pd.DataFrame, Any]:
    categorical_features = ['subjects', 'speaker_name', 'speaker_job',
                            'speaker_state', 'speaker_affiliation']

    row['cleaned_statement'] = row['statement'].apply(clean_text)
    row['cleaned_context'] = row['statement_context'].apply(clean_text)
    row, statement_embeddings = generate_embeddings_for_column(row, "cleaned_statement", per_sample=True)
    row, context_embeddings = generate_embeddings_for_column(row, "cleaned_context", per_sample=True)

    for column in categorical_features:
        le_dict = le_encoders.get(column)
        if le_dict:
            le = le_dict.get(column)
            if le:
                # Transform the value and handle unseen values
                try:
                    transformed_value = le.transform([row[column].iloc[0]])[0]
                    row.at[0, column] = transformed_value
                except:
                    row.at[0, column] = -1

    transformed_row = pd.DataFrame(row, index=[0])
    drop_unrelevant_features(transformed_row)
    return transformed_row, statement_embeddings
