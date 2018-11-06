container:
	docker build -t sm_asr_console_builder -f Dockerfile .

lint: container
	docker run --rm -it --entrypoint='make lint_local' sm_asr_console_builder

lint_local:
	lint
