
import pandas as pd
import logging
from src.model_integration import chain_run

# Setup logging
logging.basicConfig(level=logging.INFO)

# Load your dataset (ensure your file is in 'data/sample_data.csv')
df = pd.read_csv('data/sample_data.csv')

# Function to process each entity
def process_entities(df):
    responses = []
    for index, row in df.iterrows():
        entity = str(row['Entity'])  # Ensure entity is a string
        query_prompt = f"Extract information for the entity '{entity}'."

        try:
            # Call the AI model (replace with your actual function call)
            response = chain_run(query_prompt=query_prompt, entity=entity)
            responses.append(response)
            logging.info(f"Successfully processed entity '{entity}': {response}")
        except Exception as e:
            # Log the error and append it to responses
            error_message = f"Error processing '{entity}': {str(e)}"
            logging.error(error_message)
            responses.append(error_message)

    # Add the responses to the DataFrame
    df['Extracted Info'] = responses
    return df

# Process the entities and output the results
processed_df = process_entities(df)
print(processed_df)

# Save results to a file for review (optional)
processed_df.to_csv("processed_results.csv", index=False)
