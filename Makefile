run:
	uvicorn --port 5000 app.main:app --reload

test:
	pytest -vv .
