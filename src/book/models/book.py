from django.db import models
from acc.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='book_covers/')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    published=models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
@receiver(post_save, sender=Book)
def send_book_info(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'book_info',
        {
            'type': 'book_info',
            'title': instance.title,
            'author': instance.author.username,
            'price': instance.price,
        }   
    )