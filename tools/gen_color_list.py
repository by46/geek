import xml.etree.ElementTree as ET


def main(xml_full_path):
    import re
    with open(xml_full_path, 'rb') as reader:
        root = ET.fromstring(reader.read())
        for tr in root:
            label = tr.find("td/a/span")
            color = tr.find("td/div/p/span")
            text = label.text
            if not text:
                continue
            color_label = color.get("data-source")[-9:]  # type: str
            if color_label.startswith("#"):
                text = re.sub(r"([A-Z])", r"_\1", text.strip(" \n"))
                text = text[1:].lower()
                # print("\"{0}\": {{ 0x{1}, 0x{2},0x{3},0x{4}}},".format(text, color_label[3:5], color_label[5:7], color_label[7:9], color_label[1:3]))
                print(text, '#'+color_label[3:])

if __name__ == '__main__':
    import re
    print(re.sub(r"([A-Z])", r"_\1", "AndB"))
    main("data.xml")
