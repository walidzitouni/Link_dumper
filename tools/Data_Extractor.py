import requests
import json
import re



def request(Link):
    try:
        Request = requests.get(f'{Link}', verify=True)
        if Request.status_code == 200:
            js_text = Request.text # extract js fcontent working with BS dfficult cause it fetch HTML
            # print(soup)
            #print("Fetched JS Content:\n", js_text[:500])
            result1, api_keys = grep(js_text)

            if result1 :
                saving(result1)
            if api_keys:
                save_api_keys(api_keys)
    except Exception as error:
        print(f"Error in URL: {error}")

#----------- Regular expressions--------
def grep(soup):

    regular_expressions1=r'[^.{50}\n,{]*[\'"\s]?v?\d+\.\d+\.\d+[\'"\s]?'
    regular_expressions2 = r'(?<=["\'])[A-Za-z0-9_-]{32,}[\'"]'
    result1=re.findall(regular_expressions1, soup)
    api_keys = re.findall(regular_expressions2, soup)
    # print(f"Matches found: {result}")
    return result1,api_keys


#------Saving (e.g., version numbers)--------#.....--------#
def saving(file_name):
    with open('sensetive_info.json','w') as json_file:
        json.dump(file_name, json_file,indent=4)

#------Saving API keys in a separate file--------#
def save_api_keys(api_keys):
    with open('api.json', 'w') as api_file:
        json.dump(api_keys, api_file, indent=4)

#-------------extract links from js file-------------#

def link_by_link(file):
    try:
        with open(file, 'r') as jsonfile:
            links = json.load(jsonfile)

        # Process each link
        for link in links:
            request(link)

    except Exception as error:
        print(f"Error reading the file: {error}")
#-----------main---------------#
link_by_link('file_js.json') #The file PATH://
