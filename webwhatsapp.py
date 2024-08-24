import time 
import pyodbc
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()

SERVER = 'localhost'
DATABASE = 'wmessages'
USERNAME = 'root'
PASSWORD = ''


connectionString = f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'


if __name__ == "__main__":
    print("w")
    conn = pyodbc.connect(connectionString)
    SQL_QUERY = "SELECT * FROM WhatsAppMessages where sentStatus is null"
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)
    records = cursor.fetchall()
    
    for r in records:
        now = datetime.now()
        dttm = now.strftime("%Y%m%d, %H%M%S")
        mssg = r.messagetext + " " + dttm
        phn = "91" + r.receiver
        print(r.reciever, mssg)
        
        options.add_argument("-profile")
        options.add_argument("~/.mozilla/firefox/12g5912d.default-esr")
        driver = webdriver.Firefox(options=options)

        driver.get("https://web.whatsapp.com/send?phone=" + phn)

        time.sleep(20)
        message_box = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]")

        wamessage = mssg

        for mm in wamessage:
            message_box.send_keys(mm)
        time.sleep(1)
        message_box.send_keys(Keys.RETURN)
        time.sleep(5)
        driver.quit()
    