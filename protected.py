from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi(model='nsfw-v0.1')
result = clarifai_api.tag_image_urls('https://www.petfinder.com/wp-content/uploads/2012/11/140272627-grooming-needs-senior-cat-632x475.jpg')
result = result['results'][0]['result']['tag']['probs']

if result[0] > result[1]:
    print 'Safe for work!'
else:
    print 'Not safe for work.'
