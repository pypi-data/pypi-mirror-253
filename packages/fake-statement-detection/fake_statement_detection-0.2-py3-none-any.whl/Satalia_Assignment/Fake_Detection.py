from Preprocess import *
from Classifier import FakeClassifier

RANDOM_SEED = 123

if __name__ == "__main__":
    fake_classifier = FakeClassifier(seed=RANDOM_SEED)
    x_train, y_train = fake_classifier.load_and_preprocess_dataset_from_csv("Fake_statements_data/data.csv", new_dataset=False)
    fake_classifier.fit_fake_classifier(x_train, y_train, "Fake_1")
    # df = read_and_preprocess_dataset_from_csv("Fake_statements_data/data.csv")
    # x_train, x_val, x_test, y_train, y_val, y_test = train_test_split_(df, "Label", seed=RANDOM_SEED)
    # fake_classifier = FakeClassifier(x_train, y_train, x_test, y_test, "XGBoost", seed=RANDOM_SEED)



    with open('single_sample.json', 'r') as f:
        dict_data = json.load(f)



    print(fake_classifier.predict_dict(dict_data))
    print(fake_classifier.predict_json_by_path('single_sample.json', top_k=5))
    print()
