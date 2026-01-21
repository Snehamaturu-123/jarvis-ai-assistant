def generate_response(user_query: str, context: str):
    """
    Local AI logic (LLM-ready placeholder)
    """

    if context:
        return f"Based on previous knowledge: {context}"

    if "hello" in user_query.lower():
        return "Hello! I am Jarvis, your personal AI assistant."

    if "who are you" in user_query.lower():
        return "I am Jarvis, designed to assist you intelligently."

    return (
        "I am still learning. Please provide more information "
        "or ask another question."
    )
