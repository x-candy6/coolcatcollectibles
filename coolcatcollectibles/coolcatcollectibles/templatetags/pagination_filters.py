from django import template

register = template.Library()


@register.filter
def dynamic_page_range(current_page, total_pages, max_pages=6):
    half_range = max_pages // 2
    start_page = max(1, current_page - half_range)
    end_page = min(total_pages, current_page + half_range)

    if end_page - start_page < max_pages - 1:
        if start_page == 1:
            end_page = min(end_page + max_pages - 1, total_pages)
        else:
            start_page = max(end_page - max_pages + 1, 1)

    return range(start_page, end_page + 1)


@register.filter
def is_equal(value, arg):
    return value == arg
