import cv2

videoCapture = cv2.VideoCapture('video.avi')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter('MyOutputVideo.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)
'''There are different codecs for different video formats:
 - 'I', '4', '2', '0': this option is an uncompressed YUV encoding, 4:2:0 chroma subsamples. This encoding is widely compatible but produces large files. The file extension should be .avi
 - 'X', 'V', 'I', 'D': this option is a relative  old MPEG-4 encoding. It is a good option if you want to limit the size of the resulting video. The file extension should be .avi
 - 'P', 'I', 'M', '1': this option is a MPEG-1 encoding. The file extension should be .avi
 - 'M', 'P', '4', '2': this option is another relatively old MPEG-4 encoding. It is a good option if you want to limit the size of the resulting video. The file extension should be .mp4
 - 'X', '2', '6', '4': this option is a newer MPEG-4 encoding. It is a good option if you want to limit the size of the resulting video. The file extension should be .mp4
 - 'T', 'H', 'E', 'O': this option is Ogg Vorbis. The file extension should be .ogv
 - 'F', 'L', 'V', '1': this option is a Flash video encoding. The file extension should be .flv 
 '''

success, frame = videoCapture.read()
while success:
    videoWriter.write(frame)
    success, frame = videoCapture.read()