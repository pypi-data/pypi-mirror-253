#
#  Copyright (c) 2018-2024 Renesas Inc.
#  Copyright (c) 2018-2024 EPAM Systems Inc.
#

import random
import string
from pathlib import Path

from rich.console import Console

CONTENT_ENCRYPTION_ALGORITHM = 'aes256_cbc'
DOWNLOADS_PATH = Path.home() / '.aos' / 'downloads'
AOS_DISKS_PATH = DOWNLOADS_PATH
IMAGE_WITHOUT_NODES_FILENAME = 'aos-image-vm-genericx86-64_3.0.1.wic.vmdk'
NODE0_IMAGE_FILENAME = 'aos-vm-node0-genericx86-64.wic.vmdk'
NODE1_IMAGE_FILENAME = 'aos-vm-node1-genericx86-64.wic.vmdk'

DISK_IMAGE_DOWNLOAD_URL = (
    'https://d3bbh8dbll67u6.cloudfront.net/vm/aos-vm-v4.2.1.tar.gz?Expires=1861957961&'
    'Signature=Ll1gEpmx-6IJQQNIiuwffKbjx-myKsqwBZHH7Gin9W6HY-ooYvJYzmj31mZdoA-nKYW8r2D'
    'O0HbXYC0Lr0NlStS4XPRWEiWHIFGs-VY-tBbjpSjkbs663DoV175bhNQyQSX~nXeEaQugfsUkXI9w-RaA'
    '4bHnV7cRmZDydrqb2md6b1UoQQp5X9gF4PgEaPE~V0Tr8ES-qfFHtlikHlUqBdcYODKaBJa4pgetbOunX'
    'qYNR3sF-ynZFFGYqW5Q7621dSX~NnvdiQZJIQQHNaGaNZW-~rXfDwWjqOB9s-XfFqGCS-N3Jir7Ru-Yfu'
    'VpUgNQk8mWY0Jw1S6HKI4uNHhlqw__&Key-Pair-Id=K15STESC8GKWQK')  # noqa: WPS319
REQUEST_TIMEOUT = 30
RECONNECT_TIMEOUT = 40

console = Console()
error_console = Console(stderr=True, style='red')
ALLOW_PRINT = True


def print_message(formatted_text, end='\n', ljust: int = 0):
    if ALLOW_PRINT:
        if ljust > 0:
            formatted_text = formatted_text.ljust(ljust)
        console.print(formatted_text, end=end)


def print_left(formatted_text, ljust=60):
    print_message(formatted_text, end='', ljust=ljust)


def print_done():
    print_message('[green]DONE')


def print_success(message):
    print_message(f'[green]{str(message)}')  # noqa: WPS237


def print_error(message):
    if ALLOW_PRINT:
        error_console.print(message)


def generate_random_password() -> str:
    """
    Generate random password from letters and digits.

    Returns:
        str: Random string password
    """
    dictionary = string.ascii_letters + string.digits
    password_length = random.randint(10, 15)  # noqa: S311,WPS432
    return ''.join(random.choice(dictionary) for _ in range(password_length))  # noqa: S311
