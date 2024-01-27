"""org to IPYNB converter

This script allows the user to convert an org file to IPYNB (Jupyter Notebook) one.

This file can also be imported as a module and contains the following
functions:

    * usage - returns jupytorg usage documentation
    * is_pandoc_installed - returns wether or not pandoc is installed
    * main - the main function of the script
"""

import json
import subprocess
import sys
import os
from pathlib import Path
import bs4
import json
import re


def usage() -> str:
    """Returns the usage documentation
    
    :returns: the usage documentation
    :rtype: list
    """
    return ("Usage : jupytorg src=input_file_path (optional type=code_block_language dest=output_file_path)\n"
        + "    input_file_path : the path to input the file\n"
        + "    code_block_language : le language des blocks de code (default is C)\n"
        + "    output_file_path : the path to output the file (default is output_file.ipynb)")


def is_pandoc_installed() -> bool:
    """Checks if pandoc is installed via the command `pandoc --version`
    
    :returns: True if installed, False otherwise
    :rtype: boolean
    """
    try:
        subprocess.run(["pandoc", "--version"])
        return True
    except FileNotFoundError:
        return False


def __check_args(args: list[str]) -> tuple[str]:
    """Checks the validity of the arguments and pass then to the rest of the script

    :param args: the arguments for the program **name of the program excluded !!!**
    :type args: list[str]
    :returns: the parsed parameters (src_file, dest_file)
    :rtype: tuple[str]
    """
    src_file = ""
    dest_file = "output_file.ipynb"
    if len(args) < 1:
        raise SystemExit(usage())
    else:
        for i in args:
            if i == "--help":
                raise SystemExit(usage())
            arg = i.split("=")  
            match arg[0]:
                case "src":
                    src_file = arg[1].replace('~', str(Path.home()))
                case "dest":
                    dest_file = arg[1].replace('~', str(Path.home()))
                case _:
                    raise SystemExit("Unknown argument : " + i)
    return (src_file, dest_file)


def __write_file(language: str, files_to_write: tuple[str, dict[str, str]], data_tangle: list[str] , code: str):
    try:
        file_names = files_to_write[1][language]
        block_name = data_tangle[0].split('.')[0]
        if block_name != "" and (block_name in file_names):
            file = open(files_to_write[0]+data_tangle[0], "w")
            file.write(code)
            file.close()
    except KeyError | IndexError:
        pass


def __c_code_analysis(node, language_flags:str, language_imports: str, code: str) -> str:
    """Analyses a C code block
    
    :param node: the code node to analyse
    :type node: Any
    :param language_flags: the language flags for C
    :type language_flags: str
    :param language_imports: the language imports for C
    :type language_imports: str
    :param code: the raw code read from the html
    :type code: str
    :returns: the source code of the block
    :rtype: str
    """
    try:
        data_tangle = [node.attrs['data-tangle']]
    except KeyError:
        data_tangle = [""]
    try:
        data_main = str(node.attrs['data-main'])
    except KeyError:
        data_main = "yes"

    if data_tangle != [""] and data_tangle[0].endswith(".c"):
        if data_main != "no" and re.match("^[ \t]*[intvod]+[ \t\n\r]*main[ \t]*(.*)", code) is None:
            # because why the fuck would you use emacs
            encapslation_start = "int main(int argc, char* argv[]){"
            code_modified = '\t'.join(('\n'+code.lstrip()).splitlines(True))
            encapslation_end = "\n}"
            return language_flags+language_imports+encapslation_start+code_modified+encapslation_end
        else:
            return language_flags + language_imports + code.lstrip()
    else:
        return language_imports + code.lstrip()


def __code_node_analysis(node, flags: dict[str, str], imports: dict[str, str], files_to_write: tuple[str, dict[str, str]]) -> list[dict[str, ]]:
    """Analyses a code node

    :param node: the code node to compile
    :type node: Any
    :param flags: the dictionnary of flags relative to languages to use
    :type flags: dict[str, str]
    :param imports: the list of imports relative to languages to use
    :type imports: dict[str, str]
    :param files_to_write: the list of files to write for each language
    :type files_to_write: tuple[str, dict[str, str]]
    :returns: a list of json cells
    :rtype: list[dict[str, Any]]
    """
    language_flags = ""
    source = ""
    language_imports = ""

    # Checks if there are already defined imports and flags for the language
    language = str(node.attrs.get("data-org-language", [""]))
    try:
        language_imports = imports[language]
    except KeyError:
        imports[language] = ""
        language_imports = ""
    try:
        language_flags = flags[language]
    except KeyError:
        flags[language] = ""
        language_flags = ""
    
    # Checks if there is any tangled data
    try:
        data_tangle = [node.attrs['data-tangle']]
    except KeyError:
        data_tangle = [""]

    # json IPYNB generation
    if node.attrs.get("data-results", [""]) == "file":
        cell_code = {
                "cell_type": "code",
                "source": [language_flags+node.get_text()],
                "execution_count": 0,
                "outputs": [],
                "metadata": {
                    "tags": data_tangle,
                    "vscode": {
                        "languageId": language
                    }
                }
            }
        # text equivalent to an image in markdown
        image = "!["+str(node.attrs.get("data-file", [""]))+"]("+str(node.attrs.get("data-file", [""]))+")"
        cell_image = {"cell_type": "markdown", "source": [image], "metadata": {}}
        return [cell_code, cell_image]
    else:
        code = node.get_text()
        if node.attrs.get("data-includes", [""]) != [''] and language == 'C':
            # already specified imports
            language_imports = "".join(list(map(lambda dep: "#include "+dep+"\n", (node.attrs.get("data-includes", [""])).split()))) + "\n"
        if language == 'C':
            source = __c_code_analysis(node, language_flags, language_imports, code)
            __write_file(language, files_to_write, data_tangle, source)
        if data_tangle == [""] or data_tangle[0] == "no":
            example_code = "```"+language+"\n"+(node.get_text()).rstrip()+"\n```"
            cell_code = {"cell_type": "markdown", "source": [example_code], "metadata": {}}
        else:
            cell_code = {
                    "cell_type": "code",
                    "source": [source],
                    "execution_count": 0,
                    "outputs": [],
                    "metadata": {
                        "tags": data_tangle,
                    }
                }
        return [cell_code]


def __check_file_to_save(language: str, params, files_to_write: tuple[str, dict[str, str]]):
    """Checks if there a files to save  for a list of flags arguments

    :param language: the language targeted
    :type language: str
    :param params: the list of parameters go through
    :type params: Any
    :param files_to_write: the list of files to write for each language
    :type files_to_write: tuple[str, dict[str, str]]
    """
    if language == 'C':
        to_save = False
        for arg in params:
            if arg == "-I.":
                to_save = True
            elif to_save and arg.endswith(".c"):
                try:
                    files_to_write[1][language] += arg.split(".c")[0]
                except KeyError:
                    files_to_write[1][language] = arg.split(".c")[0]
            elif to_save:
                to_save = False


def __c_header_analysis(category_content: list, flags: dict[str, str], imports: dict[str, str], files_to_write: tuple[str, dict[str, str]]):
    """Analyses a c header

    :param category_content: the content of the c header
    :type category_content: list[Any]
    :param flags: the dictionnary of flags relative to languages to update
    :type flags: dict[str, str]
    :param imports: the list of imports relative to languages to update
    :type imports: dict[str, str]
    :param files_to_write: the list of files to write for each language
    :type files_to_write: tuple[str, dict[str, str]]
    """
    language = 'C'
    for property in category_content[2:]:
        params = property.split(' ')
        match params[0]:
            # flags given to the compiler for each C code block
            case "flags":
                flags[language] = "//%cflags:" + (' '.join(params[1:])) + '\n'
                # saving in memory which file to write on disk for the flags to be correct
                __check_file_to_save(language, params, files_to_write)
            case "includes":
                # includes necessary for the flags, eg: -I. aux.c might need a include "aux.h"
                includes = ("".join(list(map(lambda dep: "#include "+dep+"\n", params[1:])))) + '\n'
                imports[language] = includes.replace("<", "\"").replace(">", "\"")


def __rawblocks_analysis(node, flags: dict[str, str], imports: dict[str, str], files_to_write: tuple[str, dict[str, str]]):
    """Analyses RawBlocks

    :param node: the code node to compile
    :type node: Any
    :param flags: the dictionnary of flags relative to languages to update
    :type flags: dict[str, str]
    :param imports: the list of imports relative to languages to update
    :type imports: dict[str, str]
    :param files_to_write: the list of files to write for each language
    :type files_to_write: tuple[str, dict[str, str]]
    """
    content = node['c']
    if content[0] == 'org':
        category = (content[1]).split(": ")[0]
        match category:
            case "#+PROPERTY":
                category_content = list(map(lambda arg: arg.strip(), ((content[1]).split(": ")[1].split(':'))))
                if category_content[0] == "header-args":
                    language = category_content[1]
                    if language == 'C':
                        __c_header_analysis(category_content, flags, imports, files_to_write)
                        

def main():
    nom_fichier_in: str
    nom_fichier_out = ""
    temp_html_file = "out.html"
    temp_json_file = "out.json"
    flags = {}
    imports = {}
    files_to_write: tuple[str, dict[str, str]]

    # Analysis of the arguments given
    (nom_fichier_in, nom_fichier_out) = __check_args(sys.argv[1:])
    if str(Path(nom_fichier_out).anchor) == '':
        files_to_write = ("", {})
    else:
        files_to_write = (str(Path(nom_fichier_out).parent)+str(Path(nom_fichier_out).anchor), {})

    # Convertion from org format to html format
    if not is_pandoc_installed():
        raise SystemExit("Install pandoc to use this script")
    try:
        subprocess.run(["pandoc", nom_fichier_in, "-o", temp_html_file])
        subprocess.run(["pandoc", nom_fichier_in, "-o", temp_json_file])
    except FileNotFoundError:
        raise SystemExit("Input file not found : " + nom_fichier_in)

    # Reading the content of the html file
    html_file = Path(temp_html_file).read_text()
    # Reading the content of the json file
    json_file = json.loads(Path(temp_json_file).read_text())
    # Comment this line to keep the temporary html file
    os.remove(temp_html_file)
    os.remove(temp_json_file)

    # Parsing of the json specific metadatas
    i = 0
    node = json_file['blocks'][i]
    while node['t'] == "RawBlock":
        __rawblocks_analysis(node, flags, imports, files_to_write)
        i += 1
        node = json_file['blocks'][i]

    # Parsing the html to retrieve a list of nodes
    document_parsed = bs4.BeautifulSoup(html_file, features="html.parser")

    # The list of the json cells after each node compilation
    cells = []

    # Convert from html format to json ipynb format
    for node in document_parsed.find_all(recursive=False):
        # If we find a code block
        if node.attrs.get("class", [""])[0] == "sourceCode":
            cells += __code_node_analysis(node, flags, imports, files_to_write)
        # If we find an image
        elif node.img:
            cells.append({"cell_type": "markdown", "source": [str(node.img)], "metadata": {}})
        # If we find an example (somewhat equivalent to code)
        elif node.attrs.get("class", [""])[0] == "example":
            example_code = "```c\n"+(node.get_text()).rstrip()+"\n```"
            cells.append({"cell_type": "markdown", "source": [example_code], "metadata": {}})
        # If we find a plot, for now we pray for an existing compiled output image
        elif node.attrs.get("class", [""])[0] == "gnuplot":
            texte = "!["+str(node.attrs.get("data-file", [""]))+"]("+str(node.attrs.get("data-file", [""]))+")"
            cells.append({"cell_type": "markdown", "source": [texte], "metadata": {}})
        # Else we just found plain old text
        else:
            cells.append({"cell_type": "markdown", "source": [str(node)], "metadata": {}})

    # Writing everything in the output file
    fichier_out = open(nom_fichier_out, "w")
    fichier_out.write(
        json.dumps(
            {
                "cells": cells,
                "metadata": {
                    "kernelspec": {
                        # C language kernelspec with OpenMP support
                        "display_name": "C",
                        "language": "c",
                        "name": "c",
                    },
                    "language_info": {
                        "file_extension": ".c",
                        "name": "c",
                        "mimetype": "text/plain",
                    },
                },
                "nbformat": 4,
                "nbformat_minor": 4,
            }
        )
    )

if __name__ == '__main__':
    main()
