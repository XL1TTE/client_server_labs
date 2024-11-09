
class FileManager:
    output_path: str = None
    input_path: str = None
    def __init__(self, output_path:str = None, input_path:str = None):
        self.input_path = input_path
        self.output_path = output_path
   
    def WriteOneLine(self, line: str, path: str = None):
        if path is None:
            if self.output_path is not None:
                path = self.output_path
            else:
                raise ValueError("Output file path is not specified!")
        
        with open(path, "a") as file:
            file.write(line + "\n")

