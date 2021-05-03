from django.db import models
from django.urls import reverse

# Create your models here.
class DevBoardBsc(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    hit = models.DecimalField(max_digits=10, decimal_places=0)
    insert_dt = models.DateTimeField()
    update_dt = models.DateTimeField()

    class Meta:
        managed = False
        verbose_name='board'
        verbose_name_plural='boards'
        db_table = 'dev_board_bsc'
        ordering = ('-insert_dt',)
        
    def __str___(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse('board:board_detail', args=(self.id))
    
    def get_previous(self):
        return self.get_previous_by_update_dt()
    
    def get_next(self):
        return self.get_next_by_update_dt()
    
    