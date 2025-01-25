from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from langchain.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain.chains import OpenAI

app = Flask(__name__)
CORS(app) # Allow requests from frontend

# Carregando o texto
loader = TextLoader('path/to/your/file.txt')
documents = loader.load()

# Dividindo o texto em partes menores
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

for text in texts:
    print(text)

@app.route('/train', methods=['POST'])
def train_llm():
    data = request.json
    text_data = data.get('text', '')

    # Simulated LLM training process
    chain = OpenAI()
    result = chain.run(text_data)
    return jsonify({"message": "LLM trained sucessfully!", "result": result})

@app.route('/upload', methods=['POST'])
def upload_document():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file uploaded"}), 400
    
    # Example file handling
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)

    # Extract text (mock process)
    text = open(file_path, "r").read()
    return jsonify({"text": text})

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)