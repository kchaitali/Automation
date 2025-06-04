# 🗃️ Log Archive Tool
https://github.com/kchaitali/Automation/blob/master/Log_Archive_Tool.py 
A simple Python CLI utility to periodically archive `.log` files from a specified directory. This tool helps keep your system clean by backing up logs into a separate folder and compressing them into a `.tar.gz` archive. Each archive is timestamped and logged for future reference.

---

## 🚀 Features

- Accepts a log directory path from the command line
- Copies only `.log` files into a backup folder
- Archives the backup folder into a compressed `.tar.gz` file
- Records each archive action with a timestamp in a log file
- CLI-friendly and easy to use

---

## 📦 Requirements

- Python 3.6+
- Works on Unix-based systems (macOS, Linux)

---

## 🛠️ Setup

1. Clone the repository:

```bash
git clone git@github.com:kchaitali/Automation.git
cd Automation

##🧪 **Usage**
python log_archive_tool.py <log-directory>

## 📌 **Example**:
python log_archive_tool.py /var/log

This will:

1. Create a /var/log_backup folder (if it doesn’t exist)

2. Copy all .log files from /var/log to /var/log_backup

3. Compress them into logs_archive_YYYYMMDD_HHMMSS.tar.gz

4. Log the action in archive_log.txt

📝 **Log File**
Each time the script runs, it appends a log entry to archive_log.txt in the current directory:

20250602_104500: Archived logs from /var/log into logs_archive_20250602_104500.tar.gz

🔐 **Permissions**
sudo python log_archive_tool.py /var/log

🧠 **Why This Tool?**
System logs grow over time and can fill up disk space. This tool helps:

Retain logs in a compressed, organized way

Remove clutter from primary log folders

Track archiving activity over time

🛡️ **License**
MIT License

👩‍💻 **Author**
Chaitali Kanetkar
🔗 [LinkedIn](www.linkedin.com/in/chaitali-m-kanetkar)

📂 [GitHub](https://github.com/kchaitali)


