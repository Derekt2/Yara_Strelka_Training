

# YARA Strelka Training

The purpose of this training is to act as an environment for users to build YARA rules and submit files to Strelka for practicals given during ([FIRSTCon 2021's Workshop: Using YARA & Strelka to Identify & Detect Malware](https://events.first.org/session_catalog/#/attendee/80DBEEC9-CA26-4408-BB12-A7E2E964DB04/catalog)).

This repository includes the following technologies:
    - Guacamolee: Remote access for users
    - Postgres: Managing users
    - OpenSSH: Server users will access

In addition to this repository, users should also stand up a modified version of [Strelka](https://github.com/phutelmyer/strelka) that was slightly modified to communicate with the OpenSSH server.

## Prerequisites

 - `docker  `
 - `docker-compose`

## Setup
1. Clone this repo.
2. Clone the modified Strelka repo (https://github.com/phutelmyer/strelka).
3. Run `docker network create net` to create the network the two repositories will communicate on.
4. Rename `prod.env.example` to `.env` and set values accordingly.
5. Run `docker-compose up` while in the current working directory for the Strelka repo.
6. Run `docker-compose -f build/docker-compose.yaml up` while in the current working directory for the Strelka repo.

## Usage
With setup complete, you will have both the remote server and Strelka running on the same docker network. Users can now access the SSH server with the following steps:
1. Visit http://localhost:8080/guacamole
2. Login with default credentials (guacadmin:guacadmin)
3. Setup a new connection to `127.0.0.1` port `2222` using the credentials specified in the .env file.

## Warning
In its current form, the SSH server was unable to be built / accessed on a Mac OSX test environment. This project was successfully built and tested on Ubuntu.
