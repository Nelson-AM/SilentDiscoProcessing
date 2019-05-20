import argparse
import sys

import cv2


def parse_args(args):
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("-v",
                                 "--video",
                                 required=True,
                                 help="Path to video file")

    return vars(argument_parser.parse_args(args))


def get_frame_rate(video):
    return video.get(cv2.CAP_PROP_FPS)


def get_frame_time_in_ms(video):
    return int(1000 / get_frame_rate(video))


if __name__ == "__main__":
    print("Start of main program.")

    parser = parse_args(sys.argv[1:])
    video_capture = cv2.VideoCapture(parser["video"])
    frame_time_ms = get_frame_time_in_ms(video_capture)

    while video_capture.isOpened():
        ret, frame = video_capture.read()
        resized_frame = cv2.resize(frame, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

        cv2.imshow("frame", resized_frame)
        if cv2.waitKey(frame_time_ms) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
