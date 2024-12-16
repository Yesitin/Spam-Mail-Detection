# Spam Mail Detection 

This project is about building a Machine Learning Classifier model which is able detect spam mails received by a transport forwarding company. To train the model synthetic data gets created. Synthetic data is a valid method because it contains patterns of real world data since the LLMs also had to be trained with real data. The project trains and compares three different ML algorithms. 

For this, firstly synthetic training data was created within the _data_generator.py_ file with the help of an AI Assistant based on an OpenAI API. The respective prompt is stored in the _prompts.py_ file. In the _main.py_ file the whole model building is performed. It contains Data Cleaning, Explorative Data Analysis (for having a better understanding of the data), Preprocessing, Machine Learning for model building, preserving the model permanently and finally test the model on complete new data. Machine Learning comprehenses three different model: Support Vector Machine, Random Forest Classifier and Naive Bayes Classifier. Due to the best metrics the choice was fallen on the Random Forest Classifier. The final model gets persisted in _rf_model.pkl_ and directly retrieved to test it on new data. 

## Getting started

To set up this repo create a folder for the project on your system (instructions for windows), open a terminal window, write "cd" and paste the folder path `cd "C:\Users\user\path\to\your\folder"`. Then type `git clone https://github.com/Yesitin/Spam-Mail-Detection.git` to download the whole repository (ensure that you have installed python and git). 

Next, create a virtual environment in order to avoid dependency conflicts. For this, type into the terminal `python -m venv env`. With `env\Scripts\activate` you start the environment.

Now you can install all dependencies with `pip install -r requirements.txt`. 

As a last step, you have to create a .env file and insert and OpenAI key: `OPENAI_API_KEY=your_api_key`. Replace your_api_key with your actual key.

Now, you can adjust _prompts.py_ if desired or adjust parameters of _data_generator.py_ and create some new training data. For this, run _data_generator.py_. After this, you can build a model with your own synthetic or even real data.
 
