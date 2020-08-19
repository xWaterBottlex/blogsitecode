# from django.db import models
# from django.contrib.auth import get_user_model
#
# # get the user model
# User = get_user_model()
#
# from django.template.defaultfilters import slugify
# from django.urls import reverse
# from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
# from django.core.validators import MinLengthValidator, validate_image_file_extension
# from taggit.managers import TaggableManager
# from django.core.exceptions import ValidationError
#
#
# # custom validation
#
# def validate_file_size(value):
#     filesize = value.size
#
#     if filesize > 5242880:
#         raise ValidationError("Max file size is 5MB")
#     else:
#         return value
#
#
# # Create your models here.
#
# def get_anonymous():
#     return User.objects.get(first_name='Anonymous')
#
#
# class Post(models.Model):
#     user = models.ForeignKey(User, related_name='postx', null=True, on_delete=models.SET(get_anonymous))
#     title = models.TextField(max_length=128, unique=True)
#     content = RichTextUploadingField(
#         validators=[MinLengthValidator(500, message='minumum of 500 characters are necessary')])
#     snippet = models.TextField(max_length=256)
#     thumbnail_image = models.ImageField(upload_to='blog/',
#                                         validators=[validate_image_file_extension, validate_file_size])
#     slug = models.SlugField(default='')
#     tags = TaggableManager()
#     created_at = models.DateTimeField(auto_now_add=True)
#     edited_at = models.DateTimeField(auto_now=True)
#     status = models.BooleanField(default=False)
#
#     # ad = models.ForeignKey('Advertisement',on_delete=models.SET_NULL,related_name='post',null= True)
#
#     def publish(self):
#         self.status = True
#         self.save()
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.title)
#         return super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return reverse("blog:blog-detail", kwargs={"slug": self.slug})
#
#     class Meta:
#         ordering = ['-created_at']
