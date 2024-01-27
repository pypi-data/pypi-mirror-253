# Critiqypy

Critiqypy is a simple File Categorizer Tool. It allows you to quickly view all files in a folder, and categorize them into categories you have defined. A straightforward example is looking through photos quickly, selecting some for printing, while discarding others.

I created this simple application, because I need to sort a lot of images and videos manually; I have a large amount of microscopy data, and it is easy to see whether further analysis is worth it by eye. Therefore, simply looking at all images and/or movies and manually separating them one-by-one became annoying, and I wrote this super-simple script to just go through all files.

## Usage

On the command line, simply run `critiqypy <path to folder with files to categorize> <path where to put the result>`.
More advanced options are given in the help menu (also shown below). A typical, more complicated example is:

```bash
critiqypy -cp /path/to/images/ /path/to/output/folder -c Bad Meh Good "Absolutely fantastic"
```

which will show you the images in `/path/to/images/` one by one, allowing you to sort them into one of the categories (Bad, Meh, Good, and Absolutely fantastic). When you sort an image into 'meh', a copy of the image is placed in `/path/to/output/folder/meh`.

```text
usage: Critiqypy [-h] [-c CATEGORY [CATEGORY ...]] [-j | -cp | -mv] folder_path destination

positional arguments:
  folder_path           Path to the folder containing files to categorize
  destination           Path to the folder to store categorized pictures, or to the location to save the json with results

options:
  -h, --help            show this help message and exit
  -c CATEGORY [CATEGORY ...], --category CATEGORY [CATEGORY ...]
                        The categories to split the files into. Defaults to Yes & No, because that is probably what you want anyway. Can be any number you like.
  -j, --json            Write the categorization to the destination as a json file. Leave the original files alone.
  -cp, --copy           In the destination path, create subfolders with each category and place a //copy// of files in their respective categories
  -mv, --move           In the destination path, create subfolders with each category and //move// files to their respective categories
```

## Limitations

Currently, this script can only handle video and image files. Extending things shouldn't be too difficult (?), but I personally don't need it. I checked that the script runs on a Linux machine, the code *should* work on Windows and Mac as well, but your mileage may vary.

Internally, I use VLC to display movies, so any video that VLC can show should work. Images are handled by Pillow.


## Installation

Before installing this package, note that we use [VLC media player](https://www.videolan.org/vlc/) to display videos. If VLC is not installed, this script will not work. If VLC installed, simply install this package using your favourite python package installer, probably:

```
pip install critiqypy
```
