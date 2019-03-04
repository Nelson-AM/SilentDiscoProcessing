import unittest

from silentdisco.main import parse_args


class ParserTest(unittest.TestCase):
    def test_running_without_arguments(self):
        empty_args = []
        self.assertEquals("usage: main.py [-h] -v VIDEO", parse_args(empty_args))

    def test_video_argument_gets_parsed(self):
        args = ["-v", "videofile"]
        parser = parse_args(args)
        self.assertTrue(str(parser.video))


if __name__ == '__main__':
    unittest.main()
