FROM python:3

WORKDIR /Documents/taxfix

COPY . /Documents/taxfix

RUN pip install simplejson

RUN pip install jsonschema

RUN pip install ijson

RUN pip install plotly

RUN pip install pandas

RUN pip install kaleido
	
CMD [ "python", "schema_validator.py" ]

CMD [ "python", "report.py" ]