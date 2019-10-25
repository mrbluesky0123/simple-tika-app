import uploader
import parser
import watcher
import constants

def main():
    # Get file list
    file_list = watcher.get_file_list()

    # Get contents
    contents_list = parser.get_contents(file_list)

    # Upload contents
    uploader.upload_contents(contents_list)


if __name__ == '__main__':
    main()