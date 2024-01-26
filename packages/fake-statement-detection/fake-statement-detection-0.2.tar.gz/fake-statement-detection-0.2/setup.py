from setuptools import setup, find_packages

setup(
    name='fake-statement-detection',
    version='0.2',
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'spacy', 'langchain', 'sentence_transformers', 'xgboost'],
)

# entry_points = {
#                    'console_scripts': [
#                        'fake-classifier-init = FakeStatementDetection.Satalia_Assignment:Classifier.init',
#                        'fake-classifier-load-preprocess = FakeStatementDetection.Satalia_Assignment:Classifier.load_and_preprocess_dataset_from_csv',
#                        'fake-classifier-fit = FakeStatementDetection.Satalia_Assignment:Classifier.fit_fake_classifier',
#                        'fake-classifier-predict-dict = FakeStatementDetection.Satalia_Assignment:Classifier.predict_dict',
#                        'fake-classifier-predict-json = FakeStatementDetection.Satalia_Assignment:Classifier.predict_json_by_path',
#                    ],
#                },