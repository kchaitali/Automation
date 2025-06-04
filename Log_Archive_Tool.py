import os
import shutil
import tarfile
import sys
from datetime import datetime

# Function to copy only .log files to a backup folder
def backup_logs(source_directory, backup_directory):
    if not os.path.exists(backup_directory):
        os.mkdir(backup_directory)
    for filename in os.listdir(source_directory):
        if filename.endswith(".log"):
            shutil.copy2(
                os.path.join(source_directory, filename),
                os.path.join(backup_directory, filename)
            )
    print(f"Copied .log files to backup folder: {backup_directory}")

# Function to create a tar.gz archive from the backup folder
def make_tarfile(output_filename, source_directory):
    try:
        with tarfile.open(output_filename, "w:gz") as tar:
            for filename in os.listdir(source_directory):
                if filename.endswith(".log"):
                    filepath = os.path.join(source_directory, filename)
                    if os.path.isfile(filepath):
                        tar.add(filepath, arcname=filename)
                        print(f"Added {filename} to archive.")
        print(f"Archive created: {output_filename}")
    except Exception as e:
        print(f"Error while creating archive: {e}")

# Function to write the archive action to a log file
def log_archive_action(log_file_path, message):
    with open(log_file_path, "a") as log_file:
        log_file.write(message + "\n")

# Main function: drives the backup and archive process
def main():
    # Check command line argument
    if len(sys.argv) < 2:
        print("Usage: python log_archive_tool.py <log-directory>")
        sys.exit(1)

    # Get the log directory from command line
    source_directory = sys.argv[1]

    # Validate path
    if not os.path.isdir(source_directory):
        print(f"Error: {source_directory} is not a valid directory.")
        sys.exit(1)

    # Timestamp for folder and archive naming
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 📁 Define backup and output paths
    backup_directory = f"{source_directory.rstrip('/')}_backup"
    archive_filename = f"logs_archive_{timestamp}.tar.gz"
    log_file_path = "archive_log.txt"  # Log file to track actions

    # Perform backup and archive
    backup_logs(source_directory, backup_directory)
    make_tarfile(archive_filename, backup_directory)

    # Record the archive operation
    log_message = f"{timestamp}: Archived logs from {source_directory} into {archive_filename}"
    log_archive_action(log_file_path, log_message)

# Ensures this only runs when executed directly, not on import
if __name__ == "__main__":
    main()
