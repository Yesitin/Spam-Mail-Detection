system_message = """
    You are an AI agent who creates new CSV training for machine learning. The CSV data will serve for 
    a spam mail fraud detection project.
"""


def generate_prompt(batch_size):
    prompt = f"""
            Generate {batch_size} transport request emails for a forwarding company, with an even split of "spam" and "not spam" labels. Each email should be 50 to 300 characters long (make variation of length).
            Instructions:

                For "not spam" emails:
                    Include realistic transport queries with clear, detailed information:
                        Subject: Must include specific transport details.
                        Body: Describe cargo (type, weight), origin, destination, and realistic pricing. Mention standard payment terms.
                    Avoid unrealistic pricing, excessive urgency, unclear payment terms, or suspicious attachments/links.

                For "spam" emails:
                    Incorporate elements of spam:
                        Subject: Should hint at urgency or unrealistic offers.
                        Body: Include features like unrealistic pricing, high-pressure language for quick decisions, vague payment terms, or unusual bank details. Add minimal or unclear information about cargo and routes.
                    Ensure varied spam characteristics to avoid predictability (e.g., don't always use the same unrealistic price or urgency).

            Output the emails in a CSV format with two columns, first one is mail text and second one is the label. DON'T INCLUDE HEADERS!

            - label each mail as "spam" or "not spam" accordingly
            - Some spam emails should look almost legitimate with only a small giveaway (e.g., slight mispricing or a vague reference to payment).
            - make the dataset balanced what means it is required to be 50:50 since it serves for a classification problem (machine learning)
            - DO NOT INCLUDE ANY TEXT BEFORE AND AFTER THE DATA. JUST START BY OUTPUTTING THE ROWS. NO EXTRA TEXT!!!

            Ensure the dataset includes a variety of email styles and content to help the model generalize better. Variety is essential in order to prevent overfitting!!
            Ensure VARITY!!"""
    
    return prompt
