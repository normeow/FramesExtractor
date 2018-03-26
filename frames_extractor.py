import cv2
import argparse
import os
import time


def _exctract_frames(videofile, destination_dir, fps=1):
    start = 0
    step = 1000 / fps
    cap = cv2.VideoCapture(videofile)

    if not cap.isOpened():
        print("Can't open", videofile)

    frame_count = 0
    success = True
    while success:
        cap.set(cv2.CAP_PROP_POS_MSEC, start)
        success, image = cap.read()
        cv2.imwrite("{}frame_{}.jpg".format(destination_dir, frame_count), image)
        frame_count += 1
        start += step


def main():
    parser = argparse.ArgumentParser(description='Extract frames from video')
    parser.add_argument('source', type=str, help='filename')
    parser.add_argument('dest', type=str,
                        help='directory storage for extracted frames')
    parser.add_argument('--fps', '-f', type=float, default=1,
                        help='frames per second. Default=1. Float is allowed, i.e. 0.5, 0.1')

    args = parser.parse_args()
    src = args.source
    dest = args.dest
    fps = args.fps

    if not os.path.exists(dest):
        os.makedirs(dest)

    start = time.clock()
    _exctract_frames(src, dest, fps)
    end = time.clock()
    print('Processed in {} sec'.format(end - start))


if __name__ == '__main__':
    main()
