from pydantic import ValidationError
from redis_om import NotFoundError, Migrator
from ResumeModel import Resume
import logging

logging.basicConfig(filename='error.log',
                    format='[%(asctime)s] => %(message)s',
                    level=logging.ERROR)

from flask import Flask, request

app = Flask('__name__')


@app.route('/resume/<string:resume_id>', methods=['GET'])
def get_resume(resume_id):
    try:
        resume = Resume.get(resume_id)
        return resume.dict()
    except NotFoundError:
        return {}


@app.route('/resume', methods=['POST'])
def create_resume():
    try:
        resume = Resume(**request.json)
        resume.save()
        return resume.pk
    except ValidationError:
        return "Bad request.", 400


@app.route('/resume', methods=['PUT'])
def put_resume():
    try:
        resume = Resume.get(request.json.get('pk'))
        resume.update(**request.json)
        return resume.save()
    except NotFoundError:
        resume = Resume(**request.json)
        return resume.save()



if __name__ == '__main__':
    Migrator().run()
    app.run(host='0.0.0.0', debug=True, load_dotenv=True, port=8080)
