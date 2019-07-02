from django import template

register = template.Library()#タグやフィルターを登録するための初期化処理

@register.simple_tag#デコレータ
def url_replace(request, field, value):
  #GETパラメーターを一部置き換える
  url_dict = request.GET.copy()
  url_dict[field] = str(value)
  return url_dict.urlencode()