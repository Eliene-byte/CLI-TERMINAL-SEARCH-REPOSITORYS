import os

class Config:
    # High-Definition ANSI Palette
    CLR_MAIN = "\033[38;5;39m"    # Electric Blue
    CLR_ACCENT = "\033[38;5;118m" # Vivid Green
    CLR_DATA = "\033[38;5;220m"   # Gold
    CLR_WARN = "\033[38;5;202m"   # Orange (Adicionando esta linha)
    CLR_ERROR = "\033[38;5;196m"  # Red
    CLR_DIM = "\033[38;5;240m"    # Gray
    RESET = "\033[0m"
    BOLD = "\033[1m"

    LANG = os.getenv("LANG", "en")[:2]
    
    STRINGS = {
        "en": {
            "title": "NEURAL GITHUB COMMAND BRIDGE",
            "search_status": "PROBING REPOSITORIES...",
            "no_results": "NO DATA RECOVERED.",
            "prompt": "INPUT QUERY > ",
            "meta_stars": "STARS"
        },
        "pt": {
            "title": "PONTE DE COMANDO NEURAL GITHUB",
            "search_status": "SONDANDO REPOSITÓRIOS...",
            "no_results": "NENHUM DADO RECUPERADO.",
            "prompt": "COMANDO DE BUSCA > ",
            "meta_stars": "ESTRELAS"
        }
    }

    @classmethod
    def get_t(cls):
        return cls.STRINGS.get(cls.LANG, cls.STRINGS["en"])