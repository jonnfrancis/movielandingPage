from django import template

register = template.Library()

@register.filter
def runtime_in_hours_and_minutes(runtime):
    hours, minutes = divmod(runtime, 60)
    if hours > 0:
        return f"{hours}h {minutes}min"
    else:
        return f"{minutes}min"
