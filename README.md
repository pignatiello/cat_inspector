# 🐱 cat_inspector – Plugin di introspezione per Cheshire Cat AI

**cat_inspector** è un plugin per [Cheshire Cat AI](https://cheshire-cat-ai.github.io/docs/) pensato per aiutare sviluppatori a esplorare **tutti gli attributi e metodi disponibili nell’oggetto `cat`**
---

## 🚀 Funzionalità

✅ Mostra tutti gli attributi disponibili dell'oggetto `cat`  


---

## 🧪 Esempio di output

Esegui in chat:

```
debug_cat
```

Output:

```
['_llm', 'loop', 'memory', 'user_id', 'send_chat_message', 'main_agent', 'recall_relevant_memories_to_working_memory', ...]
```

---

## 🔧 Installazione

1. Crea un file chiamato `cat_inspector.py` nella cartella dei tuoi plugin (es. `plugins/`)
2. Incolla il codice sottostante
3. Riavvia Cheshire Cat 
4. In chat, scrivi:

```
debug_cat
```

---

## 📦 Contenuto del file `cat_inspector.py`

```python
from cat.mad_hatter.decorators import tool

@tool(return_direct=True)
def debug_cat(arg, cat):
    """Esplora gli attributi disponibili sull'oggetto cat in modo sicuro."""
    try:
        return "\n".join(dir(cat))
    except Exception as e:
        return f"Errore durante introspezione: {str(e)}"
```

---

## 👤 Autore

Creato da [@pignatiello](https://github.com/pignatiello) per supportare la community di Cheshire Cat nello sviluppo di plugin e strumenti intelligenti.

---

## 📜 Licenza

MIT – Puoi usarlo, modificarlo e distribuirlo liberamente.

---

