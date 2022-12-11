# create a python script that accepts a flickr album identifier and then enumerates all photo ids of the pictures in that album which have an empty description.

import os
import argparse
import flickrapi
import subprocess

def get_home_directory():
    return os.path.expanduser('~')

def get_api_key_file():
    return os.path.join(get_home_directory(), '.flickr_api_key')

def store_api_key(api_key, api_secret):
    with open(get_api_key_file(), 'w') as f:
        f.write(api_key + '\n')
        f.write(api_secret + '\n')

def read_api_key():
    if os.path.exists(get_api_key_file()):
        with open(get_api_key_file()) as f:
            api_key = f.readline().strip()
            api_secret = f.readline().strip()
            return (api_key, api_secret)
    else:
        return (None, None)

def create_parser():
    parser = argparse.ArgumentParser(
        description='Enumerates all photo ids of the pictures in a flickr album which have an empty description.')
    parser.add_argument('album_id', help='The ID of the album on Flickr.', nargs='?')
    parser.add_argument('--api-key', help='The Flickr API key.')
    parser.add_argument('--api-secret', help='The Flickr API secret.')
    parser.add_argument('--store', help='Store the API key and secret in the home directory.', action='store_true')
    parser.add_argument('--read', help='Read the API key and secret from the home directory.', action='store_true')
    parser.add_argument('--tag', help='Call the ImageTagger script on each photo.', action='store_true')
    return parser

def get_flickr_album_info(api_key, api_secret, album_id):
    flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
    photos = flickr.photosets.getPhotos(photoset_id=album_id)
    photo_ids = []
    for photo in photos['photoset']['photo']:
        info = flickr.photos.getInfo(photo_id=photo['id'])
        description = info['photo']['description']['_content']
        if description == '':
            photo_ids.append(photo['id'])
    return photo_ids

def main(album_id, api_key, api_secret, tag):
    photo_ids = get_flickr_album_info(api_key, api_secret, album_id)
    print(photo_ids)
    if tag:
        for photo_id in photo_ids:
            subprocess.call(['imagetagger', photo_id])

if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    api_key = args.api_key
    api_secret = args.api_secret
    if args.store:
        store_api_key(api_key, api_secret)
        exit(0)

    if not api_key:
        api_key, api_secret = read_api_key()
        if not api_key or not api_secret:
            api_secret = input('Enter your Flickr API secret: ')
            if args.store:
                store_api_key(api_key, api_secret)
    if not api_secret:
        api_secret = input('Enter your Flickr API secret: ')

    main(args.album_id, api_key, api_secret, args.tag)
