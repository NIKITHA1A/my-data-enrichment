
# Mock function to simulate chain.run behavior
def chain_run(query_prompt, entity):
    # Validate that the model_name is passed correctly as a string
    model_name = "phi3:medium"  # This should be the model string, not a dictionary

    if not isinstance(entity, str):
        raise ValueError(f"Entity must be a string. Received: {type(entity)}")

    # Assuming chain.run() accepts the query as a string input and model_name as a string
    try:
        # Simulate a successful model call (replace with actual chain.run call)
        result = f"Processed information for entity '{entity}' using model '{model_name}'."
        return result
    except Exception as e:
        raise ValueError(f"Error during model execution: {str(e)}")
