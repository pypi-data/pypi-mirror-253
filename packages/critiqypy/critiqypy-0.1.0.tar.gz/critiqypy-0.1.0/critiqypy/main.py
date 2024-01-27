import PySimpleGUI as sg
import shutil
import pathlib
from PIL import Image
import argparse
import io
import json
# import magic
import filetype
import warnings
import vlc
import sys

def normalizeCategoryName(name):
    # if you dont do this, json and filenames that result can become stupid.
    name = name.title()
    keepcharacters = ('.','_')
    return "".join(c for c in name if c.isalnum() or c in keepcharacters).rstrip()

class FileCategorizer:
    def __init__(self, folder_path, destination, categorization_action,categories):
        self.folder_path = pathlib.Path(folder_path)
        self.destination = pathlib.Path(destination)
        self.categorization_action = categorization_action
        self.categories = categories
        # self.categories_clean = [normalizeCategoryName(c) for c in categories]
        self.file_list = list(self.folder_path.glob("*"))
        self.video_played = False
        self.current_file = -1
        if len(self.file_list) == 0:
            if not self.folder_path.exists():
                raise FileNotFoundError(f"The given input folder path '{folder_path}' does not exist")
            else:
                raise FileNotFoundError(f"The given input folder path '{folder_path}' is empty")
        
        sg.theme("DefaultNoMoreNagging")
        layout = [
            [sg.Push(),sg.Text(key="-DESCRIPTION-"),sg.Push()],
            [sg.Image(key="-MEDIA-", size=(900, 900))],
            [sg.Push()]+[sg.Button(c) for c in self.categories] + [sg.Push()]
        ]

        self.window = sg.Window("Critiqypy file organizer", layout, finalize=True)
        self.display_next_file()

        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED:
                break
            elif event in self.categories:
                self.categorize_file(normalizeCategoryName(event))
                self.display_next_file()

        self.window.close()

    def display_next_file(self):
        self.current_file += 1
        try:
            file_path = self.file_list[self.current_file]
        except IndexError:
            # gracefull exit
            print("\n\nCategorization complete")
            sys.exit(0)
        if file_path.is_dir():
            # skip
            warnings.warn(f"Directory found. Skipping!")
            self.display_next_file()
            return None
        try:
            kind_of_file = filetype.guess(file_path).mime
        except AttributeError:
            # this probably means this is text! Could also be some weird binary file, but why would a user try to look at that? Assume it is text, and catch the error later if it is not.
            # Currently not implemented, but would be trivial to do I guess.
            kind_of_file = "text"
        self.window["-DESCRIPTION-"].Update(f"{file_path.name} | {kind_of_file} | {self.current_file} / {len(self.file_list)}")
        if "image" in kind_of_file:
            self._display_image(file_path)
        elif "video" in kind_of_file:
            self._display_video(file_path)
        else:
            warnings.warn(f"File '{file_path.name}' has MIMEtype '{kind_of_file}', which is not implemented. Skipping!")
            self.display_next_file()

    def _display_image(self,image_path):
        self.window["-MEDIA-"].Update(data=None)
        image = Image.open(image_path)
        image.thumbnail((900, 900))
        with io.BytesIO() as output:
            image.save(output, format="PNG")
            data = output.getvalue()
        self.window["-MEDIA-"].Update(data=data)
    
    def _display_video(self,video_path):
        # borrowed from https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Media_Player_VLC_Based.py
        if not self.video_played:
            self.vlc_inst = vlc.Instance()
            self.vlc_list_player = self.vlc_inst.media_list_player_new()
            self.vlc_media_list = self.vlc_inst.media_list_new([])
            self.video_played = True
        self.vlc_media_list.add_media(video_path)
        self.vlc_list_player.set_media_list(self.vlc_media_list)
        self.player = self.vlc_list_player.get_media_player()
        if sys.platform.startswith('linux'):
            self.player.set_xwindow(self.window['-MEDIA-'].Widget.winfo_id())
        else:
            self.player.set_hwnd(self.window['-MEDIA-'].Widget.winfo_id())
        self.vlc_list_player.play()

    def categorize_file(self, category):
        if self.categorization_action in ("copy","move"):
            self._copy_or_move_file(category)
        elif self.categorization_action in ("json"):
            self._cat_to_json(category)
        # clean up if required:
        if self.video_played:
            self.vlc_list_player.pause()
            self.vlc_list_player.stop()
            self.vlc_media_list.remove_index(0)  # Remove the media from the list
            self.player.release()
            self.video_played = False  # Reset the flag
        # self.window["-MEDIA-"].update(data=None) # clear the screen, this does not work for some reason, instead killing any future videos? Pff. Just accept the overlap I guess.
    
    def _cat_to_json(self,category):
        # I load and save everytime, so in case of exit before end of job, data is saved
        try:
            with open(self.destination, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            # this is the first run, create empty file
            data = dict()
        data[self.file_list[self.current_file].as_posix()] = category
        with open(self.destination, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def _copy_or_move_file(self, category):
        self.destination.mkdir(parents=True, exist_ok=True)
        file_name = self.file_list[self.current_file].name
        destination_path = self.destination / file_name
        if self.categorization_action == "copy":
            shutil.copy2(self.file_list[self.current_file], destination_path)
        elif self.categorization_action == "move":
            shutil.move(self.file_list[self.current_file], destination_path)

    def show(self):
        self.window.read()

def parse_arguments():
    parser = argparse.ArgumentParser(
        prog='Critiqypy',
        description="Critiqypy is a File Categorizer Tool. It allows you to quickly view all files in a folder, and categorize them into categories you have defined. A straightforward example is looking through photos quickly, selecting some for printing, while discarding others."
    )
    parser.add_argument("folder_path", help="Path to the folder containing files to categorize")
    parser.add_argument("destination", help="Path to the folder to store categorized pictures, or to the location to save the json with results")
    parser.add_argument('-c','--category', nargs='+', default= ['Yes','No'], help="The categories to split the files into. Defaults to Yes & No, because that is probably what you want anyway. Can be any number you like.")
    actiongroup = parser.add_mutually_exclusive_group(required=False)
    actiongroup.add_argument('-j','--json', action='store_true', default=True, help="Write the categorization to the destination as a json file. Leave the original files alone.")
    actiongroup.add_argument('-cp','--copy', action='store_true', default=False, help="In the destination path, create subfolders with each category and place a //copy// of files in their respective categories")
    actiongroup.add_argument('-mv','--move', action='store_true', default=False, help="In the destination path, create subfolders with each category and //move// files to their respective categories")
    return parser.parse_args()

def main():
    args = parse_arguments()
    if args.move:
        categorization_action = "move"
    elif args.copy:
        categorization_action = "copy" 
    elif args.json:
        categorization_action = "json" 
    else:
        print(args)
        raise ValueError("No categorization action was set!")
    if not args.category:
        categories = ["yes","no"]
    else:
        categories = list(args.category)
    FileCategorizer(args.folder_path, args.destination,categorization_action,categories).show()

if __name__ == "__main__":
    main()

