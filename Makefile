container:
	docker build -t sm_asr_console_builder -f Dockerfile .

lint: container
	docker run --rm -it --entrypoint=make sm_asr_console_builder lint_local

lint_local:
	pycodestyle --max-line-length=120 --exclude="swagger_client*" /src
	pylint --max-line-length=120 --ignore="swagger_client" /src
