Protected Uploader
====================

This is a simple checker that confirms that photos being uploaded have no
pornographic content.

To run:

 - Create a free account on [Clarifai's developer site](http://developer.clarifai.com)
 - Create a new application
 - Run this in the terminal:

```bash
pip install git+git://github.com/Clarifai/clarifai-python.git
export CLARIFAI_APP_ID=<application_id_from_your_account>
export CLARIFAI_APP_SECRET=<application_secret_from_your_account>
```

**Note:** If you don't want to `export` these variables, you can add the
application ID and secret in the arguments of the new Clarifai object.

Once you've got this, you're all set up!  Run the following in your terminal to
see if the given image is Safe for Work.

```bash
python protected.py <your_image_url>
```

Here's an example of what my terminal looks like from start to finish after I've
downloaded the project and opened the terminal in the project folder:

```bash
$ pip install git+git://github.com/Clarifai/clarifai-python.git
$ export CLARIFAI_APP_ID=abc123xyz
$ export CLARIFAI_APP_SECRET=abc123xyz
$ python protected.py http://i.imgur.com/YCqQW0W.jpg
Safe for work!
```
