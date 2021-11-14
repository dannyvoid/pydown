import requests, os
from pathlib import Path
from tqdm import tqdm


def download(url):
    file_name = url.split("/")[-1]
    file_name = os.path.join("downloads/", file_name)
    if not os.path.exists(file_name):
        get_response = requests.get(url, stream=True)
        total_size_in_bytes= int(get_response.headers.get('content-length', 0))
        block_size = 1024
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        with open(file_name, "wb") as f:
            for data in get_response.iter_content(block_size):
                progress_bar.update(len(data))
                f.write(data)
        progress_bar.close()
        if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
            print("ERROR, something went wrong")


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
            with open(l) as f:
                total_links = sum(1 for _ in f)
            with open(l) as links:
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
