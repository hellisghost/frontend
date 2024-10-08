from django.db import models

class Rol(models.Model):
    name_rol = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    state_rol = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    #Para que a futuro nos salgan datos de los roles que queramos. en este caso: el name_rol
    #Es decir, lo que quiero que me salga en un deplegable lo pongo luego de self
    def __str__(self):
        return self.name_rol