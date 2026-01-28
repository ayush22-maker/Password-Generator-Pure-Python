## How to Use This Password Generator

This project is a **command-line (terminal) program**. You run it, answer a few questions, and it generates a password for you.

### 1) Open the project folder

Make sure you are inside the folder that contains `main.py`:

```
Password-Generator-Pure-Python/
  main.py
  README.md
  USAGE.md
```

### 2) Run the program

Run:

```bash
python main.py
```

If `python` doesn’t work, try:

```bash
python3 main.py
```

### 3) Answer the prompts

The program will ask you:

- **Password length**: enter a number (example: `12`, `16`, `20`)
- **Save to file?**: type `yes` or `no`
- **Your name**: used in the message and (if saving) in the filename
- **Purpose/Application**: example: `gmail`, `facebook`, `github`

### 4) Output (what you get)

- If you choose **no** for saving:
  - your password is shown directly in the terminal.
- If you choose **yes** for saving:
  - the program creates a text file in the **same folder** where you ran the script.

The saved file name format is:

```
password_<name>_<purpose>_<length>.txt
```

Example:

```
password_Ayush_Gmail_12.txt
```

### 5) Generate another password

At the end, it asks:

```
Do you want to generate another password (yes/no):
```

- Type **yes** to run again.
- Type **no** to exit.

## Common Problems (Quick Fix)

### “python is not recognized…”

Install Python 3 from the official website and make sure **Add Python to PATH** is enabled during installation. Then reopen your terminal and try again.

### I entered letters for length and got an error

Length must be an **integer number** (like `12`). Don’t enter text like `twelve`.

### I chose “yes” but can’t find the saved file

The `.txt` file is created in the **same directory where you ran `python main.py`**. Make sure your terminal is inside `Password-Generator-Pure-Python/` when you run it.

