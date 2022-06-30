from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    """Кастомный профиль пользователя"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()

    management_company = models.ForeignKey(
        "ManagingOrganization",
        on_delete=models.CASCADE,
        verbose_name="Управляющая организация",
        related_name="ManagingOrganization",
    )

    def __str__(self):
        return f"{self.user.username}, {self.management_company}"


class ManagingOrganization(models.Model):
    """Управляющие организации"""

    name = models.CharField(
        max_length=250, verbose_name="Название управляющей организации"
    )

    def __str__(self):
        return self.name

    # @property
    # def request(self):
    #     return json.dumps(Request.objects.filter(manage_org=self).values())

    class Meta:
        verbose_name = "Управляющая организация"
        verbose_name_plural = "Управляющие организации"
