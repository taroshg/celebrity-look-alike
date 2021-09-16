# Celebrity Look Alike
This algorithm uses the VGG model to create an encoding of any given face then compares other face encodings with a simple distance formula to derive the similarity between two encodings. Then the algorithm filters through the database of encodings to find the image with the lowest distance or the highest similarity.

## Credits
The data was acquired by scraping <https://www.forbes.com/celebrities/> 

The VGG model and weights was acquired from [here](https://gist.github.com/EncodeTS/6bbe8cb8bebad7a672f0d872561782d9) 

### Note
Due to size constraints, the vgg weights (.h5) is not in this repo, therefore the weights must be downloaded and stored into a folder with the name ("vggFace") and naming the weights file ("vgg_face_weights.h5")