#!/bin/sh
cd ..
docker compose run airflow-cli airflow config list
