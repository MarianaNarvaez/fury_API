from flask import Blueprint, request, redirect, render_template, jsonify
from app.item.item import ITEM
import logging
 
item = Blueprint("item", __name__)

logging.basicConfig(
    format='%(asctime)s - %(levelname)s : %(message)s', level=logging.INFO)


@item.route('/', methods=['GET'])
def home():
    #Test output
    books = [
        {'id': 0,
        'title': 'A Fire Upon the Deep',
        'author': 'Vernor Vinge',
        'first_sentence': 'The coldsleep itself was dreamless.',
        'year_published': '1992'}
    ]
    return jsonify(books)

@item.route('/get_val', methods=['GET'])
def get_val():
    ite_item_id = request.args.get('ite_item_id')
    val = ITEM().get(ite_item_id)
    return jsonify(val)

@item.route('/add_item', methods=['POST'])
def add_item():
    ite_item_id = request.args.get('ite_item_id')
    ite_item_title = request.args.get('ite_item_title')
    ite_date_created = request.args.get('ite_date_created')
    ite_condition = request.args.get('ite_condition')
    res = ITEM().add_item(ite_item_id,ite_item_title,ite_date_created,ite_condition)
    return res

@item.route('/delete', methods=['GET'])
def delete():
    ite_item_id = request.args.get('ite_item_id')
    res = ITEM().del_item(ite_item_id)
    return jsonify(res)

@item.route('/update', methods=['POST'])
def update():
    ite_item_id = request.args.get('ite_item_id')
    ite_item_title = request.args.get('ite_item_title')
    ite_date_created = request.args.get('ite_date_created')
    ite_condition = request.args.get('ite_condition')
    res = ITEM().update_item(ite_item_id,ite_item_title,ite_date_created,ite_condition)
    return jsonify(res)

@item.route('/insert_all', methods=['GET'])
def insert_all():
    res = ITEM().insert_all_items()
    return jsonify(res)





