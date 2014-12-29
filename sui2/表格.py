from django.forms.models import ModelForm
from sui2.models import 使用者表格

# Users type data in modelform of views 
class 加使用者表格(ModelForm):
    class Meta:
        model = 使用者表格
        fields = ['username', 'password']
#         labels = {
#             '新帳號':'新帳號', 
#             '新密碼':'新密碼'
#         }
#         error_messages = {}