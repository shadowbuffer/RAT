### RAT-8000 : Remote Access Trojan for educational purposes.
:rat: 
**Description:** RAT-8000 is a Remote Access Trojan. Features include: keys logging, capture screenshot(s), send email(s), and remote control. See To-do List for upgrades (WIP). 

I know, I know. Not too many people frown upon a Python being used for malware development, but that's not the point. The point of creating such a project is to learn and build a solid foundation of how  a Remote Access Trojan (RAT) can be engineered from scratch. No, I will not upload any low-level C and assembly language hybrid RATs in the in the future. 

### 1. To-do List
<ol>
  <li>Persistence</li>
  <li>Send screenshots via email</li>
  <li>Reverse Shell</li>
    <li>Communication Module:
      <ol>
        <li>DNS Smuggling </li>
      </ol>
    </li>
  </ol>
  
### 2. Files

1. key_capture.py
   
2. storage.py   

3. context.py
    
4. config.py

5. screenshot.py

6. smtp.py 

9. agent.py 
    
```
Start
    open file
  └─> Initialize hook / listener
        └─> On key event:
              ├─> Capture keystroke + timestamp
              ├─> get active window
              └─> Append to log 
              └─> local and remote grab screen
              └─> send email (f10)
                  └─> clear log file              
  └─> * DNS smuggling (WIP)
  └─> HTTP/HTTPS port 8000: Plain-text JSON ATM (bypasses Windows Defender)
        └─> remote screen grab
              └─> send to email
  └─> On flush interval (5MB):
        └─> Write log file  
Stop
  └─> Unhook listener
  └─> Close log file
```
### 3. Tech Stack (Example: Python)
| Component | Library |
|---|---|
| Key capture | `pynput` or `keyboard` |
| Active window | `pygetwindow` (Windows) |
| File I/O | Built-in `open()` |
| Timestamps | `datetime` module |
| Threading | `threading` module |
| Screenshot | `pyscreenshot` module |
| Smtp | `smtplib` module |
| HTTP | `http.server` module |

### 4. Log File Format (Example)
```
[2026-04-02 10:15:32] [Chrome] H
[2026-04-02 10:15:32] [Chrome] e
[2026-04-02 10:15:33] [Chrome] l
[2026-04-02 10:15:33] [Chrome] l
[2026-04-02 10:15:33] [Chrome] o
[2026-04-02 10:15:34] [Chrome] key.ENTER
```
