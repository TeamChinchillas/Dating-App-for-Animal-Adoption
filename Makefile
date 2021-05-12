.PHONY: reset_database
reset_database:
	rm animal_adoption/db.sqlite 
	docker-compose exec backend python animal_adoption/models/initialize_db_data.py