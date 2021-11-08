from flask import Flask, request, jsonify
from flask_cors import CORS
import config

from database.database import db

import redis


from model.service import getUser

app = Flask(__name__)

app.config.from_object(config)
db.init_app(app)


@app.route('/api/index', methods=['POST'])
def getUser():
    user_id = request.json['id']
    try:
        data = getUser(id=user_id)
        code = 200
        msg = ''
    except :
        data = ''
        code = 400
        msg = 'error'
    return jsonify({
        'code': code,
        'data': data,
        'msg': msg
    })


# 对于经常访问的数据可以放在redis中
# r = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, password=config.REDIS_PASSWORD)
# r.hmset(key, value)
# data = r.hgetall(key)

if __name__ == '__main__':
    CORS(app, supports_credentials=True)
    CORS(app, resources=r'/*')
    app.run(host='0.0.0.0', port=5000, debug=1)
