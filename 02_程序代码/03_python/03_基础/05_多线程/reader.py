import os
import uuid
import time
import json
import re
import requests
from bs4 import BeautifulSoup
import concurrent.futures
import logging
from typing import Dict, List
from copy import copy


JINA_API_KEY = os.getenv('JINA_API_KEY')

def read_pages(docs: List[Dict[str, str]], api='jina') ->List[Dict[str, str]]:
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(read_page, doc, api) for doc in docs]
        for future in concurrent.futures.as_completed(futures):
            try:
                results.append(future.result())
            except:
                pass
    return results


def read_page(doc: Dict[str, str], api='damo') -> Dict[str, str]:
    assert doc.get('url', '') != ''
    for _ in range(2):
        try:
            if api == 'jina':
                doc['content'] = read_page_jina(doc['url'])
            else:
                raise ValueError(f'Unknown Readpage Api: {api}')
            return doc
        except Exception as e:
            logging.warning(f'Readpage failed: {str(e)}, retrying')
            time.sleep(1)

    raise ValueError(f'Readpage failed')


def read_page_jina(url: str) -> str:
    headers = {
        'Authorization': f'Bearer {JINA_API_KEY}',
        'X-Timeout': 5,
        'Accept': 'application/json',
        'X-Return-Format': 'text'
    }

    resp = requests.get(f'https://r.jina.ai/{url}')

    if resp.status_code != 200:
        raise Exception(f'Error: {resp.status_code} {resp.text}')
    
    content = resp.text

    try:
        prefix = 'Markdown Content:\n'
        content = content[content.index(prefix)+len(prefix):]
    except:
        pass
    content = re.sub('\[(.+?)\]\(.+?\)', '[\\1]', content)

    return content



if __name__ == '__main__':
    print(read_pages([{'url': 'https://www.pbs.org/newshour/search-results?q=a+timeline+of&pnb=1'}]))
