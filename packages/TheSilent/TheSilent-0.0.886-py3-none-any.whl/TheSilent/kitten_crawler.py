import re
import time
import urllib.parse
from TheSilent.clear import clear
from TheSilent.puppy_requests import text

CYAN = "\033[1;36m"

def kitten_crawler(host,delay=0):
    clear()
    hits = [host]
    total = []
    depth = -1
    while True:
        depth += 1
        hits = list(dict.fromkeys(hits[:]))
        try:
            if urllib.parse.urlparse(host).netloc in urllib.parse.urlparse(hits[depth]).netloc or ".js" in hits[depth]:
                valid = bytes(hits[depth],"ascii")
                time.sleep(delay)
                print(CYAN + hits[depth])
                data = text(hits[depth])
                total.append(hits[depth])

        except IndexError:
            break

        except:
            continue

        try:
            links = re.findall("content\s*=\s*[\"\'](\S+)(?=[\"\'])|href\s*=\s*[\"\'](\S+)(?=[\"\'])|src\s*=\s*[\"\'](\S+)(?=[\"\'])",data.lower())
            for link in links:
                for _ in link:
                    _ = re.split("[\"\'\<\>\;\{\}]",_)[0]
                    if _.startswith("/") and not _.startswith("//"):
                        hits.append(f"{host}{_}")

                    elif not _.startswith("/") and not _.startswith("http://") and not _.startswith("https://"):
                        hits.append(f"{host}/{_}")

                    elif _.startswith("http://") or _.startswith("https://"):
                        hits.append(_)

        except:
            pass

    hits = list(dict.fromkeys(hits[:]))
    hits.sort()
    results = []
    for hit in total:
        try:
            if urllib.parse.urlparse(host).netloc in hit:
                valid = bytes(hit,"ascii")
                results.append(hit)

        except UnicodeDecodeError:
            pass

    clear()
    return results
