Protected Uploader
====================

This is a simple checker that confirms that photos being uploaded have no
pornographic content.

To run:

 - Create a free account on [Clarifai's developer site](developer.clarifai.com)
 - Create a new application
 - Run this in the terminal:

```
pip install git+git://github.com/Clarifai/clarifai-python.git
export CLARIFAI_APP_ID=<application_id_from_your_account>
export CLARIFAI_APP_SECRET=<application_secret_from_your_account>
```

**Note:** If you don't want to `export` these variables, you can add the
application ID and secret in the arguments of the new Clarifai object.
