from constants import ALLOWED_OUTPUT_FILE_EXTENSIONS
from scraper import get_list_of_available_urls


def validate_command_inputs(sys_argv):

    if len(sys_argv) > 3:
        print('Command has too much arguments.')
        quit()
    elif len(sys_argv) < 3:
        print('Command has less arguments than expected.')
        quit()

    validate_given_url(sys_argv[1])
    validate_given_filename(sys_argv[2])

def validate_given_url(url):

    urls_list = get_list_of_available_urls()

    if url not in urls_list:
        print('Given invalid url.')
        quit()

def validate_given_filename(filename):
    
    try:
        name, extension = filename.split('.')
    except ValueError:
        print('The given file name has wrong format. The format should be: file_name.csv.')
        quit()

    if extension not in ALLOWED_OUTPUT_FILE_EXTENSIONS:
        print('The given file name for the output has wrong extension. Allowed extensions: %s.' % ', '.join(ALLOWED_OUTPUT_FILE_EXTENSIONS))
        quit()
    
    return filename