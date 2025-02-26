# CipherBot_on_NLP
CipherBot is an AI-powered file encryption and decryption assistant that processes user commands with NLP and machine learning. It identifies encryption requests, extracts filenames, verifies file paths, and retrieves decryption keys automatically. Designed for seamless security workflows,It enhances file protection with intelligent automation.

## Features

- **Command Processing**: Understands encryption and decryption commands using NLP.
- **Named Entity Recognition (NER)**: Extracts decryption keys and filenames from user input.
- **File Path Verification**: Ensures the correct file path before processing.
- **Fuzzy Matching**: Predicts file locations if the given path is incorrect.
- **Seamless Integration**: Works with predefined datasets for learning and improving predictions.

## Named Entity Recognition (NER)

CipherBot utilizes NER to extract key information from user commands. This includes:

- **Decryption Keys**: Identifying and extracting passcodes or keys required for decryption.
- **File Names & Paths**: Recognizing and verifying file locations for processing.

### How NER is Used in CipherBot

1. User provides an encryption or decryption command.
2. NER extracts key details such as filenames and decryption keys.
3. The bot verifies the file location and processes encryption/decryption accordingly.

## Use Cases

- **Automated File Security**: Encrypt or decrypt files with simple natural language commands.
- **Secure File Handling**: Ensure confidential files are properly protected or accessed only with valid keys.
- **Systematic Command Processing**: Streamline encryption workflows in security-sensitive environments.
- **Smart Key Extraction**: Extract and apply decryption keys from user-provided text without manual input.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/cipherbot.git
   cd cipherbot
   ```
2. Install Required Dependencies
   ```
3. Run the bot:
   ```sh
   python bot.py
   ```

## How to Run `bot.py`

Run the bot with a simple command:

```sh
python bot.py
```

### Example Output

#### Encryption Example

**Input:**

```
Encrypt file document.txt

then it started to predicts the file location based on your file name if you verify that predicted file then it started to encrypt the file
```

**Output:**

```
Encryption successful! Encrypted file: document_encrypted.txt
```

#### Decryption Example

**Input:**

```
Decrypt file document_encrypted.txt with key fTw5bYlu3bJ1izdZeKfsPrQ3fYK-Wx0xH7OQ2VO0mA=
```

**Output:**

```
Decryption successful! Decrypted file: document.txt
```

## Dataset

CipherBot uses a predefined dataset (`command_dataset.csv`) to train its model in recognizing encryption and decryption commands. It includes various sample commands for improving accuracy.

## Contribution

Contributions are welcome! Feel free to fork the repository, submit issues, or create pull requests.

