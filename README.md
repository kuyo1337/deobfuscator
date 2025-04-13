
---
(yes,chatgpt wrote this)
# python deobfuscator
This is a Python-based tool designed to help you deobfuscate code that has been obfuscated via a combination of zlib compression, marshal serialization, and Base64 encoding. This utility automatically detects and handles both common encoding sequences, making it easier to recover obfuscated bytecode and generate Python compiled files (`.pyc`).

## Features

- **Automatic Sequence Detection:**  
  Detects if the obfuscation sequence is either:
  - `marshal → zlib → base64`  
  - `marshal → base64 → zlib`
  
- **User-friendly Interface:**  
  Provides clear output detailing the detected sequence and confirms when the deobfuscated `.pyc` file is saved.

- **Extensible Codebase:**  
  Written in clean, well-commented Python code that is easy to modify or extend for further functionality (like converting `.pyc` back to `.py`).

- **ASCII Art Intro:**  
  Displays a cool ASCII art banner upon startup.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/kuyo1337/deobfuscator.git
   cd deobfuscator
   ```

2. **(Optional) Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows use: venv\Scripts\activate
   ```

3. **Install any requirements:**  
   This project uses only the standard Python library, so no additional packages are required.

## Usage

To deobfuscate an obfuscated Python file, run the script with the file as an argument:

```bash
python deobfuscate.py obfuscated_code.py
```

The program will:
- Extract the Base64 encoded data from the target file.
- Attempt to decode it with both possible sequences.
- Display the detected decoding sequence.
- Write the resulting code object to `kuyo1337.pyc` by default.

### Example Output

```plaintext
 __                           .__         .__   
|  | ____ __ ___.__. ____     |  |   ____ |  |  
|  |/ /  |  <   |  |/  _ \    |  |  /  _ \|  |  
|    <|  |  /\___  (  <_> )   |  |_(  <_> )  |__
|__|_ \____/ / ____|\____/ /\ |____/\____/|____/
     \/      \/            \/                   

[+] Detected decode sequence: marshal → zlib → base64  
[+] Decompiled .pyc saved to: kuyo1337.pyc
```

## How It Works

1. **Extract Base64 String:**  
   The tool scans for the typical `base64.b64decode(b'...')` pattern in the file.

2. **Decode the Data:**  
   It then attempts both:
   - **Sequence 1:** `Base64 → zlib.decompress → marshal.loads`  
   - **Sequence 2:** `Base64 → alternate sequence (if applicable)`

3. **Generate `.pyc` File:**  
   Once the data is successfully decoded, it writes out a `.pyc` file prefixed with a basic header.

## Contributing

Contributions, bug reports, and feature requests are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

**PyZMBInit** is intended for educational and recovery purposes only. Use this tool responsibly and only on code that you have permission to deobfuscate.

---

Feel free to customize this README to better match the exact details of your project or any additional functionality you add. Enjoy deobfuscating with **PyZMBInit**!
