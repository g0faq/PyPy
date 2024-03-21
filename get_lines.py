import argparse


def count_lines(file):
    try:
        with open(file) as f:
            count = len(f.readlines())
            return count
    except Exception:
        return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, default='')
    args = parser.parse_args()
    print(count_lines(args.file))
