from django.db import models
from vendor.models import Vendor
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File

class blogs(models.Model):
    vendor=models.ForeignKey(Vendor, related_name='blogs' , on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    description=models.TextField(blank=True, null=True)
    date_added=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail=models.ImageField(upload_to='uploads/,', blank=True, null=True)
    
    class Meta:
        ordering=['-date_added']
        
    def __str__(self):
        return self.title
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail=self.make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240*180.jpg'
    
    def make_thumbnail(self, image, size=(300,200)):
        img=Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        
        thumb_io=BytesIO()
        img.save(thumb_io,'JPEG', quality=85)
        thumbnail=File(thumb_io, name=image.name)
        
        return thumbnail

class BlogImage(models.Model):
    blogs=models.ForeignKey(blogs, related_name='images', on_delete=models.CASCADE)   
    image=models.ImageField(upload_to='uploads/', blank=True , null=True)
    thumbnail=models.ImageField(upload_to='uploads/,', blank=True, null=True)
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail=self.make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240*180.jpg'
    
    def make_thumbnail(self, image, size=(300,200)):
        img=Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        
        thumb_io=BytesIO()
        img.save(thumb_io,'JPEG', quality=85)
        thumbnail=File(thumb_io, name=image.name)
        
        return thumbnail
    
