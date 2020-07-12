import configparser
import time
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def collect_property_file_contents(property_file, header):
    u"""
    Collect items from a config file

    :param property_file: The file holding the information to be collected
    :param header: header blocks of elements
    :return:
    """
    try:
        config = configparser.ConfigParser()
        config.read(property_file)
        configuration = config[header]
        return configuration
    except Exception as e:
        print('ERROR: ' + str(e))


def write_to_file(file_path, data, write_type):
    u"""
    Store contents of a string input (data) within a folder of ${PYTHON_HOME}/out

    :param file_path: Relative file path to store output in ${PYTHON_HOME}/out. :"myfile.txt"
    :param data: The content to be written to the file encoded as UTF-8. :"Hello, old friend."
    :param write_type: The file opening procedure. Write/Read/Append... etc. :"w"
    :return: None
    """
    try:
        f = open(str(file_path), write_type, encoding="utf-8")
        f.write(data)
        f.close()
    except Exception as e:
        print(e)


def fetch_pgn(study_id, driver) -> str:
    u"""
    Collect the PGN file for all chapters of a specified Lichess Study. Uses the Selenium driver. Note, the driver
    must have preferences defined that negate popups, warnings, and any other user required field.

    :param study_id: The Lichess study unique identifier. :"PoNcwbK3"
    :param driver: The Selenium WebDriver
    :return: PGN file as a UTF-8 encoded string
    """

    # TODO: This is janky AF. Selenium is not returning after the driver download of the pgn. It times out. IDK why.
    driver.set_page_load_timeout(3)
    try:
        driver.get("https://lichess.org/study/" + study_id + ".pgn")
    except selenium.common.exceptions.TimeoutException:
        print("COMPLETE!")
    except Exception as e:
        print("ERROR! " + str(e))


def get_page_height(driver):
    return driver.execute_script("return document.documentElement.scrollHeight")


if __name__ == "__main__":

    # Get and set property file contents
    properties = collect_property_file_contents('./config.ini', "GENERAL")
    download_directory = properties["download_directory"]
    username = properties["username"]
    password = properties["password"]

    # Setup the Firefox preferences to avoid user input on file downloads
    fp = webdriver.FirefoxProfile()
    fp.set_preference("browser.download.folderList", 2)
    fp.set_preference("browser.download.manager.showWhenStarting", False)
    fp.set_preference("browser.download.dir", download_directory)
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-chess-pgn")

    # Create a Selenium driver and login to Lichess
    driver = webdriver.Firefox(firefox_profile=fp)
    driver.get("https://lichess.org/login?referrer=/study/by/" + username)
    login_form_username = driver.find_element_by_id('form3-username')
    login_form_password = driver.find_element_by_id('form3-password')
    login_form_username.send_keys(username)
    login_form_password.send_keys(password)
    login_button = driver.find_element_by_xpath("//*[@class='submit button']")
    login_button.send_keys(Keys.RETURN)

    # After logging in, scroll to the bottom. This loops due to their infinite scroll class.
    time.sleep(3)
    assert username in driver.title
    height = 0
    while height != get_page_height(driver):
        height = get_page_height(driver)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)

    # Collect and Parse HTML content
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    studies = soup.find_all(class_='study paginated')

    # Clear manifest file
    write_to_file('manifest.csv', '', 'w')

    # For each study download the PGN file.
    for i, study in enumerate(studies):
        study_html_components = study.find('a')
        study_name = study_html_components['href'][7:]
        print('(' + str(i+1) + '/' + str(len(studies)) + '): Capturing study ' + str(study_name) + "... ", end="")

        title = study_html_components['title']
        alphanumeric_filter = filter(str.isalnum, title)
        title_alphanumeric_string = "".join(alphanumeric_filter)

        write_to_file(download_directory+'\\manifest.csv', str(i) + ',' + str(study_name) + ',' + title_alphanumeric_string + ',' + str(title) + '\n', 'a')
        fetch_pgn(study_name, driver)
