import nltk, re, pandas, string, spacy, os
from collections import defaultdict
from fuzzywuzzy import fuzz, process
from pathlib import Path
import extract_files as e
data=pandas.read_csv('command_dataset.csv')
#nltk.download('stopwords')
#nltk.download('punkt')
stopwords=nltk.corpus.stopwords.words('english')
punctuation=string.punctuation
e.get_all_files()
def data_cleaning(cmd):
    lowercase_and_removepunction= "".join([ char.lower() for char in cmd if char.lower() not in punctuation ])
    tokenize=nltk.tokenize.word_tokenize(lowercase_and_removepunction)
    remove_stopwords=[ word for word in tokenize if word not in stopwords ]
    return remove_stopwords
data['processed']=data['Prompt'].apply(lambda x: data_cleaning(x))
def categorize_words():
    encrypt_words,decrypt_words=[],[]
    for cmd in data['processed'][data['Label']=='encrypt']:
          for word in cmd:
               encrypt_words.append(word)
    for cmd in data['processed'][data['Label']=='decrypt']:
         for word in cmd:
              decrypt_words.append(word)
    return encrypt_words, decrypt_words
encrypt_words,decrypt_words=categorize_words()
def predict(user_prompt):
     commands={}
     encrypt_counter,decrypt_counter=0,0
     for word in user_prompt:
          encrypt_counter += encrypt_words.count(word)
          decrypt_counter += decrypt_words.count(word)
     commands['Encrypt']=encrypt_counter
     commands['Decrypt']=decrypt_counter
     max_value=max(commands.values())
     max_commands=[ cmd for cmd, value in commands.items() if value==max_value ]
     return max_commands
user_prompt=input('Enter prompt: ')
cleaned_prompt=data_cleaning(user_prompt)
prediction=predict(cleaned_prompt)[0]
def extract_filenames(text):
    """Extracts filenames with various extensions from a given text.
    Supports all common file types, including video, audio, images, documents, etc."""
    # Expanded regex pattern to match almost all file extensions
    pattern = r'([^\s,]+(?:\.(?:[a-zA-Z0-9]{1,5})))'  
    # Use re.findall to get all matching file names in the text
    matches = re.findall(pattern, text)
    return matches
def extract_decryption_key(prompt):
    nlp = spacy.load('decryption_key_extractor/model-best')
    doc = nlp(prompt)
    keys=[ ent.text for ent in doc.ents ]
    result= keys[0] if len(keys)!=0 and len(keys) < 2 else False
    return result
def verify_path(file_path):
    # Check if the path contains a wildcard (e.g., *.mp4)
    path_obj = Path(file_path)
    if '*' in path_obj.name:
        directory = path_obj.parent  # Get the directory part
        # Check if the directory exists
        if directory.exists() and directory.is_dir():
            print(f"The exact directory '{directory}' exists.")
            return True
        else:
            print(f"The exact directory '{directory}' does not exist. lets predict the {file_path}")
            return False
    else:
        # If no wildcard, check if the full path exists as a file or directory
        if os.path.exists(file_path):
            if os.path.isfile(file_path):
                print(f"The file '{file_path}' exists.")
                return True
            
        else:
            print(f"The path '{file_path}' does not exist. lets predict the {file_path}") 
            return False         


def predict_file_location(files):
    file_paths=e.get_files_by_extension(files.split('.')[-1]) 
    
    matches = process.extract(files, file_paths, scorer=fuzz.ratio, limit=5)
    print("Top matching file paths:")
    for file_path, score in matches:
        print(f"File: {file_path}")
        choice = input("Is this the correct file path? (yes/y or no/n): ").lower()
        if choice in ('yes', 'y'):
            return file_path
        elif choice in ('no', 'n'):
            continue
    
File_names=extract_filenames(user_prompt)
exact_files=[]
def get_exact_file_location(files):
    for i in files:
        if verify_path(i):
            exact_files.append(i)
        else:
            file=predict_file_location(i)
            exact_files.append(file)
get_exact_file_location(File_names)
print(exact_files)
print(prediction)
keys=extract_decryption_key(user_prompt)
print(keys)
file_struct=' '.join(File_names)
from my_modules.EncryptDecrypt import encrypt_file, decrypt_file
if prediction == 'Encrypt':
    encrypt_file(exact_files[0])
elif prediction == 'Decrypt':
    decrypt_file(exact_files[0],keys)





