import time 
import pyodbc
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()

SERVER = 'yoooooooooooo'
DATABASE = 'wam'
USERNAME = 'iampowerful'
PASSWORD = 'supersecretpassword'


connectionString = f'DRIVER={"ODBC Driver 17 for SQL Server"};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};Trusted_Connection=yes;'



if __name__ == "__main__":

    conn = pyodbc.connect(connectionString)
    SQL_QUERY = "SELECT * FROM WhatsAppMessages where sentStatus is null"
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)

    records = cursor.fetchall()

    for r in records:

        

        mssg = r.messagetext
        phn = "91" + r.receiver
        print(f"{r.receiver}\t{mssg}")

        options.add_argument("-profile")
        options.add_argument("C:/Users/Irshad Khatri/AppData/Roaming/Mozilla/Firefox/Profiles/rlyugxw5.default-release-1724559328504")
        driver = webdriver.Firefox(options=options)

        driver.get("https://web.whatsapp.com/send?phone=" + phn)

        time.sleep(20)
        message_box = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]")
        # /html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1] new
        # /html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]     old
        wamessage = mssg

        for mm in wamessage:
            message_box.send_keys(mm)
        time.sleep(1)
        message_box.send_keys(Keys.RETURN)
        
        SQL_QUERY1 = "UPDATE WhatsAppMessages SET sentStatus=1 WHERE idno="  + str(r.idno)
        # "UPDATE WhatsAppMessages SET sentStatus=1 WHERE idno="  + str(r.idno)
        print(SQL_QUERY1)
        cursor.execute(SQL_QUERY1)
        conn.commit()

        time.sleep(5)
        driver.quit()
