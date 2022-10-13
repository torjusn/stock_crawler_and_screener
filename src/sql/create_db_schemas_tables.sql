/*
create database, schema and tables
*/

-- create and connect to db
CREATE DATABASE stocks;
\connect stocks;

-- create schemas
CREATE SCHEMA data;
CREATE SCHEMA metadata;

-- create tables
CREATE TABLE metadata.tracked_stocks(
  nasdaq_code text NOT NULL,
  company_name text NOT NULL,
  selection_date date,
  CONSTRAINT "metadata.tracked_stocks_pkey" PRIMARY KEY(nasdaq_code)
);