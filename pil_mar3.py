from PIL import Image
import os
import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        description='Module re-sizes an image'
    )
    parser.add_argument('path', type=str,
                        help='location of the original pic')
    parser.add_argument('-w', '--width', type=int,
                        help='width of the output pic')
    parser.add_argument('-he', '--height', type=int,
                        help='height of the output pic')
    parser.add_argument('-s', '--scale', type=int,
                        help='how to scale the output pic')
    parser.add_argument('-o', '--output', type=str, default='.',
                        help='where to save the output pic')
    return parser


def resize_image(original_image, new_file_path):
    im = Image.open(original_image)
    original_width = im.width  # old_size[0] is in (width, height) format
    print(original_width)
    ratio = float(desired_width) / max(original_width)
    new_size = tuple([int(x * ratio) for x in old_size])
    im = im.resize(new_size, Image.ANTIALIAS)
    new_im = Image.new('RGB', (desired_width, desired_height))
    new_im.paste(im, ((desired_size - new_size[0]) // 2,
                      (desired_size - new_size[1]) // 2))
    new_im.show()
    new_im.save(new_file_path, 'kartinka' + '_' + '.png', 'PNG')


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    original_image = args.path
    desired_width = args.width
    desired_height = args.height
    desired_scale = args.scale
    new_file_path = args.output
    resize_image(original_image, new_file_path)




# answer = args.square**2
# if args.verbosity == 2:
#     print("the square of {} equals {}".format(args.square, answer))
# elif args.verbosity == 1:
#     print("{}^2 == {}".format(args.square, answer))
# else:
#     print(answer)