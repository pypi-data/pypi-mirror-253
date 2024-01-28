# [BTO]: multi-purpose cli tool (one-script-to-rule-them-all)
# [dev]: A Divinemonk creation!
# [git]: https://github.com/Divinemonk/bto

# [docker]: ...
# [pypi]: 
#  - https://pypi.org/project/bto/
#  - `pip install bto`
# [licence]: MIT

# ==================================================================================================

# [The Story]
#     Initially, 'bto' was a simple script that I used to convert bytes to equivalent readable format,
# so the name 'bto' (bytes to). But as time went on, I added more and more functionalities to it.
# You can find individual scripts for most of the functionalities on the following repo:
# `https:github.com/Divinemonk/program_dumps'. But many other functionalities are not available as
# individual scripts nad are exlcusive to 'bto'.

# [The Idea-Goal]
#     The idea is to make a multi-purpose cli tool that can be used for various purposes, sort of all
# in one tool. The functions are not limited to just one category, but are spread across various
# categories, and it is the solution to the problems I faced while working on various projects in 
# my day to day life.

# [The Playbook]
# ...

# [The Future]
#     I will keep adding more and more functionalities to it as I keep working on various projects
# and face new problems. I will also keep updating the existing functionalities as I learn new things
# will trying to make it as user-friendly as possible, and add documentation.
#     All the contributions are welcome, do follow the guidelines mentioned in the CONTRIBUTING.md and
# CODE_OF_CONDUCT.md files. You can also raise issues if you find any bugs or have any suggestions.
# Would love to hear your feedback and suggestions, by reaching me at my [socials](https://divinemonk.github.io/socials/).

# ==================================================================================================

# [The Usage]
#     ...

# [The Categories]
#     ...

# [To Do List]
#  - [ ] Make each avaliable as a separate module that can be imported and used in other projects
#  - scripts t o add from 'program_dumps' repo:
#    - [ ] logpath   (lp)
#    - [ ] massnamer (massrename - mrn)
#    - [ ] responsor (httpcodechecker - hcc, check from single url or from file, add under network sub-command)
#    - [ ] brrtp     (burp raw reques to python)
#    - [ ] ocr       (optiptical character recognizer)
#    - [ ] mm        (monitor mode, add under network sub-command)

# ==================================================================================================

# [The Code]

# --------------------------------------------------------------------------------------------------

# import the required modules
#  - preinstalled
import argparse # parser()
import math # convert_size()
import psutil # sysinfo(), unique_key()
import platform # sysinfo(), unique_key()
import hashlib # unique_key()
import os # printit(), file_info(), create_directory_tree(), get_file_size(), logpath()
import socket # sysinfo(), unique_key()
import uuid # sysinfo(), unique_key()
import requests # responsor()
import re # sysinfo(), unique_key()
import base64 # unique_key()
import time # logpath()
import sys # brrtp(), ocr()
import random # responsor()
from PIL import Image # (pip install pillow) ocr()
import pytesseract # ocr()
import numpy as np # ocr()
#  - install with pip 
from rich.console import Console # sysinfo(), file_info(), memsizetable()
from rich.table import Table # sysinfo(), file_info(), memsizetable()

# --------------------------------------------------------------------------------------------------

# global variables
version = '1.0.0'

# --------------------------------------------------------------------------------------------------

# common fucntions

def banner():
    print('''
██████╗ ████████╗ ██████╗ 
██╔══██╗╚══██╔══╝██╔═══██╗
██████╔╝   ██║   ██║   ██║
██╔══██╗   ██║   ██║   ██║
██████╔╝   ██║   ╚██████╔╝
╚═════╝    ╚═╝    ╚═════╝ 

[ multi-purpose sys tool ]
''')

# help messages
def help_msg(msg_for):
    banner()
    if msg_for == 'd':
        print('''[usage]: bto [options] / [sub-commands] [sub-command options]

[options]:
  -b, --bytes BYTES    converts bytes to suitable memory size (try `static -t`)
  -i, --sysinfo        prints system info, regardless OS (Win/Linux)
  -u, --uniquekey      get a bto-unique-key (your system specific)
  -v, --version        get version and other details *

[sub-commands]:
    static               display static information
    local                local files & folders related tools
    network              network tools
    logpath              directory tree log generator & searcher

[ A Divinemonk creation! ]
''')
    elif msg_for == 'local':
        print('''[usage]: bto local [options]

[options]:
    -f, --fileinfo FILENAME    returns details of the file specified
    -i, --img2txt FILENAME     convert image to text
    ''')
    elif msg_for == 'static':
        print('''[usage]: bto static [options]

[options]:
    -mst, --memory-sizes-table    Tabular representation of various memory sizes
    -hsc, --http-status-codes     Common HTTP Status Codes & Their Meanings
    ''')
    elif msg_for == 'network':
        print('''[usage]: bto network [options]

[options]:
    -b, --brrtp FILENAME    enter burp raw request file and get its equivalent python requests code
    -r, --responsor FILENAME    displays response code of the url(s) specified in the file
    ''')
    elif msg_for == 'logpath':
        print('''[usage]: bto logpath [options]

[options]:
    -g, --generate    Generate directory tree log
    -q, --query       Search for a file/folder and get its absolute path
    -f, --filename    Specify custom log file name (default is directory_tree_log.txt, optional)
    ''')

# parser (with sub-commands)
def parser():
    # categrization of names
    #   - d_ : default
    #   - s_ : sub-command
    #       - l_ : local
    #       - s_ : static
    #       - n_ : network
    #           - t_ : table
    #       - lp_ : logpath

    # create a parser object
    parser = argparse.ArgumentParser(description='[BTO]: multi-purpose cli tool (one-script-to-rule-them-all)')
    parser.add_argument("-b", "--bytes",  metavar = "BYTES", dest = "d_bytes", help = "converts bytes to suitable memory size (try `static -t`)")
    parser.add_argument("-i", "--sysinfo", action = "store_true", dest = "d_sys", default = False, help = "prints system info, regardless OS (Win/Linux)")
    parser.add_argument("-u", "--uniquekey", action = "store_true", dest = "unikey", default = False, help = "get a bto-unique-key (your system specific)")
    parser.add_argument("-v", "--version", action = "store_true", dest = "version", default = False, help = "Get version and other details *")

    # create sub-commands
    subparsers = parser.add_subparsers(dest="subparser_name")

    # - static
    static_parser = subparsers.add_parser('static', help="display static information")
    static_parser.add_argument("-mst", "--memory-sizes-table", action="store_true", dest="table", default=False, help="Tabular representation of various memory sizes")
    static_parser.add_argument("-hsc", "--http-status-codes", action="store_true", dest="http_status_codes", default=False, help="Common HTTP Status Codes & Their Meanings")

    # - local
    local_parser = subparsers.add_parser('local', help="local files & folders related tools")
    local_parser.add_argument("-f", "--fileinfo", dest = "s_l_filename", metavar = "FILENAME", help = "returns details of the file specified")
    local_parser.add_argument("-i", "--img2txt", dest = "s_l_img2txt", metavar = "FILENAME", help = "convert image to text")

    # - network
    network_parser = subparsers.add_parser('network', help="network tools")
    network_parser.add_argument("-b", "--brrtp", dest = "s_n_brrtp", metavar = "FILENAME", help = "enter burp raw request file and get its equivalent python requests code")
    network_parser.add_argument("-r", "--responsor", dest = "s_n_responsor", metavar = "FILENAME", help = "displays response code of the url(s) specified in the file")

    # - logpath (https://raw.githubusercontent.com/Divinemonk/program_dumps/m41n/logpath.py)
    logpath_parser = subparsers.add_parser('logpath', help="directory tree log generator & searcher")
    logpath_parser.add_argument('-g', '--generate', help="Generate directory tree log", action="store_true", dest="s_lp_generate")
    logpath_parser.add_argument('-q', '--query', help="Search for a file/folder and get its absolute path", dest="s_lp_query", metavar="QUERY")
    logpath_parser.add_argument('-f', '--filename', help="Specify custom log file name (default is directory_tree_log.txt, optional)", dest="s_lp_filename", metavar="FILENAME")

    # return the parsed args and the sub-command
    return parser.parse_args()

# custom print function
def printit(text='', center='', line_up=False, line_down=False, space_up=False, space_down=False, coledt=[0, 0, 0], normaltxt_start='', normaltxt_end='', hide=False, verbose_mode=False, input_mode=False):
    # spacing and line printing: line_up, line_down, space_up, space_down
    # normal text: normaltxt_start, normaltxt_end
    # set color: coledt[style, 49, color] 
        # start color: `~[style;49;colorm`
        # end color: `\033[0m`
        # refer: https://media.geeksforgeeks.org/wp-content/uploads/20201223013003/colorsandformattingsh.png
    # take input: input_mode
    # display: hide, verbose_mode

    if not hide or verbose_mode:
        # get terminal width
        width = os.get_terminal_size().columns

        # printing text
        if space_up: print()
        if line_up: print('⸺'*width)

        print(normaltxt_start, end='')

        new_width = int((width - len(text))/2)
        print(center*new_width, end='')
        print(f'\33[{coledt[0]};{coledt[1]};{coledt[2]}m', end='')
        if input_mode: input_var = input(text)
        else: print(str(text), end='')
        print('\033[0m', end='')
        print(center*new_width)

        print(normaltxt_end, end='')

        if line_down: print('⸺'*width)
        if space_down: print()

        if input_mode: return input_var

# --------------------------------------------------------------------------------------------------

# sub-commands specific functions

# default
# -b, --bytes
def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])

# -i, --sysinfo
def sysinfo():
    uname = platform.uname()
    ram = psutil.virtual_memory()
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    # due to fetching public ip, it takes time to execute
    try: public_ip = requests.get('https://api.ipify.org').text
    except: public_ip = "[err-failed-to-fetch-public-ip]"

    table = Table(title='System Information')

    table.add_column("param")
    table.add_column("value")

    table.add_row('OS', str(uname.system))
    table.add_row('Hostname', hostname)
    table.add_row('Architecture', str(platform.architecture()[0]))
    table.add_row()
    table.add_row('Processor', str(platform.processor()))
    table.add_row("Total RAM", str(convert_size(ram.total)))
    table.add_row("Available RAM", str(convert_size(ram.available)))
    table.add_row()
    table.add_row('Mac Address', str(':'.join(re.findall('..', '%012x' % uuid.getnode()))))
    table.add_row('Private IP', str(ip))
    table.add_row('Public IP', str(public_ip))
    table.add_row()
    table.add_row("Release", str(uname.release))
    table.add_row('Kernel', str(platform.platform()))
    table.add_row('Version', str(uname.version))

    console = Console()
    console.print(table)
    exit()

# -u, --uniquekey
def unique_key():
    system = platform.system().lower() # Windows, Linux, Darwin (macOS)
    machine = platform.machine().replace('_', '') # x86_64, i386, i686
    release = platform.release().replace('.', '').replace('-', '').replace('_', '') # 10, 4.19.128-microsoft-standard
    version = platform.version() # 10.0.19041, #1 SMP Wed Mar 10 15:34:10 UTC 2021
    version_hash = hashlib.sha256(version.encode()).hexdigest()
    # get ram, memory, cpu, gpu, etc
    ram = psutil.virtual_memory().total
    memory = psutil.disk_usage('/').total
    cpu = psutil.cpu_freq().current
    # get mac address
    mac = ':'.join(re.findall('..', '%012x' % uuid.getnode())).replace(':', '')

    unique_key = system + machine + ':' + mac + str((ram + memory)/cpu).rsplit('.', 1)[0] + ':' + version_hash + ':' + release

    unique_key_md5 = hashlib.md5(unique_key.encode()).hexdigest()
    unique_key_sha256 = hashlib.sha256(unique_key.encode()).hexdigest()
    unique_key_base64 = base64.b64encode(unique_key.encode()).decode()

    printit('[ BTO | Unique Key ]', coledt=[7, 49, 37], line_up=True, line_down=True, center=' ', space_up=True)
    printit('[bto-unique-key-start]', coledt=[7, 49, 37])
    printit('\t[orignal]:', normaltxt_end='\t'+unique_key, coledt=[1, 49, 37])
    printit('\n\t[md5]:', normaltxt_end='\t'+unique_key_md5, coledt=[1, 49, 37])
    printit('\n\t[sha256]:', normaltxt_end='\t'+unique_key_sha256, coledt=[1, 49, 37])
    printit('\n\t[base64]:', normaltxt_end='\t'+unique_key_base64, coledt=[1, 49, 37])
    printit('\n[bto-unique-key-end]', coledt=[7, 49, 37], line_down=True)
    printit('[above keys are unique & specific to your system]', center=' ', coledt=[1, 49, 37], line_down=True, space_down=True)

    # table = Table(title='Unique Key')
    # table.add_column("Type")
    # table.add_column("Value")
    # table.add_row('Original', unique_key)
    # table.add_row('MD5', unique_key_md5)
    # table.add_row('SHA256', unique_key_sha256)
    # table.add_row('Base64', unique_key_base64)
    # console = Console()
    # console.print(table)
    exit()

# local
# -f, --fileinfo
def file_info(filename):
    stats = os.stat(filename)

    table = Table(title=filename)

    table.add_column("Details")
    table.add_column("Data")

    table.add_row("Access date", time.ctime(stats.st_atime))
    table.add_row("Last modified date", time.ctime(stats.st_mtime))
    table.add_row("Creation date", time.ctime(stats.st_ctime))
    table.add_row()
    table.add_row("Size", str(convert_size(stats.st_size)))
    table.add_row("Owner id", str(stats.st_uid))
    table.add_row("Group id", str(stats.st_gid))
    table.add_row()
    table.add_row("Type and permissions", str(stats.st_mode))
    table.add_row("Inode number", str(stats.st_ino))
    table.add_row("Device id", str(stats.st_dev))
    table.add_row("No. of hard links", str(stats.st_nlink))

    console = Console()
    console.print(table)
    exit()

# -i, --img2txt
def ocr(filename):
    # Read image
    image = Image.open(filename)

    # Convert image to numpy array
    image = np.array(image)

    # Convert image to text using pytesseract
    text = pytesseract.image_to_string(image, lang='eng')

    # Print text
    printit('[ BTO | OCR ]', coledt=[7, 49, 37], line_up=True, center=' ', space_up=True)
    printit(text, line_up=True, line_down=True, coledt=[1, 49, 37], space_down=True)
    exit()


# static
# -mst, --memory-sizes-table
def memsizetable():
    table = Table(title="Tabular Representation of various Memory Sizes")

    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Equal To", style="magenta")
    table.add_column("Size(in bytes)", style="green")
    table.add_column("Shorthand", style="yellow")

    table.add_row('Bit', '1 Bit', '0.125', 'b')
    table.add_row('Byte', '8 Bits', '1', 'B')
    table.add_row('Kilobyte', '1024 B', '1024', 'KB')
    table.add_row('Megabyte', '1024 KB', '1048576', 'MB')
    table.add_row('Gigabyte', '1024 MB', '1073741824', 'GB')
    table.add_row('Terrabyte', '1024 GB', '1099511627776', 'TB')
    table.add_row('Petabyte', '1024 TB', '1125899906842624', 'PB')
    table.add_row('Exabyte', '1024 PB', '1152921504606846976', 'EB')
    table.add_row('Zettabyte', '1024 EB', '1180591620717411303424', 'ZB')
    table.add_row('Yottabyte', '1024 ZB', '1208925819614629174706176', 'YB')

    console = Console()
    console.print(table)
    exit()

# -hsc, --http-status-codes
def httpstatuscodes():
    printit(line_up=True, space_up=True)
    table = Table(title="HTTP Status Codes Categorization")

    table.add_column("Category", no_wrap=True)
    table.add_column("Status Codes")

    table.add_row('1xx', 'Informational Response')
    table.add_row('2xx', 'Success')
    table.add_row('3xx', 'Redirection')
    table.add_row('4xx', 'Client Errors')
    table.add_row('5xx', 'Server Errors')

    console = Console()
    console.print(table)

    printit(line_up=True, space_up=True)
    table = Table(title="Top Common HTTP Status Codes")

    table.add_column("Status Code", no_wrap=True)
    table.add_column("Meaning")

    table.add_row('200', 'OK')
    table.add_row('201', 'Created')
    table.add_row('202', 'Accepted')
    table.add_row('204', 'No Content')
    table.add_row('301', 'Moved Permanently')
    table.add_row('302', 'Redirect')
    table.add_row('304', 'Not Modified (RFC 7232)')
    table.add_row('400', 'Bad Request')
    table.add_row('401', 'Unauthorized (RFC 7235)')
    table.add_row('403', 'Forbidden')
    table.add_row('404', 'Not Found')
    table.add_row('405', 'Method Not Allowed')
    table.add_row('408', 'Request Timeout')
    table.add_row('429', 'Too Many Requests (RFC 6585)')
    table.add_row('500', 'Internal Server Error')
    table.add_row('501', 'Not Implemented')
    table.add_row('502', 'Bad Gateway')
    table.add_row('503', 'Service Unavailable')
    table.add_row('504', 'Gateway Timeout')
    table.add_row('505', 'HTTP Version Not Supported')

    console = Console()
    console.print(table)
    printit(line_up=True, space_up=True, space_down=True)
    exit()


# network
# -b, --brrtp
def brrtp(filename):
    # Read the file
    try:
        with open(filename, 'r') as f:
            data = f.read()
    except FileNotFoundError:
        printit("[BTO | BRRTP] FILE NOT FOUND!", coledt=[7, 49, 31], line_down=True, center=' ', line_up=True)
        exit()

    try:
        # Split the file into headers and body
        headers, body = data.split('\n\n')
    except ValueError:
        # If there is no body, set body to empty string
        headers = data
        body = ''

    # Filtering HEADERS
    # Split the headers into a list
    headers = headers.split('\n')

    # Split the first line of the headers into a list
    first_line = headers[0].split(' ')

    # Get the method, second part of the url and protocol
    method = first_line[0]
    url = first_line[1]
    protocol = first_line[2]

    # Remove the first line from the headers
    headers.pop(0)

    # From the headers, remove the 'Host' header and 
    # add its value as first (domain) part  of the url
    for header in headers:
        if 'Host' in header:
            url = 'http://' + header.split(': ')[1] + url
            headers.remove(header)
            break

    # Remove the first line from the headers
    headers.pop(0)

    # Create a dictionary of headers
    headers_dict = {}
    for header in headers:
        header = header.split(': ')
        try: headers_dict[header[0]] = header[1]
        except IndexError: pass

    # Filtering BODY
    # if body is not in json format, convert it to json
    if not body.startswith('{'):
        body = body.replace('\n', '')
        body = body.replace('\r', '')
        body = body.replace(' ', '')
        body = body.replace('=', '":"')
        body = body.replace('&', '","')
        body = '{"' + body + '"}'
        body = body.replace('""', '"')


    # Save the python requests code in a variable
    python_requests = f"""
    import requests

    url = '{url}'
    headers = {headers_dict}
    data = {body}

    response = requests.request('{method}', url, headers=headers, data=data)
    """

    # Print the python requests code
    printit('[ BTO | BRRTP ] python code snippet', coledt=[7, 49, 37], line_up=True, center=' ', space_up=True)
    printit(python_requests, line_up=True, line_down=True, coledt=[1, 49, 37])

    try:
        if '.' in filename:
            filename = filename.split('.')[0]
        # Write the python requests code to a file (same name as the burp raw request file)
        with open(filename + '.py', 'w') as f:
            f.write(python_requests)
        printit(f"[BTO | BRRTP] CODE WRITTEN TO FILE: {filename + '.py'}", coledt=[1, 49, 37], line_down=True, space_down=True, center=' ')
    except:
        printit("[BTO | BRRTP] FAILED TO WRITE THE CODE TO FILE!", coledt=[7, 49, 31], line_down=True, center=' ', space_down=True)

    exit()

# -r, --responsor
def responsor(filename):
    # banner
    printit('[ BTO | R3SP0NS0R ]', coledt=[7, 49, 37], line_up=True, line_down=True, center=' ', space_up=True)
    
    # common status codes & their meanings (dict)
    csc = {
        100: 'Continue',
        101: 'Switching Protocols',
        102: 'Processing (WebDAV)',
        103: 'Early Hints',
        200: 'OK',
        201: 'Created',
        202: 'Accepted',
        203: 'Non-Authoritative Information',
        204: 'No Content',
        205: 'Reset Content',
        206: 'Partial Content (RFC 7233)',
        207: 'Multi-Status (WebDAV)',
        208: 'Already Reported (WebDAV)',
        226: 'IM Used (RFC 3229)',
        300: 'Multiple Choices',
        301: 'Moved Permanently',
        302: 'Found (Previously "Moved temporarily")',
        303: 'See Other (since HTTP/1.1)',
        304: 'Not Modified (RFC 7232)',
        305: 'Use Proxy (since HTTP/1.1)',
        306: 'Switch Proxy',
        307: 'Temporary Redirect (since HTTP/1.1)',
        308: 'Permanent Redirect (RFC 7538)',
        400: 'Bad Request',
        401: 'Unauthorized (RFC 7235)',
        402: 'Payment Required',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Allowed',
        406: 'Not Acceptable (RFC 7231)',
        407: 'Proxy Authentication Required (RFC 7235)',
        408: 'Request Timeout',
        409: 'Conflict',
        410: 'Gone',
        411: 'Length Required',
        412: 'Precondition Failed (RFC 7232)',
        413: 'Payload Too Large (RFC 7231)',
        414: 'URI Too Long (RFC 7231)',
        415: 'Unsupported Media Type (RFC 7231)',
        416: 'Range Not Satisfiable (RFC 7233)',
        417: 'Expectation Failed',
        418: 'I\'m a teapot (RFC 2324)',
        421: 'Misdirected Request (RFC 7540)',
        422: 'Unprocessable Entity (WebDAV) (RFC 4918)',
        423: 'Locked (WebDAV) (RFC 4918)',
        424: 'Failed Dependency (WebDAV) (RFC 4918)',
        426: 'Upgrade Required',
        428: 'Precondition Required (RFC 6585)',
        429: 'Too Many Requests (RFC 6585)',
        431: 'Request Header Fields Too Large (RFC 6585)',
        451: 'Unavailable For Legal Reasons (RFC 7725)',
        500: 'Internal Server Error',
        501: 'Not Implemented',
        502: 'Bad Gateway',
        503: 'Service Unavailable',
        504: 'Gateway Timeout',
        505: 'HTTP Version Not Supported',
        506: 'Variant Also Negotiates (RFC 2295)',
        507: 'Insufficient Storage (WebDAV) (RFC 4918)',
        508: 'Loop Detected (WebDAV) (RFC 5842)',
        510: 'Not Extended (RFC 2774)',
        511: 'Network Authentication Required (RFC 6585)'
    }

    # user agents (list)
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)',
        'Chrome/90.0.4430.212 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'AppleWebKit/537.36 (KHTML, like Gecko)',
        'Chrome/90.0.4430.212 Safari/537.36',
    ]

    try:
        with open(filename, 'r') as url_file:
            # url should we without `http://` or `https://`
            urls = url_file.read().split('\n')
            # remove blank lines
            urls = list(filter(None, urls))
            # if http:// or https:// is present, remove it
            urls = [url.replace('http://', '').replace('https://', '') for url in urls]

            # requesting each url and displays their response code
            for url in urls:
                try:
                    status_code = requests.get('https://'+url, headers={'User-Agent': user_agents[random.randint(0, len(user_agents)-1)]}, timeout=10).status_code
                except Exception as e:
                    print(e)
                    continue
                
                # display status code with meaning (color coded)
                cc = { # color codes
                    1: 97, # white
                    2: 92, # green
                    3: 93, # yellow
                    4: 93, # yellow
                    5: 91 # red
                }

                # printit(f'[url] {url} : ', coledt=[1, 49, 37])
                # printit(f'\t[{status_code}] {csc[status_code]}', coledt=[1, 49, cc[int(str(status_code)[0])]])
                printit(f'[{status_code}] {url} : {csc[status_code]}', coledt=[1, 49, cc[int(str(status_code)[0])]])

        # scan complete message
        # print ('\n \033[0m\33[7;90;97m [ Aye aye, happy hacking captain :) ] \033[0m\n')
        printit('[ URL SCAN COMPLETE ]', coledt=[7, 49, 37], line_down=True, center=' ', space_down=True, line_up=True)

    except FileNotFoundError:
        printit(f'[ BTO | R3SP0NS0R ] FILE NOT FOUND!', coledt=[7, 49, 31], line_down=True, center=' ', space_down=True, line_up=True)


# logpath
# creates directory tree
def create_directory_tree(root_path, log_file):
    with open(log_file, 'w') as log:
        log.write(f"[BTO | L0GP4TH] ROOT DIRECTORY: {root_path}\n") # write the root directory path (input by user)
        for root, dirs, files in os.walk(root_path):
            if root_path == '/':
                level = root.count(os.sep)
            else:
                level = root.replace(root_path, '').count(os.sep)
            indent = ' ' * 4 * (level)
            log.write('{}{}/\n'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                log.write('{}{}\n'.format(subindent, f))

# searches input query in logged file
def search_in_log(log_file, search_query):
    result = []
    with open(log_file, 'r') as log:
        lines = log.readlines()
        root_directory = lines[0].strip()
        for line in lines[1:]:
            if search_query.lower() in line.lower():
                line_index = lines.index(line)
                path = line
                result.append([path, line_index])
    return result

# prints searched file location from logged file
def print_indented_path(log_file, root_directory, results):
    with open(log_file, 'r') as log:
        lines = log.readlines()
        for result in results:
            try: indents = int(result[0].count(' ') / 4)
            except: continue
            path = result[0].strip()
            full_path = root_directory
            # going in reverse order to get the parent directories (parent has less indents than child)
            if indents == 1:
                full_path += path
            else:
                # search line with less indents from bottom to top compared to current line (indents - 1)
                sub_paths = ''
                while indents > 1:
                    indents -= 1
                    for line in reversed(lines[:result[1]]):
                        if line.count(' ') / 4 == indents:
                            sub_paths = line.strip() + sub_paths
                            break
                full_path += sub_paths + path
            ftype = '     [DIR ]' if path.endswith('/') else '     [FILE]'
            print(ftype, full_path)

# print created log file size
def get_file_size(file_path):
    try:
        size = os.path.getsize(file_path)
        return size
    except FileNotFoundError:
        print("[BTO | L0GP4TH] FILE NOT FOUND!")

# main function
def logpath(generate=False, query=None, filename="directory_tree.log"):
    printit('[ BTO | L0GP4TH ]', coledt=[7, 49, 37], line_up=True, line_down=True, center=' ')

    # create directory tree log
    if generate:
        # root_directory = input("[BTO | L0GP4TH] Enter 'root directory' path: ")
        root_directory = printit("[BTO | L0GP4TH] ENTER 'ROOT DIRECTORY' PATH (ENTER FOR DEFAULT '/'): ", input_mode=True, coledt=[1, 49, 37])
        if root_directory == '': # if user enters blank, set root directory to '/'
            root_directory = '/'
        if not os.path.exists(root_directory):
            printit("[err | L0GP4TH] SPECIFIED ROOT DIRECTORY DOES NOT EXIST!", coledt=[7, 49, 31])
            return
        start_time = time.time() # start timer
        root_directory = root_directory.rstrip('/') + '/'
        create_directory_tree(root_directory, filename)
        printit(f"[BTO | L0GP4TH] DIRECTORY TREE LOG GENERATED AT: ./{filename}", coledt=[1, 49, 37])
        printit(f"[BTO | L0GP4TH] GENERATED {convert_size(get_file_size(filename))} FILE IN {(time.time() - start_time):.2f} SECS", coledt=[1, 49, 37], line_down=True)
    
    # search in directory tree log
    if query:
        start_time = time.time() # start timer
        # reading log file
        try:
            with open(filename, 'r') as log:
                lines = log.readlines()
                root_directory = lines[0].split(":")[1].strip().rstrip('/') + '/'
                log.close()
        except: 
            printit(f"[err | L0GP4TH] NO LOG FILE FOUND WHILE SEARCHING '{query}'!", coledt=[7, 49, 31])

        search_result = search_in_log(filename, query)

        if search_result:
            printit(f"[BTO | L0GP4TH] SEARCH RESULTS FOR '{query}':", coledt=[1, 49, 37])
            print_indented_path(filename, root_directory, search_result)
            printit(f"[BTO | L0GP4TH] ABOUT {len(search_result)} RESULTS FOUND IN {(time.time() - start_time):.2f} SECS", coledt=[1, 49, 37], line_down=True)
        else:
            printit("[err | L0GP4TH] NO MATCHING RESULTS FOUND IN LOG FILE!", coledt=[7, 49, 31], line_down=True)


# --------------------------------------------------------------------------------------------------

# Main
def main():
    # parse the args
    args = parser()    

    # displaying help message if no args are passed
    if not any(vars(args).values()):
        help_msg('d')
        return

    # check for default args
    if args.d_bytes: 
        printit(' '+convert_size(int(args.d_bytes))+' ', coledt=[7, 49, 37], verbose_mode=True, line_down=True, line_up=True, center=' ')
        exit()
    elif args.d_sys: sysinfo()
    elif args.unikey: unique_key()
    elif args.version:
        banner()
        print('[ver]:', version, '\n[git]: https://github.com/Divinemonk/bto')
        # print('\n[README]:\n   -> add `-h` in fornt of any sub-command to get help (options) for that sub-command\n   -> cannot use default options with sub-commands, and multiple sub-commands at once\n   -> follow intructions to achieve intended results\n   -> if any bugs or suggestions, raise an issue on github')
        print('\n[ A Divinemonk creation! ]\n')
        exit()

    # checking if sub-commands are passed
    # - static
    if args.subparser_name == 'static':
        if args.table: memsizetable()
        elif args.http_status_codes: httpstatuscodes()
        else: help_msg('static')

    # - local
    if args.subparser_name == 'local':
        if args.s_l_filename: file_info(args.s_l_filename)
        elif args.s_l_img2txt: 
            try: ocr(args.s_l_img2txt)
            except pytesseract.pytesseract.TesseractNotFoundError: 
                print('[BTO | OCR] (err) solution > https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i')
        else: help_msg('local')

    # - network
    if args.subparser_name == 'network':
        if args.s_n_brrtp: brrtp(args.s_n_brrtp)
        elif args.s_n_responsor: responsor(args.s_n_responsor)
        else: help_msg('network')

    # - logpath
    if args.subparser_name == 'logpath':
        filename = args.s_lp_filename if args.s_lp_filename else 'directory_tree.log'
        if args.s_lp_generate: logpath(generate=True, filename=filename)
        elif args.s_lp_query: logpath(query=args.s_lp_query, filename=filename)
        else: help_msg('logpath')


    


if __name__ == '__main__':
    main()

# --------------------------------------------------------------------------------------------------



