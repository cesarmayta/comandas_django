from django.db import models


class Almacen(models.Model):
    alm_cod = models.CharField(primary_key=True, max_length=3)
    alm_desc = models.CharField(max_length=40, blank=True, null=True)
    alm_prioridad = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'almacen'
        
    def __str__(self):
        return self.alm_desc


class Envase(models.Model):
    env_cod = models.CharField(primary_key=True, max_length=255)
    env_desc = models.CharField(max_length=255, blank=True, null=True)
    env_desc_corta = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'envase'
        
    def __str__(self):
        return self.env_desc


class Marca(models.Model):
    mar_cod = models.CharField(primary_key=True, max_length=255)
    mar_desc = models.CharField(max_length=255, blank=True, null=True)
    mar_desc_corta = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marca'
        
    def __str__(self):
        return self.mar_desc


class Seccion(models.Model):
    sec_cod = models.CharField(primary_key=True, max_length=255)
    sec_desc = models.CharField(max_length=255, blank=True, null=True)
    sec_desc_corta = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seccion'
        
    def __str__(self):
        return self.sec_desc

class Producto(models.Model):
    prod_cod = models.CharField(primary_key=True, max_length=255)
    env_cod =  models.ForeignKey(Envase,to_field='env_cod',
                                 db_column='env_cod',
                                 verbose_name='Envase',on_delete=models.RESTRICT)
    prod_desc = models.CharField(max_length=255, blank=True, null=True)
    prod_desc_corta = models.CharField(max_length=255, blank=True, null=True)
    prod_peso = models.BigIntegerField(blank=True, null=True)
    prod_volumen = models.BigIntegerField(blank=True, null=True)
    mar_cod = models.ForeignKey(Marca,db_column='mar_cod',on_delete=models.RESTRICT)
    sec_cod =  models.ForeignKey(Seccion,db_column='sec_cod',on_delete=models.RESTRICT)
    prod_generastock = models.CharField(max_length=255, blank=True, null=True)
    prod_utilidad = models.BigIntegerField(blank=True, null=True)
    prod_especificacion = models.CharField(max_length=255, blank=True, null=True)
    prod_stockminimo = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'
        
    def __str__(self):
        return self.prod_desc


