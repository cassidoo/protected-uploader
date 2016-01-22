from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi(model='nsfw-v0.0')
result = clarifai_api.tag_image_urls('http://www.clarifai.com/img/metro-north.jpg')
result = result['results'][0]['result']['tag']['probs']

if result[0] > result[1]:
    print 'Safe for work!'
else:
    print 'Not safe for work.'
