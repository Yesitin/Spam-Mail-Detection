import os
import csv
import re
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from prompts import *

# Load the .env file
_ = load_dotenv(find_dotenv())

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
)


# Initialize model settings
model = "gpt-4o-mini"
temperature = 0.8
max_tokens = 5000

# Parameters 
desired_rows = 5000
batch_size = 100
generated_rows = 0
mails = []

system_message = system_message
prompt = generate_prompt(batch_size)

# Assistant function to execute model with prompt
def generate_data():
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {   
                "role": "system", 
                "content": system_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )

    return completion.choices[0].message.content



# Function to clean up the extra quotes
def clean_email_text(text):
    text = re.sub(r'"""\s*|\s*"""', '', text)                                   # Remove any extra triple quotes and unwanted formatting
    return text.strip()


# Save output file

output_file = "train_data.csv"

with open(output_file, "w", newline="", encoding = "utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Mail Text", "Label"])                                     # write header

    while generated_rows < desired_rows:
        batch_mails = generate_data()                                           # generating a batch of mails 

        rows = batch_mails.strip().split("\n")                                  # Split the batch into rows, removing extra headers and quotes
        for row in rows:
            if row and not row.lower().startswith("mail text"):                 # Avoid duplicated headers
                cleaned_row = clean_email_text(row)                             # Clean any extra quotes
                split_row = cleaned_row.split('","')                            # Split by the delimiter for email text and label
                if len(split_row) == 2:
                    writer.writerow([split_row[0].strip('"'), split_row[1].strip('"')])  # Remove edge quotes
                    generated_rows += 1
                if generated_rows >= desired_rows:
                    break                                                       # Stop if num of rows are reached