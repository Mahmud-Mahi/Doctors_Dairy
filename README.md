# 🩺 Doctor's Diary – Patient Form Assistant

**Doctor's Diary** is a lightweight and customizable desktop app designed for doctors to efficiently record and manage patient data. With support for theming and customizable form labels, it helps reduce paperwork and streamline decision-making.

---

## ✨ Features

- 📝 Create and save patient records with symptoms and diagnosed diseases  
- 🎨 Switch between light/dark themes or set your own color scheme  
- 🧩 Customize form labels to match your preferred language or workflow  
- 📁 Each patient's file is saved individually for easy access and management  
- 🖥️ Works on **Windows**, **Linux**, and **macOS**

---

## 📦 Installation

### 🔷 Windows
1. Download the latest `Windows` zip file from the [Releases](https://github.com/your-username/doctors-diary/releases) page.
2. Extract the file & place the `.exe` file according to your convenience.
3. Double-click to run, directly—no setup required.
4. On first run, the app will create a config directory at: C:\Users<YourName>\AppData\Roaming\doctors_diary\

### 🟢 Linux
1. Download the latest `Linux` zip file from the [Releases](https://github.com/your-username/doctors-diary/releases) page.
2. Extract the file & place the `Doctor's Diary` app according to your convenience, but my suggestion is to place the app in `desktop` folder.
3. (Optional) Open terminal in the extracted file & run the command:
```bash
mv icon.png ~/.config/doctors_diary/
```
5. To add a `Desktop Entry` run:
```bash
nano ~/.local/share/applications/doctors_diary.desktop
```
6. Paste the following content & edit `your-username`
``` bash
[Desktop Entry]
Version=1.0.0
Type=Application
Name=Doctor's Diary
Exec=/home/your-username/desktop/Doctors_Diary-v1.0.0
Icon=/home/your-username/.config/doctors_dairy/icon.png
Comment=Patient form assistant for doctors
Categories=Utility;Medical;
Terminal=false
```
7. Make it excutable:
``` bash
chmod +x ~/.local/share/applications/doctors_diary.desktop
```
8. Now search for Doctor's Diary in your `app launcher` or `menu`

---

### ⚙️ Developer Notes
1. If you want to customize or update the script paste the following command:
```bash
git clone https://github.com/your-username/doctors-diary.git
cd doctors-diary
python main.py
```
2. This app uses `PySide6` for GUI. To run locally:
``` bash
pip install PySide6
```
3. If you're editing UI elements, use `Qt Designer` to modify .ui files and convert them using:
``` bash
pyside6-uic main_gui.ui -o main_gui.py
```

### 📜 License
This project is licensed under the **GNU GENERAL PUBLIC LICENSE** – see the [LICENSE](https://github.com/Mahmud-Mahi/Doctors_Diary/blob/master/LICENSE) file for details.

### Contribute & Issues
Feel free to contribute by submitting pull requests. If you encounter any issues, open a ticket in the GitHub **Issues** section.

