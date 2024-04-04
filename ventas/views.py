from django.shortcuts import render
from ventas.models import VentasApple
from ventas.models import VentasProductos
import plotly.express as px
import pandas as pd

def gestionar(request):
    sells = VentasApple.objects.all()
    sellss = VentasProductos.objects.all()

    df = pd.DataFrame(list(sells.values()))
    dff = pd.DataFrame(list(sellss.values()))
    dfff = pd.DataFrame(list(sells.values("month", "value")))
    dffff = pd.DataFrame(list(sells.values("value")))

    grafico = px.bar(df, x="month", y="value", color="ubication", title="Month Sales by Region")
    torta = px.pie(dff, values='amount', names='product_type', title="Monthly Product Sales")
    financial = px.line(dfff, x='month', y='value', title="Profit Lines Per Month")
    histogram = px.histogram(dffff, x="value", title="Total Sales")

    myhtml = grafico.to_html(full_html=False)
    grafico_t = torta.to_html(full_html=False)
    grafico_f = financial.to_html(full_html=False)
    grafico_h = histogram.to_html(full_html=False)

    context = {
        "ventas": sells,
        "graf": myhtml,
        "Circular": grafico_t,
        "Financias": grafico_f,
        "Histograma": grafico_h,
    }

    return render(request, "ventas/index.html", context)

# Create your views here.
