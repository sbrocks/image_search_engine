# import the necessary packages
from pyimagesearch.colordescriptor import ColorDescriptor
from pyimagesearch.searcher import Searcher
import argparse
import cv2
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())
 
# initialize the image descriptor
cd = ColorDescriptor((8, 12, 3))

# load the query image and describe it
query = cv2.imread(args["query"])
#print(query)
features = cd.describe(query)
 
# perform the search
searcher = Searcher(args["index"])
results = searcher.search(features)
 
# display the query
resi = cv2.resize(query,(720,540))
cv2.imshow("Query", resi)
cv2.waitKey(0)
print(results) 
# loop over the results
for (score, resultID) in results:
	# load the result image and display it
	#print(resultID)
	result = cv2.imread(resultID)
	#print(result)
	resi = cv2.resize(result,(720,540))
	#cv2.imwrite("imag1.jpg",result)
	cv2.imshow("Result", resi)
	cv2.waitKey(0)
