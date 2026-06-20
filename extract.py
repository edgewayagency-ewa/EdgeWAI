import zipfile
import xml.etree.ElementTree as ET
import sys

def extract_text(pptx_path):
    with zipfile.ZipFile(pptx_path, 'r') as z:
        # Find all slide xml files
        slide_files = [f for f in z.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')]
        # Sort them properly
        slide_files.sort(key=lambda x: int(x.split('slide')[1].split('.xml')[0]))
        
        for slide_file in slide_files:
            print(f"--- {slide_file} ---")
            xml_content = z.read(slide_file)
            root = ET.fromstring(xml_content)
            # Find all text nodes. The namespace for a:t is http://schemas.openxmlformats.org/drawingml/2006/main
            namespaces = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
            for text_node in root.findall('.//a:t', namespaces):
                if text_node.text:
                    print(text_node.text)

if __name__ == "__main__":
    extract_text(sys.argv[1])
