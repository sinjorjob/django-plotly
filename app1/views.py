from django.shortcuts import render
from django.views.generic import TemplateView
from django_pandas.io import read_frame
from app1.models import OrderItem
import plotly.express as px


class Dashboard(TemplateView):

    def get(self, request, *args, **kwargs):

        #製品毎の売上円グラフを生成
        plot_fig_pie = draw_pie()
        #日付別＆製品毎の売上棒グラフを生成
        plot_fig_bar = draw_bar()

        return render(request, 'dashboard.html',
                         {"plot_fig_pie":plot_fig_pie,
                         "plot_fig_bar": plot_fig_bar,
                         })


def draw_pie():
    
    order_items = OrderItem.objects.all()
    df_orders = read_frame(order_items, fieldnames=['created_date', 'product__name', 'product__price'])
    df_orders.rename(columns={'created_date': '注文日', 'product__name':'製品名', 'product__price':'金額'}, inplace=True)
    #### 円グラフの生成
    fig_pie = px.pie(df_orders, names='製品名', values="金額")
    fig_pie.update_layout(
    width=500,  # figureの幅
    height=350,  # figureの高さ
    title={
        "text": "製品毎の売上金額割合",
        # グラフタイトルのスタイル
        "font": {"family": "Courier", "size": 20, "color": "slategray"},
        },
        margin={"l": 20, "r": 20, "t": 40, "b": 20},  # 余白
        paper_bgcolor="lightyellow",  # グラフ領域の背景色
        )
    plot_fig_pie = fig_pie.to_html(fig_pie, include_plotlyjs=True)
    return plot_fig_pie


def draw_bar():
    #日別の売上推移棒グラフ
    order_items = OrderItem.objects.all()
    df_order_items = read_frame(order_items, fieldnames=['created_date', 'product', 'product__price'])
    df_order_items.rename(columns={'created_date': '注文日', 'product':'製品名', 'product__price':'金額'},
                         inplace=True)
    fig_bar = px.bar(df_order_items,
            x="注文日",
            y="金額",
            color="製品名",   )
    fig_bar.update_layout(
    width=1000,  # figureの幅
    height=450,  # figureの高さ
    yaxis = {'tick0': 0,
                'dtick': 5000},
    title={
        "text": "日付別売上推移",
        # グラフタイトルのスタイル
        "font": {"family": "Courier", "size": 20, "color": "slategray"},
        },
        margin={"l": 20, "r": 20, "t": 40, "b": 40},  # 余白
        paper_bgcolor="lightyellow",  # グラフ領域の背景色
        )
    fig_bar.update_xaxes(rangeslider={"visible":True})  #スライダーを表示
    fig_bar.update_xaxes(tickvals=df_order_items['注文日'],tickformat="%Y年%m月%d日") #軸の値
    fig_bar.update_yaxes(tickvals=df_order_items['金額'],tickformat=",d") #軸の値
    #y軸に表示する値を指定
    fig_bar.update_yaxes(tickvals = [0, 2500, 5000, 7500, 10000, 12500, 15000, 17500, 20000, 22570, 25000],)
    plot_fig_bar = fig_bar.to_html(fig_bar, include_plotlyjs=True)
    return plot_fig_bar
