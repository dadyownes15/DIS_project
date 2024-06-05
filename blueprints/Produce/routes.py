from flask import render_template, request, Blueprint

from GreenGroceries.forms import FilterBooksForm, 
from GreenGroceries.models import Produce as ProduceModel, ProduceOrder
from GreenGroceries.queries import insert_produce, get_produce_by_pk, Sell, \
    insert_sell, get_all_produce_by_farmer, get_produce_by_filters, insert_produce_order, update_sell, \
    get_orders_by_customer_pk

Produce = Blueprint('Produce', __name__)

@Produce.route("/produce")
def produce():
    form = FilterProduceForm()
    title = 'Our produce!'
    produce = []
    return render_template('pages/produce.html', produce=produce, form=form, title=title)