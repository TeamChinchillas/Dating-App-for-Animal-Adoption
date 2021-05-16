.PHONY: reset_local_sqlite
reset_local_sqlite:
	rm animal_adoption/db.sqlite 
	docker-compose exec \
	-e DATABASE_URL='' \
	backend python animal_adoption/models/initialize_db_data.py

.PHONY: reset_heroku_postgresql
reset_heroku_postgresql:
	docker-compose exec \
	-e DATABASE_URL=postgres://ymsgryafxludsu:ea9081a4c84463b0b51416e979d8e0949c2d4cf13b4ad99106f675cc99665005@ec2-54-224-120-186.compute-1.amazonaws.com:5432/dcsr00e7288r5r \
	backend python animal_adoption/models/initialize_db_data.py

.PHONY: test
test:
	docker-compose exec backend pytest