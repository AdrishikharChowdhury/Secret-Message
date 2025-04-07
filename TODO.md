# ✅ TODO List – Secret Message 🕵️‍♂️

This document outlines tasks to improve and expand the **Secret Message** project. Organized by functionality and priority.

---

## 🧱 CORE FEATURES

- [x] Encode individual words
- [x] Decode individual words
- [x] Encode a full sentence/paragraph
- [x] Decode a full sentence/paragraph
- [x] Create a CLI menu to interact with the user

---

## 🧩 MODULARIZATION

- [x] Split logic into:
  - `encoder.py`
  - `decoder.py`
  - `paragraph.py`
  - `utils.py`
  - `main.py`
- [ ] Ensure no circular imports between modules
- [ ] Add `__init__.py` if converted to a package in the future

---

## 🛡 ENHANCEMENTS

- [ ] Add input validation for special characters
- [ ] Preserve punctuation in paragraphs (e.g., commas, periods)
- [ ] Encode/decode preserving case (upper/lower)
- [ ] Use a more complex encoding scheme (optional flag)
- [ ] Allow user to choose encoding difficulty level

---

## 🔐 SECURITY & ENCRYPTION

- [ ] Implement a password-based encryption mode
- [ ] Use hashing (e.g., `hashlib`) to verify password access
- [ ] Add encoding based on key shifting (Caesar cipher style)

---

## 💾 DATA MANAGEMENT

- [ ] Save encoded messages to a file
- [ ] Load message from a file
- [ ] Display list of saved messages

---

## 🖥 USER INTERFACE

- [ ] Add color to CLI using `colorama`
- [ ] Build a GUI version using `tkinter`
- [ ] Add voice input/output support (stretch goal)

---

## 🌐 WEB VERSION

- [ ] Build a web interface using Flask
- [ ] Host messages securely using sessions
- [ ] Add option to share encoded messages via URL

---

## 🧪 TESTING

- [ ] Add unit tests for `encoder()` and `decoder()`
- [ ] Add paragraph-level test cases
- [ ] Create test files for automation

---

## 📄 DOCUMENTATION

- [x] Create `README.md`
- [x] Create `TODO.md`
- [ ] Add docstrings to all functions
- [ ] Generate documentation using `pdoc` or `Sphinx`

---

## 🧹 CLEANUP & REFACTORING

- [ ] Remove hardcoded test cases in code
- [ ] Refactor `menu()` into cleaner control flow
- [ ] Remove unnecessary print/debug statements

---

## 🔄 OPTIONAL ADDITIONS

- [ ] Add a decoding challenge (user guesses original sentence)
- [ ] Animate character-by-character reveal in CLI
- [ ] Gamify with levels of encoding/decoding
