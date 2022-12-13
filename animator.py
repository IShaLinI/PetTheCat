import constants


def getKeyframeDelta(frame1, frame2):
    keyframeDelta = []
    for obj in range(len(frame1)):
        keyframeDelta.append(tuple(map(lambda i, j: i - j, frame1[obj], frame2[obj])))
    return keyframeDelta


class Animator:

    # time is in seconds
    def __init__(self, objects, keyframes, time):
        self.objects = objects
        self.keyframes = keyframes
        self.time = time

        self.totalSteps = constants.FRAME_RATE / self.time
        self.stepsPerKeyFrame = int(self.totalSteps / len(keyframes))

        self.keyFrame = self.keyframes[0]
        self.nextKeyFrame = self.keyframes[1]

    def update(self):

        frameDelta = getKeyframeDelta(self.keyFrame, self.nextKeyFrame)
        frameStep = frameDelta;
        for i in range(len(frameStep)):


        print(frameDelta)
        print(frameStep)

