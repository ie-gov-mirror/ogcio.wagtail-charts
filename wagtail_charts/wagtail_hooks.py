from wagtail import hooks


@hooks.register("register_icons")  # type: ignore
def register_admin_icon(icons):
    return icons + ["wagtailcharts/icons/chart-line-solid-full.svg"]
