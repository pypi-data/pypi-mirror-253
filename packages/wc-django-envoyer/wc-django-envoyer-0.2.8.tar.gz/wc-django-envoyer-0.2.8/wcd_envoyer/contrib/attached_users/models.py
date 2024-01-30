from django.db import models
from django.utils.translation import pgettext_lazy
from django.conf import settings

from wcd_envoyer.models import Message


__all__ = 'MessageAttachedUser',


class MessageAttachedUser(models.Model):
    class Meta:
        verbose_name = pgettext_lazy('wcd_envoyer', 'Message schedule')
        verbose_name_plural = pgettext_lazy('wcd_envoyer', 'Message schedules')

    message = models.ForeignKey(
        Message, on_delete=models.CASCADE,
        verbose_name=pgettext_lazy('wcd_envoyer', 'Message'),
        related_name='attached_users',
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        verbose_name=pgettext_lazy('wcd_envoyer', 'Send at'),
        null=False, blank=False, related_name='envoyer_messages',
    )

    def __str__(self) -> str:
        return pgettext_lazy('wcd_envoyer', '#{id}: user #{user_id}').format(
            id=self.message_id, user_id=self.user_id,
        )
