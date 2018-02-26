from django.db import models


class UserData(models.Model):
    username = models.CharField(max_length=24)
    email = models.EmailField(max_length=32, blank=True, null=True)
    password = models.CharField(max_length=32)
    created_data = models.DateTimeField()
    email_is_confirm = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return "Login: {}, Email: {}, Data: {}.".format(self.login, self.email, self.created_data)

    class Meta:
        verbose_name = "Данные пользователя"
        verbose_name_plural = "Данные пользователей"


class UserProfile(models.Model):
    user_data = models.OneToOneField(UserData, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)

    def __str__(self):
        return "Login: {}, Email: {}.".format(self.user_data.login, self.user_data.email)

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"
