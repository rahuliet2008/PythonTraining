def print_stars_line_length_ten():
    line = '*' * 10
    print(line)

def print_stars_line(length):
    line = '*' * length
    print(line)

def print_line(length, character):
    line = character * length
    print(line)

def pretty_print_person(first_name, last_name):
    print("Voornaam:", first_name)
    print("Achternaam:", last_name)

def indent(content, spaces):
    space = ' ' * spaces
    indented = space + content
    return indented


def as_xml(content, tag_name):
    xml='<' + tag_name + '>' + content + '</' + tag_name + '>'  # fixture
    return xml


def main():
    line_length = 25
    print_stars_line_length_ten()
    print_stars_line(line_length)
    print_stars_line(line_length + 5)
    char = '#'
    print_line(line_length, character="%")
    print_line(length=line_length, character=char)
    f_name = "Guido"
    l_name = "van Rossum"
    pretty_print_person(f_name, l_name)
    name = "Paris"
    ip = "10.0.0.135"
    xml_name = as_xml(name, "name")
    xml_ip = as_xml(ip, "ip4")
    print( indent(xml_name,3) )
    print( indent(xml_ip, 4))



if __name__ == "__main__":
    main()
