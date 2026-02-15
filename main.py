import json, urllib.request, urllib.parse, sys, time, os, base64
from config import Config

class GitHubKernel:
    """Senior engine for deep repo inspection and defensive code search."""
    def __init__(self):
        self.base = "https://api.github.com"
        self.headers = {"User-Agent": "Neural-Kernel-v6.5", "Accept": "application/vnd.github.v3+json"}

    def request(self, endpoint):
        try:
            req = urllib.request.Request(f"{self.base}{endpoint}", headers=self.headers)
            with urllib.request.urlopen(req) as r: return json.loads(r.read().decode())
        except: return None

    def deep_scan(self, repo):
        files = self.request(f"/repos/{repo}/contents") or []
        crit = [f['name'] for f in files if f['name'].startswith('.') or 'config' in f['name'].lower()]
        rel = self.request(f"/repos/{repo}/releases?per_page=1") or []
        return {"files": len(files), "ver": rel[0]['tag_name'] if rel else "N/A", "audit": crit}

    def code_search(self, repo, query):
        q = urllib.parse.quote(f"{query} repo:{repo}")
        return self.request(f"/search/code?q={q}")

class UI:
    """Advanced Terminal Interface with grid-dense rendering."""
    @staticmethod
    def header(path=""):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Config.CLR_MAIN}█{'▀'*58}█\n█ {Config.BOLD}{'NEURAL COMMAND BRIDGE'.center(56)} {Config.RESET}{Config.CLR_MAIN}█")
        if path: print(f"█ PATH: {path[:54].center(54)} █")
        print(f"█{'▄'*58}█{Config.RESET}\n")

    @staticmethod
    def menu(repo):
        print(f"{Config.CLR_ACCENT}CORE LOADED: {repo.upper()}{Config.RESET}")
        print(f"{Config.CLR_DIM}MODES: [E] EXPLORER | [F] FORENSICS | [S] SNIPPET | [Q] EXIT{Config.RESET}")

def explorer(kernel, repo, path=""):
    while True:
        UI.header(f"{repo}/{path}")
        data = kernel.request(f"/repos/{repo}/contents/{path}")
        if isinstance(data, dict) and data.get('type') == 'file':
            content = base64.b64decode(data.get('content', '')).decode('utf-8', errors='ignore')
            print(f"{Config.CLR_DATA}{content[:1500]}{Config.RESET}\n{Config.CLR_DIM}[EOF]{Config.RESET}")
            input(); return
        
        items = sorted(data, key=lambda x: x['type']) if isinstance(data, list) else []
        for i, item in enumerate(items):
            icon = "📁" if item['type'] == 'dir' else "📄"
            print(f"{Config.CLR_MAIN}[{i:02}]{Config.RESET} {icon} {item['name']}")
        
        cmd = input(f"\n{Config.CLR_MAIN}NAV (ID/Q) ❯ {Config.RESET}").lower()
        if cmd == 'q' or not cmd: break
        if cmd.isdigit() and int(cmd) < len(items): explorer(kernel, repo, items[int(cmd)]['path'])

def run():
    kernel, t = GitHubKernel(), Config.get_t()
    while True:
        UI.header()
        query = input(f"{Config.CLR_MAIN}{t['prompt']}{Config.RESET}")
        if not query: break
        search_res = kernel.request(f"/search/repositories?q={urllib.parse.quote(query)}&sort=stars")
        results = search_res.get('items', [])[:5] if search_res else []
        
        while True:
            UI.header(f"RESULTS FOR: {query}")
            for i, r in enumerate(results, 1):
                print(f"{Config.CLR_MAIN}[{i:02}]{Config.RESET} {Config.BOLD}{r['full_name']}{Config.RESET} ★ {r['stargazers_count']}")
            
            choice = input(f"\n{Config.CLR_MAIN}SELECT ID (or 'b') ❯ {Config.RESET}").lower()
            if choice == 'b' or not choice: break
            if choice.isdigit() and 0 < int(choice) <= len(results):
                sel = results[int(choice)-1]
                while True:
                    UI.header(sel['full_name']); UI.menu(sel['name'])
                    mode = input(f"\n{Config.CLR_MAIN}ACTION ❯ {Config.RESET}").lower()
                    if mode == 'q': break
                    elif mode == 'e': explorer(kernel, sel['full_name'])
                    elif mode == 'f':
                        d = kernel.deep_scan(sel['full_name'])
                        print(f"\n{Config.CLR_DATA}VER: {d['ver']} | FILES: {d['files']}{Config.RESET}")
                        for f in d['audit']: print(f"{Config.CLR_WARN}⚠ SENSITIVE: {f}{Config.RESET}")
                        input("\nSCAN COMPLETE.")
                    elif mode == 's':
                        sq = input(f"{Config.CLR_MAIN}SNIPPET QUERY ❯ {Config.RESET}")
                        res = kernel.code_search(sel['full_name'], sq)
                        if res and 'items' in res:
                            for item in res['items'][:5]: print(f"{Config.CLR_ACCENT}▶ {item['path']}{Config.RESET}")
                        else: print(f"{Config.CLR_ERROR}NO RESULTS OR API LIMIT.{Config.RESET}")
                        input("\nSEARCH COMPLETE.")

if __name__ == "__main__":
    try: run()
    except KeyboardInterrupt: print(f"\n{Config.CLR_ERROR}HALTED.{Config.RESET}")