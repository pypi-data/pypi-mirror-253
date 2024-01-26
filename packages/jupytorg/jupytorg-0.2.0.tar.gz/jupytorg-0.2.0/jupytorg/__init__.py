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
    :returns: the parsed parameters (src_file, dest_file, code_type)
    :rtype: tuple[str]
    """
    src_file = ""
    dest_file = ""
    code_type = ""
    if len(args) <= 1:
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
                case "type":
                    code_type = arg[1]
                case _:
                    raise SystemExit("Unknown argument : " + i)
    return (src_file, dest_file, code_type)

def __code_node_analysis(node) -> list[dict[str, ]]:
    """Analyses a code node

    :param node: the code node to compile
    :type node: Any
    :returns: a list of json cells
    :rtype: list[dict[str, Any]]
    """
    imports = ""
    encapslation_start = ""
    encapslation_end = ""
    flags = ""
    if node.attrs.get("data-results", [""]) == "file":
        cell_code = {
                "cell_type": "code",
                "source": [flags+node.get_text()],
                "execution_count": 0,
                "outputs": [],
                "metadata": {
                    "vscode": {
                        "languageId": str(node.attrs.get("data-org-language", [""]))
                    }
                }
            }
        # text equivalent to an image in markdown
        image = "!["+str(node.attrs.get("data-file", [""]))+"]("+str(node.attrs.get("data-file", [""]))+")"
        cell_image = {"cell_type": "markdown", "source": [image], "metadata": {}}
        return [cell_code, cell_image]
    else:
        code_modified = node.get_text()
        if node.attrs.get("data-includes", [""]) != [''] and node.attrs.get("data-org-language", [""]) == 'C':
            # already specified imports
            imports += "".join(list(map(lambda dep: "#include "+dep+"\n", (node.attrs.get("data-includes", [""])).split()))) + "\n"
        if node.attrs.get("data-org-language", [""]) == 'C':
            # for example, to use OpenMP pragmas:
            flags += "//%cflags:-fopenmp\n"
            # because why the fuck would you use emacs
            imports += "#include <omp.h>\n#include <stdio.h>\n#include <stdlib.h>\n\n"
            encapslation_start = "int main(int argc, char* argv[]){"
            code_modified = '\t'.join(('\n'+code_modified.lstrip()).splitlines(True))
            encapslation_end = "\n}"
        cell_code = {
                "cell_type": "code",
                "source": [flags+imports+encapslation_start+code_modified+encapslation_end],
                "execution_count": 0,
                "outputs": [],
                "metadata": {}
            }
        return [cell_code]

def main():
    nom_fichier_in: str
    nom_fichier_out = "output_file.ipynb"
    type_code = "C"
    temp_file_name = "out.html"

    # Analysis of the arguments given
    (nom_fichier_in, nom_fichier_out, type_code) = __check_args(sys.argv[1:])

    # Convertion from org format to html format
    if not is_pandoc_installed():
        raise SystemExit("Install pandoc to use this script")
    try:
        subprocess.run(["pandoc", nom_fichier_in, "-o", temp_file_name])
    except FileNotFoundError:
        raise SystemExit("Input file not found : " + nom_fichier_in)

    # Reading the content of the html file
    html_file = Path(temp_file_name).read_text()
    # Comment this line to keep the temporary html file
    os.remove(temp_file_name)

    # Parsing the html to retrieve a list of nodes
    document_parsed = bs4.BeautifulSoup(html_file, features="html.parser")

    # The list of the json cells after each node compilation
    cells = []

    # Convert from html format to json ipynb format
    for node in document_parsed.find_all(recursive=False):
        # If we find a code block
        if node.attrs.get("class", [""])[0] == "sourceCode":
            cells += __code_node_analysis(node)
        # If we find an image
        elif node.img:
            cells.append({"cell_type": "markdown", "source": [str(node.img)], "metadata": {}})
        # If we find an example (somewhat equivalent to code)
        elif node.attrs.get("class", [""])[0] == "example":
            cells.append({"cell_type": "code", "source": [(node.get_text()).rstrip()], "metadata": {}})
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
