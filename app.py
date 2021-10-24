import requests, os
from pathlib import Path


def download(url):
    get_response = requests.get(url, stream=True)
    file_name = url.split("/")[-1]
    file_name = os.path.join("downloads/", file_name)
    with open(file_name, "wb") as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)


def main():

    l = "urls.txt"
    path = Path(l)
    
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    if path.is_file():
        if os.stat(l).st_size == 0:
            print(f"please fill {l} with *valid* direct links to files *ONLY*")
        else:
            link_ = 0
            with open(l) as links:
                total_links = sum(1 for _ in links)
                for line in links:
                    line = line.strip("\n")
                    line = line.strip("\t")
                    url = line.split("/")[-1]
                    link_ += 1
                    print(f"downloading {url}")
                    download(line)
                    print(f"downloaded {link_} of {total_links} files\n")
    else:
        with open("urls.txt", "w") as f:
            f.write("please fill this file with *valid* direct links to files *ONLY*\n")
            f.write("this is a quick and dirty batch downloader\n")
            f.write("implying no url validation of any kind\n")
            f.write("or really any error checking of any kind\n")
            f.write("this might erase your list idk\n")
            f.write("backup all your links yourself\n")
            f.write("use at your own risk.")

        print(f"please fill {l} with *valid* direct links to files *ONLY*")


if __name__ == "__main__":
    main()
    os.system("pause")
