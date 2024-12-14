import openai
import os
def generate_answer_with_openai(query, extracted_data):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Construct the prompt for the conversation
    messages = [
        {"role": "system", "content": "You are a helpful assistant who provides answers based on patient health records."},
        {"role": "user", "content": f"Health Record Data:\n{extracted_data}\n\nQuestion: {query}"}
    ]

    # Use the ChatCompletion endpoint
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # You can also use "gpt-4" if available
        messages=messages,
        max_tokens=150,
        temperature=0.7
    )

    # Extract and return the response
    return response['choices'][0]['message']['content'].strip()
