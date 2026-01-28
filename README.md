# Password Generator (Pure Python)

A simple **command-line password generator** written in pure Python. It generates a random password of your chosen length, then either **prints it to the terminal** or **saves it to a `.txt` file** along with the name and purpose you provide.

## Features

- **Custom password length** (you choose the number of characters)
- **Random password generation** using Python’s built-in `random` module
- **Character set includes**:
  - lowercase letters (`a-z`)
  - uppercase letters (`A-Z`)
  - digits (`0-9`)
  - symbols (`.!@#$%^&*()_+-=;/`)
- **Optional saving to file** with your details
- **Generate again** option (the program can loop and generate another password)

## Project Structure

```
Password-Generator-Pure-Python/
  main.py
  README.md
```

## Requirements

- Python **3.x**
- No external libraries required (only `random` and `time`)

## How to Run

From the `Password-Generator-Pure-Python` folder:

```bash
python main.py
```

## How It Works (Program Flow)

When you run the program, it will:

1. Ask for the **length** of password you want.
2. Generate a random password using the defined character set.
3. Ask if you want to **save the password in a file** (`yes/no`).
4. Ask for:
   - your **name**
   - the **application/purpose** you are using the password for
5. If you answered **yes**, it creates a file named:
   - `password_<name>_<purpose>_<length>.txt`
6. It then asks whether you want to **generate another password** (`yes/no`).

## Example Run

Example input/output (your password will be different every time):

```text
Let's Begin...
Enter the length of password you want to generate: 12
Generating password...
Password generated successfully!
Do you want to save the password in the file (yes/no): no
Enter your name: Ayush
Enter the application in which you are using the password: Gmail
Saving your details...
 Hy Ayush,
Your password has been creatd successfully for your Gmail
 Password: aZ8!nQ2$kP;1
 Thank you for using the password generator and have your password safe from others eyes. Use your password wisely and do not share it with anyone
Please wait for a while!
Do you want to generate another password (yes/no): no
Processing...
It will take few seconds, please wait....!
Thank you for using the password generator, see you next time!
```

## Notes

- **Length must be a number**. If you enter something that isn’t an integer (or a negative number), Python will raise an error.
- If you choose to save (`yes`), the `.txt` file is created in the **same folder** where you run `main.py`.

## Security Tips

- Don’t share your passwords with anyone.
- Prefer longer passwords (12–16+ characters).
- Use a password manager for storing passwords safely.

## License

This project is free to use for learning and personal use.