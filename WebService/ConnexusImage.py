from google.appengine.ext import ndb

import logging

class Image(ndb.Model):

	imageId = ndb.IntegerProperty()
	streamId = ndb.IntegerProperty()
	blobKey = ndb.BlobKeyProperty()
	creationDate = ndb.DateProperty(auto_now_add=True)
	comment = ndb.StringProperty()
	loc = ndb.GeoPtProperty(default=(30.267153, -97.743061))

	@staticmethod
	def addImage(streamId, imageId, blobKey, loc):
		image = Image()
		image.streamId = streamId
		image.imageId = imageId
		image.blobKey = blobKey
		image.loc.lat = loc[0]
		image.loc.lon = loc[1]
		image.put()