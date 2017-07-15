ap = argparse.ArgumentParser()
ap.add_argument( "-f" , "--filename" )
args = vars (ap.parse_args())

filename = "../../data/images/capsicum.jpg"
if args[ 'filename' ]:
filename = args[ 'filename' ]

img = cv2.imread(filename) 
