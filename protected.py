from clarifai.client import ClarifaiApi
import sys

clarifai_api = ClarifaiApi(model='nsfw-v1.0')
result = clarifai_api.tag_image_urls(str(sys.argv[1]))
result = result['results'][0]['result']['tag']['probs']

if result[0] > result[1]:
    print 'Safe for work!'
else:
    print 'Not safe for work.'
