---
title: Download Files with Requests
date: September 6, 2025
tags: python
---

The Requests package can be used to download a file using the URL of the file's remote location. The example below loops through a list of URLs and downloads each file one-by-one. While this is fine for one or two files, it can be slow when downloading multiple large files because only one downlaod occurs at a time.

```python
import requests
from pathlib import Path


def download_file(url: str) -> Path:
    """Download a single file and save it to the downloads directory."""

    # Save files to the `downloads` directory
    download_dir = Path("downloads")
    download_dir.mkdir(parents=True, exist_ok=True)

    filename = download_dir / Path(url).name

    response = requests.get(url)
    response.raise_for_status()

    with open(filename, "wb") as f:
        f.write(response.content)

    return filename


def main():
    """Run the example."""

    # List of URLs to download
    urls = [
        "https://sample-files.com/downloads/data/csv/large-dataset.csv",
        "https://sample-files.com/downloads/data/csv/mixed-types.csv",
        "https://sample-files.com/downloads/data/csv/quoted-fields.csv",
        "https://sample-files.com/downloads/data/csv/international.csv",
        "https://sample-files.com/downloads/data/xml/large-dataset.xml",
        "https://sample-files.com/downloads/documents/pdf/sample-report.pdf",
        "https://sample-files.com/downloads/images/jpg/landscape_hires_4000x2667_6.83mb.jpg",
    ]

    for url in urls:
        saved = download_file(url)
        print("Downloaded ->", saved)


if __name__ == "__main__":
    main()
```

In this example, the downloads are performed in parallel using a thread pool executor. This will significantly decrease the overall download time since more than one file is downloaded at a time. On a 1 Gb/s internet connection, this parallel example took about 18 seconds to download all the files compared to the previous example which took 65 seconds.

```python
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


def download_file(url: str) -> Path:
    """Download a single file and save it to the downloads directory."""

    # Save files to the `downloads` directory
    download_dir = Path("downloads")
    download_dir.mkdir(parents=True, exist_ok=True)

    filename = download_dir / Path(url).name

    response = requests.get(url)
    response.raise_for_status()

    with open(filename, "wb") as f:
        f.write(response.content)

    return filename


def main():
    """Run the example."""

    # List of URLs to download
    urls = [
        "https://sample-files.com/downloads/data/csv/large-dataset.csv",
        "https://sample-files.com/downloads/data/csv/mixed-types.csv",
        "https://sample-files.com/downloads/data/csv/quoted-fields.csv",
        "https://sample-files.com/downloads/data/csv/international.csv",
        "https://sample-files.com/downloads/data/xml/large-dataset.xml",
        "https://sample-files.com/downloads/documents/pdf/sample-report.pdf",
        "https://sample-files.com/downloads/images/jpg/landscape_hires_4000x2667_6.83mb.jpg",
    ]

    # Run downloads in parallel
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(download_file, url): url for url in urls}
        for future in as_completed(futures):
            saved = future.result()
            print("Downloaded ->", saved)


if __name__ == "__main__":
    main()
```

## Further reading

See the [docs](https://requests.readthedocs.io/en/latest/) for more information about the Requests package. See Python's [concurrent futures](https://docs.python.org/3/library/concurrent.futures.html) documentation for more info about the thread pool executor.

