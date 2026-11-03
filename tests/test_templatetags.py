from django.template import Context, Template


def render(source):
    return Template("{% load wagtailcharts_tags %}" + source).render(Context())


def test_render_charts_includes_frontend_scripts():
    html = render("{% render_charts %}")

    for script in ("chart.umd.min.js", "chartjs-plugin-datalabels.min.js", "wagtailcharts.js"):
        assert f"/static/wagtailcharts/js/{script}" in html


def test_generate_uuid4_is_unique():
    first, second = render("{% generate_uuid4 %}"), render("{% generate_uuid4 %}")

    assert len(first) == 36
    assert first != second


def test_addspace():
    assert render('{{ "Left_Axis"|addspace }}') == "Left Axis"
