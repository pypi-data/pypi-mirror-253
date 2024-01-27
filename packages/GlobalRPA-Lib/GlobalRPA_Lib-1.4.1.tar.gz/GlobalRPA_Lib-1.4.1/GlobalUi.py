import time

def dummy_send(driver, xpath, word, delayInSeconds):    
    for c in word:
        driver.find_element('xpath',xpath).send_keys(c)
        time.sleep(delayInSeconds)

def element_exists(driver, xpath, timeoutInSeconds):
    start_time = time.time()

    while time.time() - start_time < timeoutInSeconds:
        try:
            driver.find_element('xpath', xpath)
            return True
        except Exception as e:
            time.sleep(1)

    return False