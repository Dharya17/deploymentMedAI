CUSTOM_PROMPT_TEMPLATE = """
Use the pieces of information provided in the context to answer user's question.
If you don't know the answer, say you don't know. Don't try to make up an answer.
Don't provide anything outside the given context.

Context: {context}
Question: {question}

Give answer in a proper format.
Start the answer directly. No small talk.
"""