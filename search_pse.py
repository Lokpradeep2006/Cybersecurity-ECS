from googleapiclient.discovery import build

def search(query, api_key, search_engine_id):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=query, cx=search_engine_id).execute()
    return res['items']

if __name__ == "__main__":
    api_key = "******************************"
    search_engine_id = "064a17498abfb4375"
    query = "cybersecurity vulnerabilities"

    results = search(query, api_key, search_engine_id)
    for result in results:
        print(result['title'])
        print(result['snippet'])
        print(result['link'])
        print()

