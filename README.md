# 📤 PST to MBOX Converter (Windows Guide)

This guide explains how to convert a .pst file (Outlook format) to .mbox (Thunderbird-compatible) on Windows using readpst.

## 🔧 Prerequisites
1. Download `libpst-0.6.63-w32-bin.zip` from this repository.
2. Extract it to any folder. For example:

    ```plaintext
    C:\Users\YOURNAME\Downloads\libpst
    ```

3. Place your .pst file inside any folder. For example:

    ```plaintext
    C:\Users\YOURNAME\Downloads\myemail\dritancerriEMAIL.pst
    ```

## 🧪 Conversion Steps
1. Open Command Prompt (press `Win + R`, type `cmd`, and hit Enter).
2. Navigate to the bin folder of the extracted ZIP:

    ```cmd
    cd "C:\Users\YOURNAME\Downloads\libpst\bin"
    ```

3. Run the following command to convert your .pst file to .mbox:

    ```cmd
    readpst.exe -r -o "C:\Users\YOURNAME\Downloads\myemail\mbox_output" "C:\Users\YOURNAME\Downloads\myemail\dritancerriEMAIL.pst"
    ```

   - `-r` keeps the folder structure.
   - `-o` specifies the output folder for .mbox files.

## 📁 Output
After running the command, the .mbox files will be located in:

```plaintext
C:\Users\YOURNAME\Downloads\myemail\mbox_output
```
--------------

## ✂️ Splitting MBOX Files (Optional)
Some platforms like Hostinger or Zoho Mail only allow file uploads of up to 250MB at a time. If your .mbox file exceeds this limit, you can use the `file-split.py` script to split it into smaller chunks.

1. Check out the `file-split.py` script in this repository.
2. Run the script with the following command to split your .mbox file:

    ```bash
    python file-split.py "C:\Users\YOURNAME\Downloads\myemail\mbox_output\yourfile.mbox"
    ```

   This will split the `.mbox` file into smaller parts of 250MB or less.

## 📝 Notes
- Do not rename `readpst.exe` or modify the folder structure inside the ZIP.
- This method works entirely offline.
- Tested on Windows 10 & 11.




