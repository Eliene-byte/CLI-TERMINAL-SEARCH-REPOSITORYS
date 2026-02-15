# ⚡ CLI-TERMINAL-SEARCH-REPOSITORYS
> **Engine:** Neural Command Bridge v6.5 | **Developer:** Eliene-byte

[English Version](#english) | [Versão em Português](#português)

---

<a name="english"></a>
## 🇺🇸 English Version

### 🖥️ Overview
A high-performance command-line tool built in Python for probing, forensic auditing, and navigating GitHub repositories without local cloning. It acts as a "Search Kernel," bridging the gap between raw API data and terminal efficiency.

### 🚀 Key Features
* **Global Search:** Find repositories by keywords with star/fork metrics.
* **Forensics Mode [F]:** Audit project health, releases, and detect sensitive/config files (e.g., `.env`, `.yml`).
* **Remote Explorer [E]:** Navigate remote folders in real-time, reading file content via Base64 decoding directly in the terminal.
* **Snippet Hunt [S]:** Target specific code patterns across any public repository.

### 🛠️ Setup & Usage
1.  **Clone:** `gh repo clone Eliene-byte/CLI-TERMINAL-SEARCH-REPOSITORYS`
2.  **Run:** `python main.py`
3.  **Note:** Requires Python 3.10+ and GitHub CLI (for auth).



---

<a name="português"></a>
## 🇧🇷 Versão em Português

### 🖥️ Visão Geral
Uma ferramenta de linha de comando de alta performance desenvolvida em Python para prospecção, auditoria forense e navegação em repositórios do GitHub sem clonagem local. Funciona como um "Kernel de Busca", conectando dados da API à eficiência do terminal.

### 🚀 Principais Funcionalidades
* **Busca Global:** Encontre repositórios por palavras-chave com métricas de estrelas e forks.
* **Modo Forense [F]:** Audita a saúde do projeto, versões e detecta arquivos sensíveis ou de configuração (ex: `.env`, `.yml`).
* **Explorador Remoto [E]:** Navegue pelas pastas remotas em tempo real, lendo arquivos via decodificação Base64 no terminal.
* **Caça de Snippets [S]:** Busca padrões de código específicos em qualquer repositório público.

### 🛠️ Instalação e Uso
1.  **Clonar:** `gh repo clone Eliene-byte/CLI-TERMINAL-SEARCH-REPOSITORYS`
2.  **Executar:** `python main.py`
3.  **Nota:** Requer Python 3.10+ e GitHub CLI (para autenticação).



---

## 📐 Technical Architecture / Arquitetura Técnica

* **`main.py`**: Core engine / Motor principal.
* **`config.py`**: ANSI Color Palette & Localization / Paleta de Cores e Tradução.

### 🛡️ Defensive Programming
The system implements **NoneType Guards** and **Base64 Buffer Management** to ensure stability against API rate limits and network instability.

O sistema implementa **NoneType Guards** e **Gerenciamento de Buffer Base64** para garantir estabilidade contra limites da API e instabilidades de rede.

---
**Developed by [Eliene-byte](https://github.com/Eliene-byte)**