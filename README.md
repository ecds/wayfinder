This repository contains data and scripts used in the [Wayfinder Project](https://wayfinder.libraries.emory.edu/), an Emory-led effort to digitize a major bibliography of *African American Newspapers called African American Newspapers and Periodicals: A National Bibliography*.

**africanamericanne00dank_djvu.txt**: Plain text file downloaded from the [copy of the text](https://archive.org/details/africanamericanne00dank) on the Internet Archive.

**bib_raw.txt**: The portion of the text that includes the bibliographic entries.

**make_entries.py**: A script used to create an XML file containing a `<div>` element for each bibliographic entry.

**bib_entries.txt**: The output of the make_entries.py script. This output was subsequentially broken down into one document for each entry.

**prompt.py**: A script used to generate the extracted data files for each bibliographic entry using the ChatGPT API.

