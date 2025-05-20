from cat.mad_hatter.decorators import tool





@tool(return_direct=True)
def debug_cat(arg, cat):
    """Esplora gli attributi disponibili sull'oggetto cat in modo sicuro."""
    try:
        return "\n".join(dir(cat))  # converte tutto in una stringa
    except Exception as e:
        return f"Errore durante introspezione: {str(e)}"
