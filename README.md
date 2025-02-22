# Link Dumper - Web Crawler for Extracting Links and JavaScript Files
![Alt Text](screenshot.png)

## 📌 Overview
**Link Dumper** is a powerful Python-based web crawler designed for **pentesting and reconnaissance**. It scans websites for URLs and extracts **JavaScript (.js), text (.txt), JSON (.json), and XML (.xml)** files. This is useful for **subdomain enumeration, API key discovery, and security analysis**.

## 🚀 Features
- ✅ **Extracts URLs** from `<a>` and `<script>` tags  
- ✅ **Finds JavaScript files** that might contain sensitive data  
- ✅ **Crawls additional links** recursively for deeper analysis
- ✅ **Extracts API keys & version numbers from JavaScript files**
- ✅ **Saves results in JSON format** for further processing  
- ✅ **Handles relative and absolute links** automatically  
- ✅ **Multi-threaded crawling** for fast performance  

---

## 🛠️ Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/walidzitouni/Link_dumper.git
cd Link-Dumper
````

### **2️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## 📌 Usage

### **Basic Usage**

Run the script and enter a target URL and Select [1]:

```bash
bash main.sh
```

or

```bash
python3 Link_dumper.py
```

For version 2, you can also provide a file with a list of URLs and Select [2]:

```bash
bash main.sh 
```

### **Example Output**

The tool will generate:

- `file_links.json` → Contains extracted links
- `file_js.json` → Contains extracted JavaScript file URLs

---

## 🔥 Features in Detail

### **1️⃣ Crawling & Link Extraction**

- Parses **all `<a>` and `<script>` tags** on a given website.
- Extracts **internal & external URLs**.
- Saves extracted URLs in `file_links.json`.

### **2️⃣ JavaScript File Detection**

- Finds **all JavaScript files (`.js`)**.
- Useful for discovering **API endpoints, hidden parameters, and sensitive data**.
- Saves `.js` file URLs in `file_js.json`.

### **3️⃣ Recursive Crawling**

- Reads URLs from `file_links.json`.
- Recrawls found pages for **deeper enumeration**.
- Avoids duplicate links and saves unique results.

### **4️⃣ Multi-Threading**

- Uses `concurrent.futures` for parallel processing.
- Makes scanning large websites much faster.

---



## ⚠️ Legal Disclaimer

This tool is intended for **educational and ethical security testing purposes only**.  
**Do not use it on websites without explicit permission.**

The author takes **no responsibility** for any misuse of this tool.

---

## 📜 License

**MIT License** - Feel free to use and modify this tool.

---

## 👤 Author

- **Your Name** (`@Napoli1372 aka walidzitouni`)
- LinkedIn: [Your Profile](https://www.linkedin.com/in/walid-zitouni-634809299/)
- Twitter: [Your Profile](https://x.com/walidzitouni04)



---

### **What’s Included:**
✅ Proper Markdown formatting  
✅ Installation, usage, and advanced examples  
✅ Legal disclaimer  
✅ License information  

Would you like **badges (Python version, license, etc.)** or a **contribution guide** added? 🚀
