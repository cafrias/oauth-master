from html2text import HTML2Text

SPEC_FILE_RAW = "data/raw/rfc6749.html"
SPEC_FILE = "data/spec/rfc6749.html"


def spec_to_text():
    print("Reding the spec raw file")
    with open(SPEC_FILE_RAW, "r", encoding="utf-8") as file:
        html_content = file.read()

    print("Converting the spec to text")
    text_marker = HTML2Text()
    text_marker.ignore_links = True

    text = text_marker.handle(html_content)

    print("Writing the spec to file")
    with open(SPEC_FILE, "w", encoding="utf-8") as file:
        file.write(text)

    print("Done")


if __name__ == "__main__":
    spec_to_text()
