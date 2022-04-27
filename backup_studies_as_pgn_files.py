import time
from bs4 import BeautifulSoup
import urllib.request
import os


def write_to_file(file_path, data, write_type):
    """
    Store contents of a string input (data) within a folder of ${PYTHON_HOME}/out

    :param file_path: Relative file path to store output in ${PYTHON_HOME}/out. :"myfile.txt"
    :param data: The content to be written to the file encoded as UTF-8. :"Hello, old friend."
    :param write_type: The file opening procedure. Write/Read/Append... etc. :"w"
    :return: None
    """
    try:
        f = open('./out/' + str(file_path), write_type, encoding="utf-8")
        f.write(data)
        f.close()
    except Exception as e:
        print(e)


def fetch_pgn(study_id, max_tries=2):
    """
    Collect the PGN file for all chapters of a specified Lichess Study.
    API URL: https://lichess.org/api

    :param study_id: The Lichess study unique identifier. :"PoNcwbK3"
    :param max_tries: The maximum number of attempts to collect the PGN file. Default=2
    :return: PGN file as a UTF-8 encoded string
    """
    study_contents = '<FAILED TO FETCH CONTENT>'
    for retry in range(max_tries):
        try:
            time.sleep(3)  # Lichess rate limits API calls. Set a small delay to avoid getting blocked.
            with urllib.request.urlopen('https://lichess.org/study/' + study_id + '.pgn') as response:
                study_contents = response.read().decode("utf-8")
        except Exception as e:
            print('RETRYING for study capture: ' + str(study_name))
            continue

    if study_contents == '<FAILED TO FETCH CONTENT>':
        print('FAILED for study capture: ' + str(study_name))

    return study_contents

def fetch_page(study_page, max_tries=2):
    study_contents = '<FAILED TO FETCH CONTENT>'
    print(f'############### page {study_page} ###############')
    for retry in range(max_tries):
        try:
            time.sleep(3)
            with urllib.request.urlopen('https://lichess.org/study/all/hot?page=' + str(study_page)) as response:
                study_contents = response.read().decode("utf-8")
        except Exception as e:
            print('RETRYING for study page: ' + str(study_page))
            continue

    if study_contents == '<FAILED TO FETCH CONTENT>':
        print('FAILED for study page: ' + str(study_page))
        exit()

    return study_contents


if __name__ == "__main__":

    page = 1

    os.makedirs('./out/',exist_ok=True)
    # Clear manifest file
    write_to_file('manifest.csv', '', 'w')

    while True:
        HTML_CODE_TO_REPLACE = fetch_page(page)
        # Parse HTML content
        soup = BeautifulSoup(HTML_CODE_TO_REPLACE, 'html.parser')
        studies = soup.find_all(class_='study paginated')


        for i, study in enumerate(studies):
            study_html_components = study.find('a')
            study_name = study_html_components['href'][7:]
            print('(' + str(i+1) + '/' + str(len(studies)) + '): COMPLETED capture for study ' + str(study_name))

            title = study_html_components['title']
            alphanumeric_filter = filter(str.isalnum, title)
            title_alphanumeric_string = "".join(alphanumeric_filter)

            study_file_name = str(title_alphanumeric_string) + "_(" + study_name + ').pgn'
            write_to_file('manifest.csv', str(i) + ',' + str(study_name) + ',' + study_file_name + ',' + str(title) + '\n', 'a')
            write_to_file(study_file_name, fetch_pgn(study_name), 'w+')
        page +=1
