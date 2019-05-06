docker-compose exec -T db mysql -uroot <<< 'drop database thread_bbs_test'
docker-compose exec -T db mysql -uroot <<< 'create database thread_bbs_test'
docker-compose exec -T db mysql -uroot thread_bbs_test < db/schema.sql
