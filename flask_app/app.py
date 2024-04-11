
from pydantic import ValidationError
from redis_om import NotFoundError, Migrator
from ResumeModel import Resume, ResumeWithId
import logging

logging.basicConfig(filename='error.log',
                    format='[%(asctime)s] => %(message)s',
                    level=logging.ERROR)

from flask import Flask, request

app = Flask('__name__')


@app.route('/resume/<string:resume_id>', methods=['GET', 'PUT'])
def get_resume(resume_id):
    if request.method == 'GET':
        try:
            resume = Resume.get(resume_id)
            return resume.dict()
        except NotFoundError:
            return {}
    else:
        try:
            resume = ResumeWithId.get(resume_id)
            resume.update(**request.json)
            print(resume.save())
        except NotFoundError:
            resume = Resume(**request.json)
            resume.save()
            return 'succ', 200


@app.route('/resume', methods=['POST'])
def add_resume():
    try:
        resume = Resume(**request.json)
        resume.save()
        return resume.pk
    except ValidationError:
        return "Bad request.", 400


if __name__ == '__main__':
    Migrator().run()
    app.run(host='0.0.0.0', debug=True, load_dotenv=True,port=8080)
