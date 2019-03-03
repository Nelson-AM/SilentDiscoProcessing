import cv2


def process_video(vidin):
    """
    """

    cap = read_video(vidin)
    # cv2.VideoCapture("./out.mp4")

    while not cap.isOpened():
        cap = read_video(vidin)
        # cap = cv2.VideoCapture("./out.mp4")

        cv2.waitKey(1000)
        print("Wait for the header")

        pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)

        while True:
            flag, frame = cap.read()

            if flag:

                # The frame is ready and already captured
                show_image(frame)
                # cv2.imshow('video', frame)
                pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
                print(str(pos_frame) + " frames")

            else:

                # The next frame is not ready, so we try to read it again.
                cap.set(cv2.CAP_PROP_POS_FRAMES, pos_frame - 1)
                print("Frame is not ready")

                # It is better to wait a while for the next frame to be
                # ready.
                cv2.waitKey(1000)

                if cv2.waitKey(10) == 27:
                    break

                if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
                    # If the number of captured frames is equal to the total number of frames, we stop.
                    print("Stopping")
                        break
