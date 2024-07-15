from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLine, DecorationLine, WrappingPaper, Order


@receiver(post_save, sender=WrappingPaper)
def update_wrapping_paper_remaining(sender, instance, **kwargs):
    if instance.use_wrapping_paper and instance.wrapping_paper is not None and instance.paper_qty:
        instance.wrapping_paper.update_remaining(instance.paper_qty)


@receiver(post_save, sender=OrderLine)
@receiver(post_delete, sender=OrderLine)
def update_silk_and_material_remaining(sender, instance, **kwargs):
    silk_qty_used = round(1.60 * instance.qty, 2)
    instance.product.color.update_remaining(silk_qty_used)
    if instance.product.materials_id:
        instance.product.materials_id.update_remaining(instance.qty)


@receiver(post_save, sender=DecorationLine)
@receiver(post_delete, sender=DecorationLine)
def update_decoration_remaining(sender, instance, **kwargs):
    instance.decorations.update_remaining(instance.dec_qty)


@receiver(post_save, sender=Order)
def create_order_lines(sender, instance, created, **kwargs):
    if created:
        from .models import WrappingPaper
