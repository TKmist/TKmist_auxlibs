import subprocess

class Figure_data:
    def __init__(self):
        self.label_font = 20
        self.ticlabelfont = 15
        self.legend_font_size = 10
        self.textfontsize=13
        self.manuscript_path = '../../figures_update'
        
        
    def convert_pdf_to_eps(self,file_path):
        try:
            result = subprocess.run(['pdftops', '-eps', file_path], check=True, capture_output=True, text=True)
            print("Command succeeded")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print("Command failed")
            print(e.stderr)