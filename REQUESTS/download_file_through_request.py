import requests
from tqdm import tqdm   #download this lib using command pip install tqdm --user on command prompt


url="https://download-cdn.jetbrains.com/python/pycharm-professional-2023.2.exe"   #Enter URL
r=requests.get(url , stream=True)             # Use get request to get the url from the server and stream=True for streaming the downloading of the url
totalBytes = int(r.headers["Content-Length"])     # Content length provides the total bytes of the url downloading

currentBytes = 0  #instantiate current bytes to zero

progress = tqdm(total=totalBytes,unit='iB',unit_scale=True)  #TQDM lib os used to show the downloadng bar for downloads

with open("pycharm.exe", 'wb') as f:  # Now will open the downloaded file as file in write mode(wb)
    for chunk in r.iter_content(chunk_size=128):   #This will increment the loop by 128 till total bytes
        progress.update(currentBytes)
        f.write(chunk)
        currentBytes += 128

progress.close()
