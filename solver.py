from config import llm,llm2

# Fonction pour envoyer un prompt à ChatGPT et obtenir la réponse
def get_trad_sentence(problem_statement: str) -> str:
    """
    Envoie un prompt à ChatGPT et obtient la réponse.

    Args:
    - problem_statement (str): La description du problème en français.

    Returns:
    - response (str): La réponse de ChatGPT contenant les variables et les contraintes.
    """
    prompt = f"""
    Je vais te donner une phrase en francais je veux juste que tu l'a traduise. Ne me renvoie rien d'autre que la même phrase mais traduite en anglais.
    Phrase: {problem_statement}
    """

    response = llm.invoke(prompt)  # Utilisation de invoke
    return response