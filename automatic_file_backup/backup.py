import os
import shutil
import datetime
import schedule
import time

source_dir = "/home/swathi/Pictures"
dest_dir = "/home/swathi/Backups"

def copy_folder_dest(source, dest):
    today = datetime.datetime.now()
    dest_dir = os.path.join(dest, str(today))
    try:
        shutil.copytree(source, dest_dir)
        print("folder copied to destination directory")
    except Exception as e:
        print(f"Some exception occured {str(e)}")


schedule.every().day.at("12:28").do(lambda: copy_folder_dest(source_dir, dest_dir))

while True:
    schedule.run_pending()
    time.sleep(60)


