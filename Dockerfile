FROM public.ecr.aws/lambda/python:3.12

COPY requirements.txt ${LAMBDA_TASK_ROOT}

RUN pip install -r requirements.txt

COPY src ${LAMBDA_TASK_ROOT}/src
COPY index.py ${LAMBDA_TASK_ROOT}

CMD [ "index.handler" ]