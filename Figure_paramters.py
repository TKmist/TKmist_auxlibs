import subprocess
from pathlib import Path
import sys
import importlib.metadata as im


class Figure_data:
    def __init__(self,manuscript_path,outfile,packages=None):
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
        self.packages = packages or []
        self.save_env_versions(self.outfile, self.packages)

    def save_env_versions(self, outfile="env_versions.txt", packages=None):
        packages = packages or []

        lines = [f"Python {sys.version.split()[0]}", ""]

        for pkg in packages:
            try:
                ver = im.version(pkg)
                lines.append(f"{pkg}=={ver}")
            except im.PackageNotFoundError:
                lines.append(f"{pkg}==NOT_INSTALLED")

        Path(outfile).write_text("\n".join(lines))
        
    def convert_pdf_to_eps(self,file_path):
        print("Converting PDF to EPS:")
        try:
            result = subprocess.run(['pdftops', '-eps', file_path], check=True, capture_output=True, text=True)
            print("Convertion succeeded")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print("Convertion failed")
            print(e.stderr)



