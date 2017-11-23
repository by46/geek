import ffmpy

if __name__ == '__main__':
    ff = ffmpy.FFmpeg(
        inputs={'1.mp4': None},
        outputs={'12.mp4': "-acodec aac"}
    )
    ff.run()
