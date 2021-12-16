from sqlalchemy import create_engine, orm

from flask import Flask, request, abort
from region import Region


app = Flask(__name__)
engine = create_engine('mysql+pymysql://root:@database:3306/db', pool_recycle=3600)
session = orm.Session(engine)


@app.errorhandler(404)
def page_not_found(e):
    return 'Not Found: 404', 404


@app.route('/health')
def health():
    return 'ok', 200


@app.route('/')
def handler():
    id_ = request.args.get('id')
    if id_ is None:
        abort(404)
    region = session.query(Region).get({'id': id_})
    if region is None:
        abort(404)
    return f"region: {region.name}, population: {region.population}"
