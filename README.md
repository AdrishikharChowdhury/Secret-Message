# 🔐 Secret Message

**Secret Message** is a Python-based mini-project that allows users to encode and decode messages at the word level. It provides a simple encryption technique to obscure individual words, ideal for learning about string manipulation, modularization, and basic ciphers.

---

## 📜 Features

- 🔠 **Word-level Encoding**: Rearranges and pads words to hide the original message.
- 🔓 **Decoding Mechanism**: Reverts encoded messages back to their original form.
- 🧩 **Paragraph Support**: Supports encoding and decoding full sentences or paragraphs.
- 🔄 **User Menu Interface**: Console menu to guide users through options.
- 🧱 **Modular Design**: Code is split across multiple logical modules:
  - `main.py` – Application entry point
  - `encoder.py` – Word encoding logic
  - `decoder.py` – Word decoding logic
  - `paragraph.py` – Handles sentence-level processing
  - `utils.py` – Utilities and menu system

---

## ⚙️ How It Works

- If a word has **3 or more characters**, the encoder:
  - Moves the first letter to the end
  - Adds 3 random lowercase letters before and after the word
- If a word has **less than 3 characters**, it's simply reversed
- The decoder reverses this process to retrieve the original message

---

## 🚀 Getting Started

### ✅ Requirements

- Python 3.6+
- No external libraries required

### 📂 Folder Structure

```
Secret Message/
│
├── main.py              # Application entry point
├── encoder.py           # Word encoder logic
├── decoder.py           # Word decoder logic
├── paragraph.py         # Paragraph encoding/decoding
├── utils.py             # Helper functions and menu
└── README.md            # You're reading it!
```

### 🧪 Run the Project

```bash
python main.py
```

Follow the on-screen menu to encode or decode messages.

---

## 🎯 Example

```
Enter your option:
1. Encode a paragraph
2. Decode a paragraph
3. Show the message
4. Exit

> 1
Enter the message to encode: Hello world
Message encoded successfully.

> 3
The current message is:
abcelloehl xyzdlrowrld

> 2
Enter the message to decode: abcelloehl xyzdlrowrld
Message decoded successfully.

> 3
The current message is:
Hello world
```

---

## 🛠 Future Improvements

- Password-based encryption
- File I/O support
- Web UI using Flask or Django
- Save encoded messages locally
- Add stronger encoding logic (Caesar cipher, Vigenère cipher, etc.)

---

## 🧑‍💻 Author

Made with ❤️ by [Adrishikhar Chowdhury](mailto:amiadrishikhar@gmail.com)
