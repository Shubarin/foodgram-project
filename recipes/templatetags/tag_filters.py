from django import template

register = template.Library()


@register.filter
def tags_list(get):
    return get.getlist('tags')


@register.filter
def set_tag_qs(request, tag):
    new_request = request.GET.copy()
    tags = request.GET.getlist('tags')
    if tag.name in tags:
        tags.remove(tag.name)
    else:
        tags.append(tag.name)
    new_request.setlist('tags', tags)
    return new_request.urlencode()


@register.filter
def tags_to_url_params(tags):
    url_param_tags = [f'tags={tag}' for tag in tags]
    return '&' + '&'.join(url_param_tags)
