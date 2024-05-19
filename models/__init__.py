"""This file makes it easier to import the 'BaseModel' directly
when importing the 'models' package.

Created a 'FileStorage' instance and reload it by calling
the reload method on the staorage instance.
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
