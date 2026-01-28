import subprocess
from pathlib import Path
import sys
import importlib.metadata as im


class Figure_data:
    def __init__(self,manuscript_path,outfile):
        self.label_font = 20
        self.ticlabelfont = 15
        self.legend_font_size = 10
        self.textfontsize=13
        self.manuscript_path = manuscript_path
        # Gęste style 
        self.ls_densely_dotted        = (0, (1, 1))
        self.ls_densely_dashed        = (0, (3, 1))
        self.ls_densely_dashdot       = (0, (3, 1, 1, 1))
        self.ls_densely_dashdotdotted = (0, (3, 1, 1, 1, 1, 1))
        
        # Rozrzedzone odpowiedniki
        self.ls_loosely_dotted        = (0, (1, 4))
        self.ls_loosely_dashed        = (0, (5, 4))
        self.ls_loosely_dashdot       = (0, (5, 4, 1, 4))
        self.ls_loosely_dashdotdotted = (0, (5, 4, 1, 4, 1, 4))
        
        self.outfile = outfile
        self.save_env_versions(self.outfile)

    def save_env_versions(self, outfile="env_versions.txt"):
        used_packages = {}
    
        modules_snapshot = list(sys.modules.values())
        for module in modules_snapshot:
            name = getattr(module, "__package__", None) or getattr(module, "__name__", None)
            if not name:
                continue
    
            root = name.split(".")[0]
            if root in used_packages:
                continue
    
            try:
                used_packages[root] = im.version(root)
            except im.PackageNotFoundError:
                pass
    
        lines = [f"Python {sys.version.split()[0]}", ""]
        for pkg in sorted(used_packages):
            lines.append(f"{pkg}=={used_packages[pkg]}")
    
        Path(outfile).write_text("\n".join(lines))
        
    def convert_pdf_to_eps(self,file_path):
        try:
            result = subprocess.run(['pdftops', '-eps', file_path], check=True, capture_output=True, text=True)
            print("Command succeeded")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print("Command failed")
            print(e.stderr)



