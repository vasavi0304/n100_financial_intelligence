load:
	python src/etl/loader.py

ratios:
	python src/etl/ratios.py

test:
	pytest tests/

report:
	python src/reports/generate_report.py

dashboard:
	streamlit run dashboard/app.py

api:
	python src/api/main.py

clean:
	del /Q output\*.csv