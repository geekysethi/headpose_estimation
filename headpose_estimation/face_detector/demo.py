from retinaface import RetinaFace


if __name__=="__main__":

    resp = RetinaFace.detect_faces("/Users/ashish/Desktop/projects/retinaface/tests/dataset/img1.jpg")

    print(resp)