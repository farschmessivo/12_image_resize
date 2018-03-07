from PIL import Image
import argparse
from fractions import Fraction
import os


def create_parser():
    parser = argparse.ArgumentParser(
        description='Module re-sizes an image'
    )
    parser.add_argument(
                        'pic',
                        type=str,
                        help='location of the original pic'
                        )
    parser.add_argument(
                        '-w',
                        '--width',
                        type=int,
                        help='width of the output pic'
                        )
    parser.add_argument(
                        '-he',
                        '--height',
                        type=int,
                        help='height of the output pic'
                        )
    parser.add_argument(
                        '-s',
                        '--scale', type=float,
                        help='how to scale the output pic'
                        )
    parser.add_argument(
                        '-o',
                        '--output',
                        type=str,
                        help='where to save the output pic'
                        )
    return parser


def get_new_size(
                original_image,
                requested_width,
                requested_height
                ):
    original_width, original_height = original_image.size

    if requested_width and requested_height:
        new_size = (requested_width, requested_height)
    elif requested_width:
        height = int(requested_width * original_height / original_width)
        new_size = (requested_width, height)
    elif requested_height:
        width = int(requested_height * original_width / original_height)
        new_size = (width, requested_height)
    return new_size


def get_new_scale_size(original_size, scale):
    return [round(scale * size) for size in original_size]


def choose_path_to_result(path_to_result, path_to_original, resized_image):
    if os.path.isdir(path_to_result):
        name_file, file_extension = os.path.splitext(path_to_original)
        return path_to_result + name_file + file_extension
    elif path_to_result:
        return path_to_result
    else:
        name_file, file_extension = os.path.splitext(path_to_original)
        created_path = '{}_{}x{}{}'.format(
            name_file,
            *resized_image.size,
            file_extension)
        return created_path


def save_image(resized_image, path_to_result):
    resized_image.save(path_to_result)


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    original_image = Image.open(args.pic)
    original_size = original_image.size
    original_width, original_height = original_image.size
    output_image = args.output
    if args.output.endswith('/') and not os.path.exists(args.output):
        raise parser.error('Folder doesnt exist')

    if args.scale and (args.width or args.height):
        raise parser.error('You must use scale without width or height!')
    elif not any:
        raise parser.error('Width or height or scale required!')
    elif args.scale:
        new_size = get_new_scale_size(original_size, args.scale)
    else:
        if Fraction(original_width, original_height) != Fraction(
                args.width, args.height):
            print('***The proportions do not match the original image.***')
        new_size = get_new_size(
                                args.pic,
                                args.width,
                                args.height
                                )

    resized_image = original_image.resize(new_size, Image.ANTIALIAS)

    chosen_path_to_result = choose_path_to_result(
        output_image, args.pic, resized_image)
    save_image(resized_image, chosen_path_to_result)
    print('The image is created: {}'.format(chosen_path_to_result))
