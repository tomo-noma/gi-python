from urllib import error, request
import argparse

url = "https://www.gitignore.io/api/"
# HTTP headers
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/\
        537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}


def main():
    # argument parser
    parser = argparse.ArgumentParser(
        'gi-python',
        description='Command line tool for gitignore.io from python'
        )
    parser.add_argument(
        'name',
        nargs='+',
        help='ignore environment name.',
        metavar='Envname'
        )
    args = parser.parse_args()
    req = request.Request(
        '{}/{}'.format(url, ','.join(args.name)),
        headers=header
        )
    # Request for gitignore
    get_gitignore(req)


def get_gitignore(req):
    try:
        with request.urlopen(req) as res:
            body = res.read()
            print(body.decode('utf-8'))
            return body
    except error.HTTPError as err:
        if(err.code == 404):
            print('can not find gitignore.')
        else:
            print(err.code)
    except error.URLError as err:
        print(err.code)


if __name__ == "__main__":
    main()
